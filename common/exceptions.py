class PartnerServiceException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class InvitationServiceException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

#
# Explanation:
#
# PartnerServiceException & InvitationServiceException: These are custom exception classes that extend Python’s built-in Exception class.
# They accept a message when raised and store it in the message attribute.
# super().__init__(self.message) calls the base class’s initializer to properly initialize the exception object.
# Custom exceptions help to handle specific errors more effectively and distinguish between different failure scenarios (partner service issues vs. invitation service issues).