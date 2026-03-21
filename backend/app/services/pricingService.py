"""Mock pricing service for healthcare cost estimation."""

import hashlib
from typing import Any

# Insurance types with coverage rates
INSURANCE_TYPES = {
    "uninsured": {"label": "Uninsured", "coverage_rate": 0.0},
    "private": {"label": "Private Insurance", "coverage_rate": 0.70},
    "medicare": {"label": "Medicare", "coverage_rate": 0.80},
    "medicaid": {"label": "Medicaid", "coverage_rate": 0.90},
}

# Procedures with price ranges (min, max)
PROCEDURES = {
    "general_visit": {"label": "General Visit", "min": 150, "max": 400},
    "lab_work": {"label": "Lab Work", "min": 100, "max": 500},
    "xray": {"label": "X-Ray", "min": 200, "max": 600},
    "ct_scan": {"label": "CT Scan", "min": 500, "max": 1500},
    "mri": {"label": "MRI", "min": 800, "max": 2500},
    "minor_surgery": {"label": "Minor Surgery", "min": 1500, "max": 5000},
}


def generate_hospital_price(hospital_id: str, procedure: str) -> int:
    """
    Generate a deterministic price for a hospital/procedure combination.
    Uses hash of hospital_id + procedure to ensure same hospital always
    returns same price for same procedure.
    """
    if procedure not in PROCEDURES:
        procedure = "general_visit"

    proc_info = PROCEDURES[procedure]
    price_range = proc_info["max"] - proc_info["min"]

    # Create deterministic hash from hospital_id and procedure
    hash_input = f"{hospital_id}:{procedure}"
    hash_value = int(hashlib.md5(hash_input.encode()).hexdigest(), 16)

    # Map hash to price range
    price_offset = hash_value % (price_range + 1)
    base_price = proc_info["min"] + price_offset

    return base_price


def enrich_hospitals_with_pricing(
    hospitals: list[dict[str, Any]],
    insurance_type: str = "uninsured",
    procedure: str = "general_visit",
) -> list[dict[str, Any]]:
    """
    Add pricing information to hospital results.

    Args:
        hospitals: List of hospital dictionaries from search results
        insurance_type: Type of insurance (uninsured, private, medicare, medicaid)
        procedure: Type of procedure (general_visit, lab_work, xray, ct_scan, mri, minor_surgery)

    Returns:
        List of hospitals with pricing information added
    """
    # Validate inputs with defaults
    if insurance_type not in INSURANCE_TYPES:
        insurance_type = "uninsured"
    if procedure not in PROCEDURES:
        procedure = "general_visit"

    insurance_info = INSURANCE_TYPES[insurance_type]
    procedure_info = PROCEDURES[procedure]

    enriched_hospitals = []
    for hospital in hospitals:
        hospital_id = hospital.get("id", "")
        base_cost = generate_hospital_price(hospital_id, procedure)

        # Calculate insurance coverage and out of pocket
        insurance_coverage = int(base_cost * insurance_info["coverage_rate"])
        out_of_pocket = base_cost - insurance_coverage

        # Add pricing to hospital
        hospital_copy = dict(hospital)
        hospital_copy["pricing"] = {
            "procedure": procedure_info["label"],
            "insurance_type": insurance_info["label"],
            "base_cost": base_cost,
            "insurance_coverage": insurance_coverage,
            "out_of_pocket": out_of_pocket,
            "disclaimer": "Estimated costs for demonstration only. Actual costs may vary.",
        }
        enriched_hospitals.append(hospital_copy)

    return enriched_hospitals
