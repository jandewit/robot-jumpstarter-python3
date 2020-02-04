import time

class EventHelper(object):

    def __init__(self, bridge):
    	self.bridge = bridge
    	self.bridge.set_eventhandler(self)
    	self.callbacks = dict()
    	self.is_waiting = False


    def connect(self, event, callback):
    	if not event in self.callbacks:
    		self.callbacks[event] = list()

    	self.callbacks[event].append(callback)

    	self.bridge.sendMessage("python27:self.events.connect(\"" + event + "\", self." + event.replace('/','_') + ")")

    def disconnect(self, event):
    	if event in self.callbacks:
    		self.callbacks[event] = list()

    	self.bridge.sendMessage("python27:self.events.disconnect(\"" + event + "\")")

    def wait_for(self, event):
    	self.is_waiting = True

    	self.bridge.sendMessage("python27:self.events.connect(\"" + event + "\", self." + event.replace('/','_') + ")")

    	while self.is_waiting:
    		time.sleep(0.05)

    	self.bridge.sendMessage("python27:self.events.disconnect(\"" + event + "\")")


    def trigger_callback(self, event, params):
    	if self.is_waiting:
    		self.is_waiting = False

    	else:
	    	for c in self.callbacks[event.replace('_', '/')]:
	    		c(params)