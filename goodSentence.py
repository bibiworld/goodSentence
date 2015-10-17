#coding:utf8
#get good daily sentenece from http://dipan.kekenet.com/
#for:server of Bibi World
#by:evan69
def getSentence():
	import urllib2,HTMLParser,re

	req = urllib2.Request("http://dipan.kekenet.com/group/1200")
	response = urllib2.urlopen(req)
	data = response.read()
	pattern1 = re.compile(r'<a href="(/thread.*?)"?>')
	theurl = "http://dipan.kekenet.com" + pattern1.search(data).group(1)[:-2]
	urldata = urllib2.urlopen(theurl).read()
	pattern2 = re.compile(r'<font color="#800080">(.*?)</font>')
	pattern3 = re.compile(r'</b></div><div><b>(.*?)</b>')
	return pattern2.search(urldata).group(1),pattern3.search(urldata).group(1)
	
if __name__ == "__main__":
	print getSentence()
