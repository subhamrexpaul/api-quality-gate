import requests
import logging

class BaseClient:
    """
    Base API client wrapper using requests.Session() to make HTTP calls.
    Logs request URLs and response status codes for easy debugging.
    """
    
    def __init__(self, base_url: str):
        """
        Initialize the API client with a base URL and a shared Session.
        
        :param base_url: The root URL of the API (e.g., https://restful-booker.herokuapp.com)
        """
        self.base_url = base_url
        self.session = requests.Session()

    def _log_request(self, method: str, url: str, response: requests.Response):
        """Helper to print debugging information."""
        print(f"[{method}] {url} -> Status: {response.status_code}")

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a GET request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, **kwargs)
        self._log_request("GET", url, response)
        return response

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a POST request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, **kwargs)
        self._log_request("POST", url, response)
        return response

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a PUT request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, **kwargs)
        self._log_request("PUT", url, response)
        return response

    def patch(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a PATCH request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.patch(url, **kwargs)
        self._log_request("PATCH", url, response)
        return response

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a DELETE request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, **kwargs)
        self._log_request("DELETE", url, response)
        return response
