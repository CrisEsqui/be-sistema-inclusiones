from .base_model import Base

# Tables
from .campus_model import Campus
from .career_model import Career
from .course_model import Course
from .group_model import Group
from .inclusion_request_model import InclusionRequest
from .inclusion_status_model import InclusionStatus
from .period_model import Period
from .professor_model import Professor
from .school_model import School
from .student_model import Student

# Association tables
from .association.course_career import CourseCareer