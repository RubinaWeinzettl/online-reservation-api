from typing import Optional

from pydantic import BaseModel


class TokenPayload(BaseModel):
    sub: str
    role: str
    tenant_id: Optional[int] = None
