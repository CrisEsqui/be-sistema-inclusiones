from sqlalchemy import Column, String, UUID, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4

from .base_model import Base

class CoordinationStaff(Base):

    __tablename__ = "coordination_staff"

    coordination_staff_id = Column(UUID(as_uuid=True),
                                   nullable=False,
                                   primary_key=True,
                                   default=lambda: uuid4(),
                                   )
    
    school_id = Column(UUID(as_uuid=True),
                       ForeignKey("school.school_id"),
                       nullable=False,
                       )
    
    campus_id = Column(UUID(as_uuid=True),
                       ForeignKey("campus.campus_id"),
                       nullable=False,
                       )
    
    first_name = Column(String,
                        nullable=False,
                        )
    
    last_name1 = Column(String,
                        nullable=False,
                        )
    
    last_name2 = Column(String,
                        nullable=False,
                        )
    
    user = Column(String,
                  nullable=False,
                  unique=True,
                  )
    
    password = Column(String,
                      nullable=False,
                      )
    
    # Relationships
    school = relationship("School", back_populates="school")
    campus = relationship("Campus", back_populates="campus")