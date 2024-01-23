#!/usr/bin/env python3
"""Update Topic"""
from typing import Any, List


def update_topics(mongo_collection: Any, name: str, topics: List[str]) -> None:
    """Update collection topic by name"""
    mongo_collection.update({"name": name},
                            {"$set": {"topics": topics}})
