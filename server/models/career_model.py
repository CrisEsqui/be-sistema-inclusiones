from sqlalchemy import Column, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from models.base_model import Base
from models.association.course_career import CourseCareer

from uuid import uuid4


class Career(Base):
    __tablename__ = "career"

    career_id = Column(UUID(as_uuid=True), 
                       nullable=False, 
                       primary_key=True, 
                       default=lambda: uuid4(),
                       )

    school_id = Column(UUID(as_uuid=True), 
                       ForeignKey('school.school_id'), 
                       nullable=False,
                       )
    
    name = Column(String, 
                  nullable=False,
                  )
    
    code = Column(String(3), 
                  nullable=False,
                  )
        
    year = Column(SmallInteger, 
                  nullable=False,
                  )
    
    # Relationships
    school = relationship('School', back_populates='school')
    courses = relationship('Course', secondary=CourseCareer, back_populates='course')
    student = relationship('Student', back_populates='student')