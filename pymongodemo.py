# Module used to connect Python with MongoDb
import pymongo

# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define the 'classDB' database in Mongo
db = client.travel_db

# Query all students
# Here, db.students refers to the collection 'classroom '
dests = db.destinations.find()

# Iterate through each student in the collection
for dest in dests:
    print(dest)

# Insert a document into the 'students' collection
db.destinations.insert_one(
    {
        # 'name': 'Ahmed',
        # 'row': 3,
        # 'favorite_python_library': 'Matplotlib',
        # 'hobbies': ['Running', 'Stargazing', 'Reading']
        'continent' : 'Australia',
        'country' : 'Australia',
        'major_cities' : ['blah1', 'blah2']
    }
)

# Update a document
db.classroom.update_one(
    {'name': 'Ahmed'},
    {'$set':
        {'row': 4}
     }
)

# Add an item to a document array
db.classroom.update_one(
    {'name': 'Ahmed'},
    {'$push':
        {'hobbies': 'Listening to country music'}
     }
)

# Delete a field from a document
db.classroom.update_one({'name': 'Ahmed'},
                        {'$unset':
                         {'gavecandy': ""}
                         }
                        )


# Delete a document from a collection
db.classroom.delete_one(
    {'name': 'Ahmed'}
)