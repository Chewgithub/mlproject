from mlproject.distance import haversine
def test_type_of_haversine():
    assert type(haversine(234,234,214,234)) == float
