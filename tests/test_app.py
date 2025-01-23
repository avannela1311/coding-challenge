import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_generate_invitations(self):
        response = self.app.post('/generate_invitations', json={
            "partners": [
                {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "country": "US", "available_dates": ["2023-10-10", "2023-10-11"]},
                {"first_name": "Jane", "last_name": "Smith", "email": "jane.smith@example.com", "country": "US", "available_dates": ["2023-10-10", "2023-10-12"]}
            ]
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn("attendee_count", response.json[0])

if __name__ == '__main__':
    unittest.main()

#
# Explanation:
#
# TestApp: This class tests the Flask app.
# test_invitations: Tests the /invitations endpoint to ensure it returns a 200 OK status code.
