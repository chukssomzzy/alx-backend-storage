#!/usr/bin/env python3
"""List document in collection"""


def list_all(mongo_collection):
    """List All document"""
    return [doc for doc in mongo_collection.find()]
