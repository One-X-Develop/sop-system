from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from .database import Base

class SOP(Base):
    __tablename__ = "sops"

    sop_id        = Column(Integer, primary_key=True, index=True)           # 唯一标识
    sop_code      = Column(String(64), unique=True, nullable=False)         # SOP编号
    title         = Column(String(128), nullable=False)                     # 标题
    description   = Column(Text, nullable=False)                            # 描述
    steps         = Column(JSONB, nullable=False)                           # 步骤(JSON)
    version       = Column(String(32), nullable=False, default="1.0")       # 版本号
    status        = Column(String(32), nullable=False, default="draft")     # 状态
    created_at    = Column(DateTime(timezone=True), server_default=func.now())
    updated_at    = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_flag  = Column(Boolean, nullable=False, default=False)          # 软删除
