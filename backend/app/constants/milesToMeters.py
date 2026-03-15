# Store constants for conversions
# Maps increments every 5 miles to meters

MILES_TO_METERS = 1609.34

SEARCH_RADII_MILES = [5, 10, 15, 20, 25]

SEARCH_RADII_METERS = {
    miles: int(miles * MILES_TO_METERS) for miles in SEARCH_RADII_MILES
}
