from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import enforce_tenant, require_role
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerResponse

router = APIRouter()


@router.post(
    "/business/{business_id}/customers",
    response_model=CustomerResponse,
)
def create_customer(
    business_id: int,
    payload: CustomerCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role(["business"])),
):
    enforce_tenant(business_id, user)
    customer = Customer(
        business_id=business_id,
        full_name=payload.full_name,
        email=payload.email,
    )
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer
