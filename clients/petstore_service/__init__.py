from clients._generated.petstore import PetApi, ApiClient, Configuration
from conftest import PETSTORE_URL, PETSTORE_V2_URL

petstore_client = PetApi(
    api_client=ApiClient(
        configuration=Configuration(
            host=PETSTORE_URL,
        )
    )
)


petstore_old_client = PetApi(
    api_client=ApiClient(
        configuration=Configuration(
            host=PETSTORE_V2_URL,
        )
    )
)
