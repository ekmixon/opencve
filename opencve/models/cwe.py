from opencve.extensions import db
from opencve.models import BaseModel


class Cwe(BaseModel):
    __tablename__ = "cwes"

    cwe_id = db.Column(db.String(), nullable=False, index=True)
    name = db.Column(db.String())
    description = db.Column(db.String())

    @property
    def short_id(self):
        return self.cwe_id.split("CWE-")[1] if self.cwe_id.startswith("CWE-") else None

    def __repr__(self):
        return f"<Cwe {self.cwe_id}>"
