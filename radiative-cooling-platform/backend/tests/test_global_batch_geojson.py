def test_geojson_structure():
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        55.2708,
                        25.2048,
                    ],
                },
                "properties": {
                    "city_id": "dubai",
                    "climate_adaptation_rate_percent": 75,
                },
            }
        ],
    }

    assert geojson["type"] == (
        "FeatureCollection"
    )

    assert (
        geojson["features"][0]
        ["geometry"]["type"]
        == "Point"
    )