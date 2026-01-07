from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from app.models import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("businesses.id"), nullable=False)
    slot_id = Column(Integer, ForeignKey("schedule_slots.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    status = Column(String(50), default="confirmed")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    business = relationship("Business")
    slot = relationship("ScheduleSlot")
    customer = relationship("Customer")
