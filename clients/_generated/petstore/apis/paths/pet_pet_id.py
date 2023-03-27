from clients._generated.petstore.paths.pet_pet_id.get import ApiForget
from clients._generated.petstore.paths.pet_pet_id.post import ApiForpost
from clients._generated.petstore.paths.pet_pet_id.delete import ApiFordelete


class PetPetId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
