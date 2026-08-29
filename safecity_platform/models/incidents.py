class Incident:
    id: str
    title: str
    incident_category: str
    law_breaking_category: str

    def __str__(self):
        return (f"Incident ID: {self.id}, "
                f"Title: {self.title}, "
                f"Incident Category: {self.incident_category}, "
                f"Law Breaking Category: {self.law_breaking_category}")
