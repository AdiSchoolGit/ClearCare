from app.services.hospitalSearch import find_hospitals_by_zip
from app.services.pricingService import enrich_hospitals_with_pricing
from flask import Blueprint, jsonify, request

bp = Blueprint("search", __name__, url_prefix="/api/search")


# Send a GET request to /api/search/hospitals to search for hospitals by zip code and radius
# Returns 20 results within given radius of zip code, edit /clients/googlePlacesClient.py to change max results returned
# Following mozilla HTTP response codes
#
@bp.route("/hospitals", methods=["GET"])
def search_hospitals():
    zip_code = request.args.get("zip")
    radius = request.args.get("radius", default=10, type=int)
    insurance = request.args.get("insurance", default="uninsured")
    procedure = request.args.get("procedure", default="general_visit")

    # HTTP response codes
    if not zip_code:
        return jsonify({"error": "zip is required"}), 400
        # Bad Request (Client-Side)
        # Should already be validated by frontend

    try:
        results = find_hospitals_by_zip(zip_code, radius)
        # Enrich results with pricing information
        if "places" in results:
            results["places"] = enrich_hospitals_with_pricing(
                results["places"], insurance, procedure
            )
        return jsonify(results), 200  # OK
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400  # Bad Request (Client-Side)
    except Exception:
        return jsonify(
            {"error": "Unable to search hospitals"}
        ), 500  # Internal Server Error (Server-Side)
