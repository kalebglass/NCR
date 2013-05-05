import gtk
import webkit
import os
from threading import Thread
import Queue
import socket

filePath = os.path.dirname(os.path.abspath(__file__))

print filePath

guiPath = "file://"  + filePath + "/gui.html"



#define variables for program execution

connectionThread = Thread()

sendQueue = Queue.Queue()

killConnection = False


def startConnection(ipAddress):
	sendQueue.queue.clear()
	ncrSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ncrSocket.connect((ipAddress, 5050))

	while not killConnection:
		if not sendQueue.empty():
			ncrSocket.send(sendQueue.get())


def connect(ipAddress):
	print ipAddress
	connectionThread= Thread(target=startConnection, args=(ipAddress,))
	connectionThread.start()


def sendMessage(message):
	
	sendQueue.put(message)




class Base:


	def executeCode(self, widget, frame, title):


		if title != 'null':
		 	code = title 
		 	print title
		 	exec code



	def __init__(self):

		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.show()
		self.window.resize(1300,800)
		self.browser = webkit.WebView()
		
		self.go = gtk.Button("Go")
		
		self.browser.open(guiPath)
		self.box = gtk.VBox(homogeneous=False, spacing=0)

		self.scroller = gtk.ScrolledWindow()

		self.scroller.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

		self.scroller.add(self.box)

		self.window.add(self.scroller)

		self.browser.connect('title-changed', self.executeCode)

		self.box.pack_start(self.browser, expand=True, fill=True, padding=0)

		self.window.show_all()

		
		

	def main(self):
		gtk.main()

	
def printWorks(sender):
	print 'It Works'
	



base = Base()

base.main()
