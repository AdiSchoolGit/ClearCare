import os

import requests

PLACES_NEARBY_URL = "https://places.googleapis.com/v1/places:searchNearby"


# Expected coordinates, which are given by the geocoding API from user input of ZIP
# Will require implementation within the services folder to integrate with geocoding API
def search_nearby_hospitals(
    latitude: float, longitude: float, radius_meters: float
) -> dict:
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": (
            "places.id,places.displayName,places.formattedAddress,places.location"
        ),
    }

    body = {
        "includedTypes": ["hospital"],
        "maxResultCount": 20,
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": latitude,
                    "longitude": longitude,
                },
                "radius": radius_meters,
            }
        },
    }

    response = requests.post(PLACES_NEARBY_URL, headers=headers, json=body, timeout=10)
    response.raise_for_status()
    return response.json()
