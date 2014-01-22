from string import upper
output = '['
for i in range(21,25):
  for j in range(256):
    output = output + ('{"model": "MACLibrary.address", "fields": {"mac": "00-1F-11-02-%02X-%02X"}},' % (i,j))
output = output[:-1] + ']'
print output
