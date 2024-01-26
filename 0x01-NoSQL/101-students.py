#!/usr/bin/env python3
"""students aggregate"""


def top_students(mongo_collection):
    """Aggregate student"""
    return mongo_collection.aggregate([
        {
            "$project": {
                "averageScore": {
                    "$avg": "$topics.score"
                },
                "topics": 1,
                "name": 1
            }
        },
        {
            "$sort": {
                "averageScore": 1
            }
        }
    ])
