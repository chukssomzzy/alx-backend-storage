#!/usr/bin/env python3
"""web main"""

import redis


get_page = __import__("web").get_page

url = "http://slowwly.robertomurray.co.uk"
print(get_page(url))

r = redis.Redis()
k = 'count:{}'.format(url)

print(r.get(k))
