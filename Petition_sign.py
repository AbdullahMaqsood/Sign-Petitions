#for Python 3.2
import urllib.request
page = urllib.request.urlopen("http://www.google.com")
print (page.read())