from clients.petstore_service import petstore_client, petstore_old_client
from clients._generated.petstore.exceptions import ApiException


def get_pets_by_generator(status: list[str], is_new: bool = True):
    if is_new:
        request_response = petstore_client.find_pets_by_status_with_http_info(status=status)
    else:
        request_response = petstore_old_client.find_pets_by_status_with_http_info(status=status)

    return request_response.data


def get_pets_by_generator_error(status: list[str]):
    try:
        petstore_client.find_pets_by_status_with_http_info(status=status)
    except ApiException as exception_error:
        return exception_error
