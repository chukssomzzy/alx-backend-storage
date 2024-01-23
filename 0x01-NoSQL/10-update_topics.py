#!/usr/bin/env python3
"""Update Topic"""


from typing import ParamSpecKwargs


def update_topics(mongo_collection, name, topics) -> None:
    """Update collection topic by name"""
    mongo_collection.update({"name": name},
                            {"$set": {"topics": topics}})


if __name__ == "__main__":
    pass
