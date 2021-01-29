#!/usr/bin/env python3

import os, json

print('Content-type:application/json')
print()
print(json.dumps(dict(os.environ), indent=2))

