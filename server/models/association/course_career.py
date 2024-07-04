from sqlalchemy import Column, UUID, ForeignKey
from uuid import uuid4

from models.base_model import Base

class CourseCareer(Base):

    __tablename__ = 'course_career'

    course_career_id = Column(UUID(as_uuid=True),
                              nullable=False,
                              primary_key=True,
                              default=lambda: uuid4(),
                              )

    course = Column(UUID(as_uuid=True),
                    ForeignKey('course.course_id'),
                    nullable=False,
                    )
    
    career = Column(UUID(as_uuid=True),
                    ForeignKey('career.career_id'),
                    nullable=False,
                    )