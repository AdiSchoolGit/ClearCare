from app.clients.googlePlacesClient import search_nearby_hospitals
from app.clients.googlePlacesZip import geocode_zip
from app.constants.milesToMeters import SEARCH_RADII_METERS


def find_hospitals_by_zip(zip_code: str, radius_miles: int):
    # miles range 5 to 25, increments of 5 only.
    if radius_miles not in SEARCH_RADII_METERS:
        raise ValueError("Invalid radius")

    radius_meters = SEARCH_RADII_METERS[radius_miles]

    # API call 1
    coords = geocode_zip(zip_code)

    # API call 2, returns JSON
    return search_nearby_hospitals(
        latitude=coords["latitude"],
        longitude=coords["longitude"],
        radius_meters=radius_meters,
    )
