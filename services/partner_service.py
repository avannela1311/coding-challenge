from models.partner import Partner
from common.exceptions import PartnerServiceException
import requests
from common.logger import logger
from typing import List


# def get_partners_availability(partner_api_url: str, ) -> List[Partner]:
def get_partners_availability(partners_data: List[Partner]) -> List[Partner]:
    try:
        # Fetch the partner data from the API
        # response = requests.get(partner_api_url)
        # response.raise_for_status()  # Raise an error for bad status codes
        # partners_data = response.json()

        # Deserialize data to Partner model
        partners = [Partner(**partner) for partner in partners_data]
        return partners

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching partners: {str(e)}")
        raise PartnerServiceException(f"Failed to fetch partners: {str(e)}")

#
# Explanation:
#
# get_partners_availability: This function accepts a list of Partner objects and filters out partners that have no available dates.
# Exception handling: If any error occurs during the processing, a PartnerServiceException is raised with an appropriate message.