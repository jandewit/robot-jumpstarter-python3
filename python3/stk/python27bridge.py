import socket
import sys
import threading
import time
from queue import Queue, Empty

runningReading = True

class Python27Bridge:

	def __init__(self):
		self.eventhandler = None
		self.running = True
		self.worker_threads = list()
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		server_address = ('127.0.0.1', 6686)
		self.sock.connect(server_address) 
		self.sock.settimeout(1)

		# aMessages = []
		self.a_messages = Queue()
		self.t = threading.Thread(target=self.readMessages, args=(self.sock, self.a_messages))
		self.t.start()

	    # Register this module with the ConnectionManager
		self.sendMessage("python27:register")
		# self.sendMessage(self.sock, "python27:self.s.ALTextToSpeech.say(\"Yay over socket!\")")

		threading.Thread(target=self.poll_messages, daemon=True).start()


	def set_eventhandler(self, handler):
		self.eventhandler = handler

	def poll_messages(self):
		# Repeatedly look for new messages and handle them
		try:
			while self.running:
				try:
					str_message = self.a_messages.get_nowait()
					# for str_message in a_messages:
					if str_message != "":
						# print("Message received: " + str_message)
						fields = str_message.split(":")
						# sender, method, params = fields[:3]
						if (fields[1] == 'event'):
						#logging.info("received message %s from %s" % (method, str(sender)))
							wt = threading.Thread(target=self._spawn_thread, args=(fields[2], fields[3]))
							self.worker_threads.append(wt)
							wt.start()
					self.a_messages.task_done()
				except Empty:
					pass
				# del a_messages[:]
				time.sleep(0.1)

			self.cleanup()

		except KeyboardInterrupt:
			#print "Keyboard interrupt"
			self.cleanup()

	def _spawn_thread(self, method, params):
		self.eventhandler.trigger_callback(method, params)
		self._thread_complete_callback(threading.currentThread())

	def _thread_complete_callback(self, thread_ref):
		#print "Thread completed, removing: " + str(thread_ref)
		self.worker_threads.remove(thread_ref)

	def cleanup(self):
		global runningReading
		self.sendMessage("exit")

		# Clean up all worker threads that may be left running
		for wt in self.worker_threads:
			# print("Worker thread found, cleaning:")
			# print(wt)
			wt.join()

		runningReading = False
		self.t.join()
		self.sock.close()

	def sendMessage(self, strMessage):
		#send the message in parameter
		# print("Sending message: " + strMessage)
		self.sock.sendall((strMessage + "#").encode())
		time.sleep(0.1)

	def readMessages(self, _socket, a_messages):
		"""
            This function receives all messages send over the socket connection.

            :param _socket: The TCP Socket.
            :param a_messages: A list where all messages have to be stored.
        """
		tmp_messages = []
		while runningReading:
			try:
				str_receive = _socket.recv(1024).decode()
				if "#" in str_receive:
					str_receive = str_receive.split("#")
					if len(str_receive) > 1:
						tmp_messages += str_receive[0]
						a_messages.put("".join(tmp_messages)) if len(tmp_messages) > 1 else a_messages.put(tmp_messages[0])

						for r in str_receive[1:-1]:
							a_messages.put(r)

					#tmp_messages += str_receive[:-1]
					#a_messages.put("".join(tmp_messages)) if len(tmp_messages) > 1 else a_messages.put(tmp_messages[0])
					#logging.info("Current message # on stack: %s" % a_messages.qsize())
					tmp_messages = [str_receive[-1]]
				else:
					tmp_messages.append(str_receive)

				#time.sleep(0.3)
			except:
				pass
				#logging.debug("error on socket: " + str(e))