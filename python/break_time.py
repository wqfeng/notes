
import time
import webbrowser

for i in range(1, 5):
	time.sleep(1 * 60 * 60)
	print "It's " + time.ctime() + ". It's time to get a break!"
	webbrowser.open("http://v.youku.com/v_show/id_XNDQ0OTA0MzU2.html")
