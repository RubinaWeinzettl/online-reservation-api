from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import enforce_tenant, require_role
from app.models.schedule import ScheduleSlot
from app.schemas.schedule import ScheduleSlotCreate, ScheduleSlotResponse

router = APIRouter()


@router.post(
    "/business/{business_id}/schedule/slots",
    response_model=ScheduleSlotResponse,
)
def create_slot(
    business_id: int,
    payload: ScheduleSlotCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role(["business"])),
):
    enforce_tenant(business_id, user)
    slot = ScheduleSlot(
        business_id=business_id,
        starts_at=payload.starts_at,
        ends_at=payload.ends_at,
        is_booked=False,
    )
    db.add(slot)
    db.commit()
    db.refresh(slot)
    return slot


@router.get(
    "/business/{business_id}/schedule/slots",
    response_model=List[ScheduleSlotResponse],
)
def list_slots(
    business_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_role(["business"])),
):
    enforce_tenant(business_id, user)
    return (
        db.query(ScheduleSlot)
        .filter(ScheduleSlot.business_id == business_id)
        .order_by(ScheduleSlot.starts_at)
        .all()
    )
