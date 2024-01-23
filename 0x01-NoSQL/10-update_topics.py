#!/usr/bin/env python3
"""Update Topic"""


def update_topics(mongo_collection, name, topics) -> None:
    """Update collection topic by name"""
    mongo_collection.update({"name": name},
                            {"$set": {"topics": topics}})
