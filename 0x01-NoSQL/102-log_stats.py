#!/usr/bin/env python3
"""improved logs with aggregate"""

from pymongo import MongoClient


def top_ten(col):
    """get top ten ips in col"""
    res = col.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "appeared": {
                    "$sum": 1
                }
            }
        },
        {
            "$sort": {
                "appeared": -1
            }
        },
        {
            "$limit": 10
        }
    ])
    return res


def main():
    """Start of program execution"""
    client = MongoClient("mongodb://localhost:27017")
    nginx = client.logs.nginx

    print(f"{nginx.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {nginx.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {nginx.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {nginx.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {nginx.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {nginx.count_documents({'method': 'DELETE'})}")
    sum = nginx.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{sum} status check")
    print("IPs:")
    for doc in top_ten(nginx):
        print("\t{}: {}".format(doc["_id"], doc["appeared"]))


if __name__ == "__main__":
    main()
