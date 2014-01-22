prefix = '00-00-00-00'
output = '['
for i in range(21,25):
  for j in range(256):
    output = output + ('{"model": "MACLibrary.address", "fields": {"mac": "' + prefix + '-%02X-%02X"}},' % (i,j))
output = output[:-1] + ']'
print output
