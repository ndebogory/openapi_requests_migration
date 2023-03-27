# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from clients._generated.petstore.paths.user_create_with_list import Api

from clients._generated.petstore.paths import PathValues

path = PathValues.USER_CREATE_WITH_LIST