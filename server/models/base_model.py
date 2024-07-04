from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Boolean, DateTime
from datetime import datetime
import pytz

class Base(DeclarativeBase):

    active = Column(Boolean, 
                    nullable=False, 
                    default=True,
                    )
    
    created_at = Column(DateTime(timezone=True), 
                        nullable=False, 
                        default=lambda: datetime.now(tz = pytz.utc),
                        )
    
    updated_at = Column(DateTime(timezone=True), 
                        nullable=False, 
                        default=lambda: datetime.now(tz = pytz.utc),
                        onupdate=lambda: datetime.now(tz = pytz.utc),
                        )

    def delete(self):
        self.active = False

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}