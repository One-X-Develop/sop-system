from pydantic import BaseModel
from typing import Any, Optional

class SOPBase(BaseModel):
    sop_code: str
    title: str
    description: str
    steps: Any                 # 任意 JSON
    version: str = "1.0"
    status: str = "draft"

class SOPCreate(SOPBase):
    pass                        # 全量必填

class SOPUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    steps: Optional[Any] = None
    version: Optional[str] = None
    status: Optional[str] = None

class SOPOut(SOPBase):
    sop_id: int

    class Config:
        orm_mode = True
