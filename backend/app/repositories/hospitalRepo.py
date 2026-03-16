from app.db import mongo
from app.utils.normalizationHandling import normalize_doc, normalize_list
from bson import ObjectId
from bson.errors import InvalidId

# if using BasedPyRight language servers have issues with bson imports
# will not affect functionality


# Lists all hospitals in DB, will probably remove
def find_all_hospitals():
    hospitals = list(mongo.db.hospitals.find())
    return normalize_list(hospitals)


# Finds a hospital by its ID
# Returns a JSON representation of the hospital
# Since retrieval will return an ObjectId, we convert it to a string before returning
# No checking for invalid inputs yet so any bad output will crash
def find_hospital_by_id(hospital_id: str):
    try:
        hospitalID = ObjectId(hospital_id)
    except InvalidId:
        return None

    hospital = mongo.db.hospitals.find_one({"_id": ObjectId(hospitalID)})
    return normalize_doc(hospital)
