import stk.python27bridge
import stk.events
import stk.services

class Python3NaoExample:
	def __init__(self):
		self.python27bridge = stk.python27bridge.Python27Bridge()
		self.events = stk.events.EventHelper(self.python27bridge)
		self.s = stk.services.ServiceCache(self.python27bridge)
		# self.events.connect("ALAnimatedSpeech/EndOfAnimatedSpeech", self.animated_speech_end)
		self.s.ALAnimatedSpeech.say("This is a test!")
		self.events.wait_for("Jantest/Test")
		self.s.ALAnimatedSpeech.say("And this won't trigger until after a JanTest/Test event is fired (e.g. from Choregraphe)")


	def animated_speech_end(self, args):
		print("Animated speech ended..")

		if args:
			print(args)

		self.events.disconnect("ALAnimatedSpeech/EndOfAnimatedSpeech")
		self.s.ALAnimatedSpeech.say("This is another test!")



if __name__ == "__main__":
    Python3NaoExample()
