import typing_extensions

from clients._generated.petstore.apis.tags import TagValues
from clients._generated.petstore.apis.tags.pet_api import PetApi
from clients._generated.petstore.apis.tags.store_api import StoreApi
from clients._generated.petstore.apis.tags.user_api import UserApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PET: PetApi,
        TagValues.STORE: StoreApi,
        TagValues.USER: UserApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PET: PetApi,
        TagValues.STORE: StoreApi,
        TagValues.USER: UserApi,
    }
)
