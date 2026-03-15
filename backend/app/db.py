from flask_pymongo import PyMongo

# Sets up connection to MongoDB
# Use within fetch based actions within Repositories
mongo = PyMongo()
