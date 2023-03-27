import typing_extensions

from clients._generated.petstore.paths import PathValues
from clients._generated.petstore.apis.paths.pet import Pet
from clients._generated.petstore.apis.paths.pet_find_by_status import PetFindByStatus
from clients._generated.petstore.apis.paths.pet_find_by_tags import PetFindByTags
from clients._generated.petstore.apis.paths.pet_pet_id import PetPetId
from clients._generated.petstore.apis.paths.pet_pet_id_upload_image import PetPetIdUploadImage
from clients._generated.petstore.apis.paths.store_inventory import StoreInventory
from clients._generated.petstore.apis.paths.store_order import StoreOrder
from clients._generated.petstore.apis.paths.store_order_order_id import StoreOrderOrderId
from clients._generated.petstore.apis.paths.user import User
from clients._generated.petstore.apis.paths.user_create_with_array import UserCreateWithArray
from clients._generated.petstore.apis.paths.user_create_with_list import UserCreateWithList
from clients._generated.petstore.apis.paths.user_login import UserLogin
from clients._generated.petstore.apis.paths.user_logout import UserLogout
from clients._generated.petstore.apis.paths.user_username import UserUsername

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PET: Pet,
        PathValues.PET_FIND_BY_STATUS: PetFindByStatus,
        PathValues.PET_FIND_BY_TAGS: PetFindByTags,
        PathValues.PET_PET_ID: PetPetId,
        PathValues.PET_PET_ID_UPLOAD_IMAGE: PetPetIdUploadImage,
        PathValues.STORE_INVENTORY: StoreInventory,
        PathValues.STORE_ORDER: StoreOrder,
        PathValues.STORE_ORDER_ORDER_ID: StoreOrderOrderId,
        PathValues.USER: User,
        PathValues.USER_CREATE_WITH_ARRAY: UserCreateWithArray,
        PathValues.USER_CREATE_WITH_LIST: UserCreateWithList,
        PathValues.USER_LOGIN: UserLogin,
        PathValues.USER_LOGOUT: UserLogout,
        PathValues.USER_USERNAME: UserUsername,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PET: Pet,
        PathValues.PET_FIND_BY_STATUS: PetFindByStatus,
        PathValues.PET_FIND_BY_TAGS: PetFindByTags,
        PathValues.PET_PET_ID: PetPetId,
        PathValues.PET_PET_ID_UPLOAD_IMAGE: PetPetIdUploadImage,
        PathValues.STORE_INVENTORY: StoreInventory,
        PathValues.STORE_ORDER: StoreOrder,
        PathValues.STORE_ORDER_ORDER_ID: StoreOrderOrderId,
        PathValues.USER: User,
        PathValues.USER_CREATE_WITH_ARRAY: UserCreateWithArray,
        PathValues.USER_CREATE_WITH_LIST: UserCreateWithList,
        PathValues.USER_LOGIN: UserLogin,
        PathValues.USER_LOGOUT: UserLogout,
        PathValues.USER_USERNAME: UserUsername,
    }
)
