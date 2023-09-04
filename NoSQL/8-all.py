#!/usr/bin/env python3
"""
lists all documents in a collection
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    """
    document_list = []
    for document in mongo_collection.find():
        document_list.append(document)
    return document_list
