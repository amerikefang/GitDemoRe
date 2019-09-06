import urllib.request
import urllib.parse

url = 'http://www.google.com'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

request = urllib.request.Request(url, headers=header)
response = urllib.request.urlopen(request).read()

fhandle = open("./2_mockbrowserbaidu.html", "wb")
fhandle.write(response)
fhandle.close()
