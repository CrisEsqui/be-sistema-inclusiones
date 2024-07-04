from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from models.base_model import Base

from uuid import uuid4


class InclusionRequest(Base):
    __tablename__ = "inclusion_request"

    inclusion_request_id = Column(UUID(as_uuid=True), 
                                  nullable=False, 
                                  primary_key=True, 
                                  default=lambda: uuid4(),
                                  )
    
    status_id = Column(UUID(as_uuid=True),
                       ForeignKey('inclusion_status.inclusion_status_id'),
                       nullable=False,
                       )

    student_id = Column(UUID(as_uuid=True), 
                       ForeignKey('student.student_id'), 
                       nullable=False,
                       )
    
    group_id = Column(UUID(as_uuid=True), 
                          ForeignKey('group.group_id'), 
                          nullable=False,
                          )
    
    student_comment = Column(String,
                             nullable=True,
                             )
    
    coordination_comment = Column(String,
                                  nullable=True,
                                  )
    
    # Relations
    status = relationship('InclusionStatus', back_populates='inclusion_status')
    student = relationship('Student', back_populates='student')
    group = relationship('Group', back_populates='group')

    