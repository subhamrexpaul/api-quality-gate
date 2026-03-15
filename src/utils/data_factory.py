from faker import Faker
import random

# Initialize Faker instance for generating realistic test data
fake = Faker()


def generate_booking() -> dict:
    """
    Generate a valid booking payload with random data using Faker.
    Matches the exact request body shape expected by POST /booking.

    :return: A dict with firstname, lastname, totalprice, depositpaid,
             bookingdates (checkin/checkout), and additionalneeds.
    """
    # Generate a future check-in date (between 1 and 30 days from now)
    checkin = fake.date_between(start_date="+1d", end_date="+30d")
    # Checkout is always after check-in (between 1 and 14 days after checkin)
    from datetime import timedelta
    checkout = checkin + timedelta(days=random.randint(1, 14))


    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": random.randint(50, 500),
        "depositpaid": random.choice([True, False]),
        "bookingdates": {
            "checkin": checkin.isoformat(),
            "checkout": checkout.isoformat()
        },
        "additionalneeds": random.choice([
            "Breakfast", "Lunch", "Dinner", "WiFi",
            "Parking", "Late Checkout", "Extra Pillows"
        ])
    }


def generate_invalid_booking() -> dict:
    """
    Generate an invalid booking payload with missing required fields.
    Used for negative testing — to verify the API rejects bad data.

    :return: A dict missing 'firstname' and 'bookingdates' (required fields).
    """
    # Deliberately missing 'firstname' and 'bookingdates' to trigger validation errors
    return {
        "lastname": fake.last_name(),
        "totalprice": random.randint(50, 500),
        "depositpaid": random.choice([True, False])
    }

