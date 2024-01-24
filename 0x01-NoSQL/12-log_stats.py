#!/usr/bin/env python3
"""Logs """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    nginx = client.logs.nginx

    print(f"{nginx.count()} logs")
    print("Methods:")
    print(f"    method GET: {nginx.count({'method': 'GET'})}")
    print(f"    method POST: {nginx.count({'method': 'POST'})}")
    print(f"    method PUT: {nginx.count({'method': 'PUT'})}")
    print(f"    method PATCH: {nginx.count({'method': 'PATCH'})}")
    print(f"    method DELETE: {nginx.count({'method': 'DELETE'})}")
    print(f"\
          {nginx.count({'method': 'GET'}) + nginx.count({'path': '/status'})}")
