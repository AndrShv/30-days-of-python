from typing import Optional
from sqlalchemy.orm import Session
from uvicorn.lifespan import off

from safecity_platform.db.db_model import DBIncident
from safecity_platform.dto.data_transf_obj import IncidentResponse
from safecity_platform.utils import log_funcs


@log_funcs
def filter_incidents(db: Session, incident_category: Optional[str] = None,
                     law_breaking_category: Optional[str] = None) -> dict[str, IncidentResponse]:
    filter_incidents= {}
    incidents = db.query(DBIncident).all()
    for incident in incidents:
        if incident_category is not None and incident.incident_category == incident_category:
            filter_incidents.setdefault(incident.id, incident.incident_category)
        if law_breaking_category is not None and incident.law_breaking_category == law_breaking_category:
            filter_incidents.setdefault(incident.id, incident.law_breaking_category)
    return filter_incidents