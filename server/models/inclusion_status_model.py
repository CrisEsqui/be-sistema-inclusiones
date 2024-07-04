from uuid import uuid4

from sqlalchemy import Column, UUID, SmallInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.association.course_career import CourseCareer

class InclusionStatus(Base):
    __tablename__ = "inclusion_status"

    inclusion_status_id = Column(UUID,
                                 nullable=False,
                                 primary_key=True, 
                                 default=lambda: uuid4,
                                 )
    
    name = Column(String,
                  nullable=False,
                  )
    
    description = Column(String,
                         nullable=False,
                         default='',
                         )
    
    # Relationships
    inclusion_request = relationship('InclusionRequest', back_populates='inclusion_request')