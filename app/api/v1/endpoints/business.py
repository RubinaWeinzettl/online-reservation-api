from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import require_role
from app.models.business import Business
from app.schemas.business import BusinessCreate, BusinessResponse

router = APIRouter()


@router.post("/business", response_model=BusinessResponse)
def create_business(
    payload: BusinessCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role(["business"])),
):
    business = Business(name=payload.name)
    db.add(business)
    db.commit()
    db.refresh(business)
    return business
