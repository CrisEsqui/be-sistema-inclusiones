from uuid import uuid4

from sqlalchemy import Column, UUID, SmallInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.association.course_career import CourseCareer

class Course(Base):
    __tablename__ = "course"

    course_id = Column(UUID,
                       nullable=False,
                       primary_key=True, 
                       default=lambda: uuid4,
                       )
    
    school_id = Column(UUID(as_uuid=True), 
                       ForeignKey('school.school_id'), 
                       nullable=True,
                       )
    
    name = Column(String,
                  nullable=False,
                  )
    
    code = Column(String(8),
                  nullable=False,
                  )

    credits = Column(SmallInteger,
                  nullable=False,
                  )
    
    # Relationships
    school = relationship('School', back_populates='school')
    career = relationship('Career', secondary=CourseCareer, back_populates='career')

    group = relationship('Group', back_populates='group')