#!/usr/bin/env python3
"""Schools by topic"""


def schools_by_topic(mongo_collection, topic):
    """Schools by topic"""
    return [doc for doc in mongo_collection.find({"topics": topic})]
