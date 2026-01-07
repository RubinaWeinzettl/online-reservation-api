from fastapi import APIRouter

from app.api.v1.endpoints import bookings, business, customers, schedule

api_router = APIRouter()

api_router.include_router(business.router, tags=["business"])
api_router.include_router(schedule.router, tags=["schedule"])
api_router.include_router(customers.router, tags=["customers"])
api_router.include_router(bookings.router, tags=["bookings"])
