import urllib, json, yaml, sys
url = "http://demo8427496.mockable.io/laltest"
response = urllib.urlopen(url)
data = yaml.safe_dump(json.loads(response.read()))
f = open('vars.yaml', 'w')
print >> f, data
f.close()
