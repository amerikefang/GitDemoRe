import urllib.request

file = urllib.request.urlopen('http://www.baidu.com')

data = file.read()  # read all

dataline = file.readline()  # read one line

fhandle = open("./1_savewebpage.html", "wb")  # save web page to local
fhandle.write(data)
fhandle.close()

