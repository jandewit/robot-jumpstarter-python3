from threading import Thread

import SocketServer

class SocketConnection(Thread):
	def __init__(self, name, ip, port, message_received_callback):
		Thread.__init__(self)
		self.server = None
		self.name = name
		self.ip = ip
		self.port = port
		self.message_received_callback = message_received_callback
		self.connected_clients = {}

	def run(self):
		print "starting socket..."
		self.server = ThreadedServer((self.ip, self.port), self._handler_factory(self._handle_request, self.connected_clients))
		self.server.serve_forever()

	def send(self, target, message, origin = ""):
		# print "Sending message..."

		if origin == "":
			origin = self.name

		if target in list(self.connected_clients.keys()):
			self.connected_clients[target].send(origin + ":" + message + "#")

	def _handler_factory(self, callback, connected_clients):
		def createHandler(*args, **keys):
			return TCPRequestHandler(callback, connected_clients, *args, **keys)
		return createHandler

	def _handle_request(self, origin, content):
		# print "Request incoming..."
		# print origin
		# print content
		components = content.split(':')

		if len(components) < 2:
			return

		client_name = components[0]
		if components[1] == 'register':
			print "New client registered: " + client_name
			self.connected_clients[client_name] = origin

		elif client_name in list(self.connected_clients.keys()):
			self.message_received_callback(client_name, content[content.find(':')+1:])

	def stop(self):
		print "stopping socket..."
		self.server.shutdown()

	# def is_client_connected(self):
	# 	return self.num_clients > 0

	def send_message(self, client, message):
		if client in list(self.connected_clients.keys()):
			self.connected_clients[client].send(message)
		else:
			print "Error sending message: " + client + "  not connected." 

class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)

class TCPRequestHandler(SocketServer.BaseRequestHandler):
    """ One instance per connection. """
    def __init__(self, callback, connected_clients, *args, **keys):
        self.callback = callback
        try:
        	SocketServer.BaseRequestHandler.__init__(self, *args, **keys)
        except:
        	for key, val in connected_clients.iteritems():
        		if val == args[0]:
		        	print key + " disconnected"
        			connected_clients.pop(key)
        			break

    def handle(self):
    	# print "client connected!"
		data_str = ""  

		# print self  	

		while True:
			data = self.request.recv(1024).strip()

			split = data.split('#')
			end_token_index = data.find('#')
			if len(split) > 1:
				data_str += split[0]
				# self.message_received_callback("test", self.data_str)
				self.callback(self.request, data_str)
				
				for i in range(1, len(split)-1):
					data_str = split[i]
					self.callback(self.request, data_str)

				data_str = split[len(split)-1]

			elif len(split) == 1 and data.find('#') != -1:
				data_str += data
				self.callback(self.request, data_str)
				data_str = ""

			else:
				data_str += data

	    	# print data
	        #data = Net.recv_from_socket(self.request)
	        # self.callback(data) 
	        # print 'callback done'  
