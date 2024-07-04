from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from models.base_model import Base

from uuid import uuid4


class Group(Base):
    __tablename__ = "group"

    group_id = Column(UUID(as_uuid=True), 
                       nullable=False, 
                       primary_key=True, 
                       default=lambda: uuid4(),
                       )

    course_id = Column(UUID(as_uuid=True), 
                       ForeignKey('course.course_id'), 
                       nullable=False,
                       )
    
    professor_id = Column(UUID(as_uuid=True), 
                          ForeignKey('professor.professor_id'), 
                          nullable=False,
                          )
    
    period_id = Column(UUID(as_uuid=True), 
                       ForeignKey('period.period_id'), 
                       nullable=False,
                       )
    
    
    campus_id = Column(UUID(as_uuid=True), 
                       ForeignKey('campus.campus_id'), 
                       nullable=False,
                       )
    
    
    
    # Relations
    course = relationship('Course', back_populates='course')
    professor = relationship('Professor', back_populates='professor')
    period = relationship('Period', back_populates='period')
    campus = relationship('Campus', back_populates='campus')

    inclusion_request = relationship('InclusionRequest', back_populates='inclusion_request')