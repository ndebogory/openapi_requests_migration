from typing import Optional

from requests import Request, Session, Response


def send_request(
        endpoint_url: str,
        method_type: str = "GET",
        data: Optional[dict] = None,
        additional_headers: Optional[dict] = None,
        params=""
):
    s = Session()

    prepared_request = Request(
        method=method_type,
        url=endpoint_url,
        headers=additional_headers,
        json=data,
        params=params,
    ).prepare()

    response = s.send(prepared_request)

    request_response_logging(response)

    return response


def request_response_logging(response: Response):
    print(f"Request: {response.request.method} {response.request.url}")
    print(f"Response: {response.status_code} {response.reason}")
    print(f"Response body: {response.text}")
