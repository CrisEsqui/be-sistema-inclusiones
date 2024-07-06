from uuid import uuid4

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship
from models.base_model import Base

class School(Base):
    __tablename__ = "school"

    school_id = Column(UUID,
                       primary_key=True, 
                       default=lambda: uuid4(),
                       )
    
    name = Column(String, 
                  nullable=False,
                  )
    
    code = Column(String,
                  nullable=False)
    
    # Relations
    career = relationship('Career', back_populates='career')
    course = relationship('Course', back_populates='course')
    coordination_staff = relationship('CoordinationStaff', back_populates='coordination_staff')
    