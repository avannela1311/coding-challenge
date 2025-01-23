from pydantic import BaseModel
from typing import List

class Invitation(BaseModel):
    name: str
    start_date: str
    attendee_count: int
    attendees: List[str]

#
# Explanation:
#
# Invitation class: This class represents an invitation, containing fields like name, start_date, attendee_count, and a list of attendees.
# dict method: Converts the Invitation object into a dictionary format to easily send it as a JSON response in the API.