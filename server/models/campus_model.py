from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship

from models.base_model import Base

from uuid import uuid4


class Campus(Base):
    __tablename__ = "campus"

    campus_id = Column(UUID(as_uuid=True), 
                       nullable=False, 
                       primary_key=True,
                       default=lambda: uuid4(),
                       )
    
    name = Column(String, 
                  nullable=False,
                  )
    
    code = Column(String, 
                  nullable=False,
                  )
    
    # Relationships
    group = relationship('Group', back_populates='group')
    coordination_staff = relationship('CoordinationStaff', back_populates='coordination_staff')