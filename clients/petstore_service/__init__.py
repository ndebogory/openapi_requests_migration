from clients._generated.petstore import PetApi, ApiClient, Configuration
from conftest import PETSTORE_URL


petstore_client = PetApi(
    api_client=ApiClient(
        configuration=Configuration(
            host=PETSTORE_URL,
        )
    )
)
