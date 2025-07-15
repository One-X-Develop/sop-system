from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/sops", tags=["sop"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=schemas.SOPOut, status_code=status.HTTP_201_CREATED)
def create_sop(payload: schemas.SOPCreate, db: Session = Depends(get_db)):
    sop = models.SOP(**payload.dict())
    db.add(sop)
    db.commit()
    db.refresh(sop)
    return sop

@router.get("", response_model=list[schemas.SOPOut])
def list_sops(db: Session = Depends(get_db)):
    return db.query(models.SOP).filter(models.SOP.deleted_flag.is_(False)).all()

@router.get("/{sop_id}", response_model=schemas.SOPOut)
def get_sop(sop_id: int, db: Session = Depends(get_db)):
    sop = db.query(models.SOP).get(sop_id)
    if not sop or sop.deleted_flag:
        raise HTTPException(status_code=404, detail="SOP not found")
    return sop

@router.put("/{sop_id}", response_model=schemas.SOPOut)
def update_sop(sop_id: int, payload: schemas.SOPUpdate, db: Session = Depends(get_db)):
    sop = db.query(models.SOP).get(sop_id)
    if not sop or sop.deleted_flag:
        raise HTTPException(status_code=404, detail="SOP not found")
    for k, v in payload.dict(exclude_unset=True).items():
        setattr(sop, k, v)
    db.commit()
    db.refresh(sop)
    return sop

@router.delete("/{sop_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sop(sop_id: int, db: Session = Depends(get_db)):
    sop = db.query(models.SOP).get(sop_id)
    if not sop or sop.deleted_flag:
        raise HTTPException(status_code=404, detail="SOP not found")
    sop.deleted_flag = True
    db.commit()
