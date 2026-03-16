from unittest.mock import patch

import pytest
from app.services.hospitalSearch import find_hospitals_by_zip


@patch("app.services.hospitalSearch.search_nearby_hospitals")
@patch("app.services.hospitalSearch.geocode_zip")
def test_find_hospitals_by_zip_success(mock_geocode_zip, mock_search_nearby_hospitals):
    mock_geocode_zip.return_value = {
        "latitude": 32.8801,
        "longitude": -117.2340,
    }

    mock_search_nearby_hospitals.return_value = {
        "places": [
            {
                "id": "places/test123",
                "displayName": {"text": "UC San Diego Medical Center"},
                "formattedAddress": "200 W Arbor Dr, San Diego, CA",
                "location": {
                    "latitude": 32.7539,
                    "longitude": -117.1661,
                },
            }
        ]
    }

    result = find_hospitals_by_zip("92122", 10)

    assert result == {
        "places": [
            {
                "id": "places/test123",
                "displayName": {"text": "UC San Diego Medical Center"},
                "formattedAddress": "200 W Arbor Dr, San Diego, CA",
                "location": {
                    "latitude": 32.7539,
                    "longitude": -117.1661,
                },
            }
        ]
    }

    mock_geocode_zip.assert_called_once_with("92122")
    mock_search_nearby_hospitals.assert_called_once_with(
        latitude=32.8801,
        longitude=-117.2340,
        radius_meters=16093,
    )


def test_find_hospitals_by_zip_invalid_radius():
    with pytest.raises(ValueError, match="Invalid radius"):
        find_hospitals_by_zip("92122", 11)


pytest.mark.real


def test_real_google_search():
    from app.services.hospitalSearch import find_hospitals_by_zip

    results = find_hospitals_by_zip("92122", 10)

    assert "places" in results
    assert len(results["places"]) > 0
