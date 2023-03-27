from clients.petstore_service import petstore_client


def get_pets_by_generator(status: list[str]):
    request_response = petstore_client.find_pets_by_status_with_http_info(status=status)

    return request_response.data
