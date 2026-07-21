from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter
from safecity_platform.db.db_model import DBIncident, get_db
from safecity_platform.dto.data_transf_obj import IncidentRequest, IncidentResponse
incident_router = APIRouter()



@incident_router.post("/new" , response_model=IncidentResponse, status_code=status.HTTP_201_CREATED)
def create_incident(data: IncidentRequest, db: Session = Depends(get_db)):
    db_incident = DBIncident(
        title=data.title,
        incident_category=data.incident_category,
        law_breaking_category=data.law_breaking_category
    )
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident


@incident_router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(incident_id: str, db: Session = Depends(get_db)):
    db_incident = db.query(DBIncident).filter(DBIncident.id == incident_id).first()
    if not db_incident:
        raise HTTPException(status_code=404, detail="Инцидент не найден")
    return db_incident