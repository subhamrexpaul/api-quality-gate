from typing import Optional
from .base_client import BaseClient

class AuthAPI(BaseClient):
    """
    Client for interacting with the Authentication endpoints.
    """

    def get_token(self, username="admin", password="password123") -> Optional[str]:
        """
        Calls POST /auth with credentials to retrieve an authentication token.
        
        :param username: The username for authentication (default: "admin")
        :param password: The password for authentication (default: "password123")
        :return: The token string if successful, else None
        """
        payload = {
            "username": username,
            "password": password
        }
        
        # Making the POST request to the /auth endpoint
        response = self.post("/auth", json=payload)
        
        # Extracting the token from the response json if status is 200
        if response.status_code == 200:
            return response.json().get("token")
        
        # In case of failure (e.g. wrong credentials), the token might not be returned so we return None
        return None
