#!/usr/bin/env python
prefix = '00-00-00-00'
for i in range(21,25):
  for j in range(256):
    print(prefix + '-%02X-%02X' % (i, j))