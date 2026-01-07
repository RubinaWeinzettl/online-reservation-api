from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import enforce_tenant, require_role
from app.models.booking import Booking
from app.models.schedule import ScheduleSlot
from app.schemas.booking import BookingCreate, BookingResponse

router = APIRouter()


@router.post(
    "/business/{business_id}/bookings",
    response_model=BookingResponse,
)
def create_booking(
    business_id: int,
    payload: BookingCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role(["business"])),
):
    enforce_tenant(business_id, user)
    slot = (
        db.query(ScheduleSlot)
        .filter(
            ScheduleSlot.id == payload.slot_id,
            ScheduleSlot.business_id == business_id,
        )
        .first()
    )
    if slot is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Slot not found",
        )
    if slot.is_booked:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Slot already booked",
        )

    slot.is_booked = True
    booking = Booking(
        business_id=business_id,
        slot_id=payload.slot_id,
        customer_id=payload.customer_id,
        status="confirmed",
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking
