from pydantic import BaseModel
from typing import List

class Partner(BaseModel):
    first_name: str
    last_name: str
    email: str
    country: str
    available_dates: List[str]

#
# Explanation:
#
# Partner class: A simple class with attributes like first_name, last_name, email, country, and available_dates representing a partner.
# __repr__: Provides a readable string representation of the Partner object, useful for debugging and logging.