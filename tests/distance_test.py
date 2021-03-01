from new_package.distance import haversine

def test_haversine():
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 44.8548021, -0.5719717
    distance = haversine(lon1, lat1, lon2, lat2)
    assert distance == haversine(lon1, lat1, lon2, lat2)
