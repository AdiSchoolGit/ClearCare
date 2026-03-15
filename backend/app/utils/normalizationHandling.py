"""
Normalization of document fields, to change name fields from _id to id
Since MongoDB uses _id as the primary key, but we want to use id as the primary key in our API responses.
Weird BSON to JSON conversion handling
"""


def normalize_doc(doc):
    if not doc:
        return None

    doc["id"] = str(doc.pop("_id"))
    return doc


"""
Usage expected when interacting with DB
Probably going to define some "repositories" folder
which is going to have all the DB interaction logic
"""
