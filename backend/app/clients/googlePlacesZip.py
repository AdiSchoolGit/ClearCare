import os

import requests
from dotenv import load_dotenv

load_dotenv()

GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"


# Pass zip code and get latitude/longitude coordinates
def geocode_zip(zip_code: str) -> dict:
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_MAPS_API_KEY is not set")

    response = requests.get(
        GEOCODE_URL,
        params={
            "components": f"country:US|postal_code:{zip_code}",  # Documentation discusses requiring plus codes, however going without seems to work fine
            "key": api_key,
        },
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()

    if not data.get("results"):
        raise ValueError("No coordinates found for that ZIP code")

    location = data["results"][0]["geometry"]["location"]
    return {
        "latitude": location["lat"],
        "longitude": location["lng"],
    }
