#!/usr/bin/env python3
""" Insert doc to collections"""


def insert_school(mongo_collection, **kwargs):
    """Insert kwargs to mongo_collections"""
    ins = mongo_collection.insert_one(kwargs)
    return ins.inserted_id
