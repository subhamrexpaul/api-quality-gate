from .base_client import BaseClient
import requests

class BookingAPI(BaseClient):
    """
    Client for interacting with the Booking endpoints of the Restful-Booker API.
    """

    def get_all_bookings(self) -> requests.Response:
        """
        Retrieve all booking IDs.
        
        :return: The Response object containing a list of booking objects (with 'bookingid')
        """
        return self.get("/booking")

    def get_booking(self, booking_id: int) -> requests.Response:
        """
        Retrieve details of a specific booking by its ID.
        
        :param booking_id: The integer ID of the booking to retrieve.
        :return: The Response object containing the booking details.
        """
        return self.get(f"/booking/{booking_id}")

    def create_booking(self, data: dict) -> requests.Response:
        """
        Create a new booking.
        
        Note: The API quirk is that this returns a 200 OK instead of 201 Created.
        
        :param data: A dictionary representing the booking details payload.
        :return: The Response object containing the created booking details and ID.
        """
        return self.post("/booking", json=data)

    def update_booking(self, booking_id: int, data: dict, token: str) -> requests.Response:
        """
        Fully update an existing booking. Requires authentication.
        
        :param booking_id: The ID of the booking to update.
        :param data: The complete dictionary of the updated booking details.
        :param token: The authentication token string.
        :return: The Response object containing the updated booking details.
        """
        # Adding the required Cookie header containing the token
        headers = {"Cookie": f"token={token}"}
        return self.put(f"/booking/{booking_id}", json=data, headers=headers)

    def partial_update(self, booking_id: int, data: dict, token: str) -> requests.Response:
        """
        Partially update an existing booking. Requires authentication.
        
        :param booking_id: The ID of the booking to update.
        :param data: A dictionary containing only the fields to update.
        :param token: The authentication token string.
        :return: The Response object containing the updated booking details.
        """
        # Adding the required Cookie header containing the token
        headers = {"Cookie": f"token={token}"}
        return self.patch(f"/booking/{booking_id}", json=data, headers=headers)

    def delete_booking(self, booking_id: int, token: str) -> requests.Response:
        """
        Delete a booking by its ID. Requires authentication.
        
        Note: The API quirk is that this returns 201 Created instead of 204 No Content.
        
        :param booking_id: The ID of the booking to delete.
        :param token: The authentication token string.
        :return: The Response object.
        """
        # Adding the required Cookie header containing the token
        headers = {"Cookie": f"token={token}"}
        return self.delete(f"/booking/{booking_id}", headers=headers)
