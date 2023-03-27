from conftest import PETSTORE_URL
from utils.http_requests import send_request

get_pets_by_status_path = "/pet/findByStatus"


def get_pets_by_requests(status: [str]):
    url = f"{PETSTORE_URL}{get_pets_by_status_path}"

    request_response = send_request(
        endpoint_url=url,
        params={"status": status}
    )

    return request_response
