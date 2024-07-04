from uuid import uuid4

from sqlalchemy import Column, UUID, SmallInteger, Date
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import relationship
from models.base_model import Base
from enum import Enum

class PeriodTypeEnum(Enum):
    SEMESTER = "SEMESTER"
    BIMESTER = "BIMESTER"
    TRIMESTER = "TRIMESTER"


class Period(Base):
    __tablename__ = "period"

    period_id = Column(UUID,
                       nullable=False,
                       primary_key=True, 
                       default=lambda: uuid4(),
                       )
    
    year = Column(SmallInteger, 
                  nullable=False,
                  )
    
    period_type = Column(SQLEnum(PeriodTypeEnum),
                  nullable=False,
                  )
    
    period_number = Column(SmallInteger, 
                      nullable=False,
                      )
    
    initial_date = Column(Date, 
                          nullable=False,
                          )
    
    final_date = Column(Date, 
                        nullable=False,
                        )
    
    # Relationships
    group = relationship('Group', back_populates='group')