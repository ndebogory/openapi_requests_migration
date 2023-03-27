# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from clients._generated.petstore.paths.pet_find_by_tags import Api

from clients._generated.petstore.paths import PathValues

path = PathValues.PET_FIND_BY_TAGS