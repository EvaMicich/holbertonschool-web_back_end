# NoSQL Project

This project focuses on understanding the basics of NoSQL databases and performing CRUD operations on MongoDB. The project also introduces integrating MongoDB with Python using the PyMongo library.

## Learning Objectives

- Understand the meaning of NoSQL.
- Differentiate between SQL and NoSQL.
- Understand ACID properties.
- Know about document storage.
- Understand various NoSQL types.
- Recognize the benefits of using a NoSQL database.
- Perform basic query operations on a NoSQL database.
- Insert, update, and delete information from a NoSQL database.
- Use MongoDB effectively.

## Requirements

### MongoDB Command File

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2).
- All files should end with a new line.
- The first line of all your files should be a comment: `// my comment`.

### Python Scripts

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10).
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.

## Tasks

1. **List all databases**: Write a script that lists all databases in MongoDB.
2. **Create a database**: Write a script that creates or uses the database `my_db`.
3. **Insert document**: Write a script that inserts a document in the collection `school` with the name "Holberton school".
4. **All documents**: List all documents in the collection `school`.
5. **All matches**: List all documents with `name="Holberton school"` in the collection `school`.
6. **Count**: Display the number of documents in the collection `school`.
7. **Update**: Add a new attribute to a document in the collection `school`.
8. **Delete by match**: Delete all documents with `name="Holberton school"` in the collection `school`.
9. **List all documents in Python**: Write a Python function that lists all documents in a collection.
10. **Insert a document in Python**: Write a Python function that inserts a new document in a collection based on kwargs.

## Setup and Installation

Detailed in the project are steps to install MongoDB 4.2 on Ubuntu 18.04 and how to integrate it with Python using PyMongo.

## Usage

Each script can be run to perform its specific task. Python scripts should be executable and can be run as:

```bash
./script_name.py
