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


def normalize_list(docs):
    return [normalize_doc(doc) for doc in docs]
