import json
import jsonschema


def assert_status_code(response, expected_code: int):
    """
    Assert that the response status code matches the expected value.

    :param response: The requests.Response object.
    :param expected_code: The expected HTTP status code (e.g., 200, 201, 404).
    """
    assert response.status_code == expected_code, (
        f"Expected status {expected_code}, got {response.status_code}. "
        f"Response body: {response.text[:200]}"
    )


def assert_response_time(response, max_seconds: float = 3.0):
    """
    Assert that the API response time is under the specified threshold.

    :param response: The requests.Response object.
    :param max_seconds: Maximum acceptable response time in seconds (default: 3.0).
    """
    elapsed = response.elapsed.total_seconds()
    assert elapsed < max_seconds, (
        f"Response took {elapsed:.2f}s, expected under {max_seconds}s"
    )


def assert_valid_schema(data: dict, schema_path: str):
    """
    Validate a response body against a JSON Schema file.

    :param data: The response body as a dict.
    :param schema_path: The file path to the JSON Schema .json file.
    """
    with open(schema_path, "r") as f:
        schema = json.load(f)
    # jsonschema.validate() raises ValidationError if schema doesn't match
    jsonschema.validate(instance=data, schema=schema)
