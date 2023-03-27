from clients._generated.petstore.paths.pet.put import ApiForput
from clients._generated.petstore.paths.pet.post import ApiForpost


class Pet(
    ApiForput,
    ApiForpost,
):
    pass
