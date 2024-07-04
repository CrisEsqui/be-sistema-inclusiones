from uuid import uuid4
from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import validates, relationship
import re

from .base_model import Base


class Professor(Base):

    __tablename__ = 'professor'

    professor_id = Column(UUID(as_uuid=True),
                          nullable=False,
                          primary_key=True,
                          default=lambda: uuid4(),
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
    
    email_address = Column(String,
                  nullable=False,
                  )
    
    # Relationships
    group = relationship('Group', back_populates='group')

    @validates('email_address')
    def validate_email_address(self, field_name, email_address):
        regex = re.compile(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')
        is_valid = bool(regex.match(email_address))

        if is_valid is False:
            raise ValueError('Invalid email address')
        
        return email_address