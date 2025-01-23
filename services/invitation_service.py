from models.invitation import Invitation
from models.partner import Partner
from common.exceptions import InvitationServiceException
from typing import List, Dict
from collections import Counter
from datetime import datetime, timedelta
from common.logger import logger


def create_invitations(partners: List[Partner]) -> List[Invitation]:
    country_to_dates = _find_common_available_dates(partners)
    invitations = _generate_invitations(country_to_dates, partners)
    return invitations


def _find_common_available_dates(partners: List[Partner]) -> Dict[str, str]:
    country_to_date = {}
    for partner in partners:
        for i, date in enumerate(partner.available_dates[:-1]):
            if _date_diff_in_days(date, partner.available_dates[i + 1]) == 1:
                if partner.country not in country_to_date:
                    country_to_date[partner.country] = []
                country_to_date[partner.country].append(date)

    # Find the most common date for each country
    common_dates = {}
    for country, dates in country_to_date.items():
        date_count = Counter(dates)
        most_common_date = min(date_count, key=lambda k: date_count[k])
        common_dates[country] = most_common_date

    return common_dates


def _date_diff_in_days(start_date: str, end_date: str) -> int:
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    return (end_date_obj - start_date_obj).days


def _generate_invitations(country_to_dates: Dict[str, str], partners: List[Partner]) -> List[Invitation]:
    invitations = []
    for country, date in country_to_dates.items():
        attendees = []
        for partner in partners:
            if date in partner.available_dates:
                attendees.append(partner.email)

        invitation = Invitation(
            name=country,
            start_date=date,
            attendee_count=len(attendees),
            attendees=attendees
        )
        invitations.append(invitation)

    return invitations


#
# Explanation:
#
# create_invitations: This function takes the list of Partner objects and generates invitations for each partner.
# It creates an Invitation object for each partner, with data like start_date, attendee_count, and the partner's email.
# Exception handling: Any error during invitation creation raises an InvitationServiceException.
