#!/usr/bin/env python3
"""Logs """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    nginx = client.logs.nginx

    print(f"{nginx.count_documents({})} logs")
    print("Methods:")
    print(f"    method GET: {nginx.count_documents({'method': 'GET'})}")
    print(f"    method POST: {nginx.count_documents({'method': 'POST'})}")
    print(f"    method PUT: {nginx.count_documents({'method': 'PUT'})}")
    print(f"    method PATCH: {nginx.count_documents({'method': 'PATCH'})}")
    print(f"    method DELETE: {nginx.count_documents({'method': 'DELETE'})}")
    sum = nginx.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{sum} status check")
