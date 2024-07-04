from uuid import uuid4
from sqlalchemy import Column, String, UUID, ForeignKey
from sqlalchemy.orm import validates, relationship
import re

from .base_model import Base


class Student(Base):

    __tablename__ = 'student'

    student_id = Column(UUID(as_uuid=True),
                          nullable=False,
                          primary_key=True,
                          default=lambda: uuid4(),
                          )
    
    career_id = Column(UUID(as_uuid=True),
                       ForeignKey('career.career_id'),
                       nullable=False,
                       )
    
    carnet_number = Column(String,
                           nullable=False,
                           unique=True,
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
    carrer = relationship('Career', back_populates='career')

    inclusion_request = relationship('InclusionRequest', back_populates='inclusion_request')

    # Validators
    @validates('email_address')
    def validate_email_address(self, field_name, email_address):
        regex = re.compile(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')
        is_valid = bool(regex.match(email_address))

        if is_valid is False:
            raise ValueError('Invalid email address')
        
        return email_address