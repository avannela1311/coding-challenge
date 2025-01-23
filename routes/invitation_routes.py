from flask import Blueprint, request, jsonify

from models.partner import Partner
from services.partner_service import get_partners_availability
from services.invitation_service import create_invitations
from common.exceptions import PartnerServiceException, InvitationServiceException
from common.logger import logger
from typing import List

invitation_bp = Blueprint('invitation_bp', __name__)

@invitation_bp.route('/invitations', methods=['POST'])
def get_invitations():
    try:
        # Fetch partners' availability
        partners = get_partners_availability(request.json['partners'])  # Fetch partners from DB or API
        invitations = create_invitations(partners)
        return jsonify({'invitations':
            [inv.dict() for inv in invitations]
        })
    except (PartnerServiceException, InvitationServiceException) as e:
        return jsonify({"error": str(e)}), 500



@invitation_bp.route('/generate_invitations', methods=['POST'])
def generate_invitations():
    try:
        data = request.get_json()
        partners = [Partner(**partner) for partner in data['partners']]

        invitations = create_invitations(partners)
        return jsonify([inv.dict() for inv in invitations]), 200

    except PartnerServiceException as e:
        logger.error(f"PartnerServiceException: {e.message}")
        return jsonify({"error": f"Partner service error: {e.message}"}), 400

    except InvitationServiceException as e:
        logger.error(f"InvitationServiceException: {e.message}")
        return jsonify({"error": f"Invitation service error: {e.message}"}), 500

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

#
# Explanation:
#
# Blueprint (invitation_bp): The blueprint is used to group routes for invitations.
# GET /invitations route: This endpoint retrieves partner availability, generates invitations, and returns them as a JSON response.
# Error Handling: If either the partner or invitation service fails, a custom error message is returned with a 500 HTTP status code.