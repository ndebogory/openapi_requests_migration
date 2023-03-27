from hamcrest import assert_that, equal_to, greater_than

from utils.generator_helper import get_pets_by_generator


def test_get_pets_by_generator():
    pets_response = get_pets_by_generator(status=["available"])

    assert_that(pets_response.status_code, equal_to(200), "Status code is not 200")
    assert_that(len(pets_response.json()), greater_than(0), "Pets list is empty")
