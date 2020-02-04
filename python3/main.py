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

		# Choregraphe bezier export in Python.
		names = list()
		times = list()
		keys = list()

		names.append("HeadPitch")
		times.append([0.04, 2.44, 4.72])
		keys.append([[-0.0134902, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.0134902, [3, -0.8, 0], [3, 0.76, 0]], [-0.0134902, [3, -0.76, 0], [3, 0, 0]]])

		names.append("HeadYaw")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.110904, [3, -0.0133333, 0], [3, 0.8, 0]], [0.110904, [3, -0.8, 0], [3, 0.76, 0]], [0.110904, [3, -0.76, 0], [3, 0, 0]]])

		names.append("LAnklePitch")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.09, [3, -0.0133333, 0], [3, 0.8, 0]], [0.09, [3, -0.8, 0], [3, 0.76, 0]], [0.09, [3, -0.76, 0], [3, 0, 0]]])

		names.append("LAnkleRoll")
		times.append([0.04, 2.44, 4.72])
		keys.append([[-0.13, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.13, [3, -0.8, 0], [3, 0.76, 0]], [-0.13, [3, -0.76, 0], [3, 0, 0]]])

		names.append("LElbowRoll")
		times.append([0.04, 2.44, 4.72])
		keys.append([[-0.410388, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.410388, [3, -0.8, 0], [3, 0.76, 0]], [-0.410388, [3, -0.76, 0], [3, 0, 0]]])

		names.append("LElbowYaw")
		times.append([0.04, 2.44, 4.72])
		keys.append([[-1.1937, [3, -0.0133333, 0], [3, 0.8, 0]], [-1.1937, [3, -0.8, 0], [3, 0.76, 0]], [-1.1937, [3, -0.76, 0], [3, 0, 0]]])

		names.append("LHand")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.3, [3, -0.0133333, 0], [3, 0.8, 0]], [0.3, [3, -0.8, 0], [3, 0.76, 0]], [0.3, [3, -0.76, 0], [3, 0, 0]]])

		names.append("LHipPitch")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.13, [3, -0.0133333, 0], [3, 0.8, 0]], [0.13, [3, -0.8, 0], [3, 0.76, 0]], [0.13, [3, -0.76, 0], [3, 0, 0]]])

		names.append("LHipRoll")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.1, [3, -0.0133333, 0], [3, 0.8, 0]], [0.1, [3, -0.8, 0], [3, 0.76, 0]], [0.1, [3, -0.76, 0], [3, 0, 0]]])

		names.append("LHipYawPitch")
		times.append([0.04, 2.44, 4.72])
		keys.append([[-0.17, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.17, [3, -0.8, 0], [3, 0.76, 0]], [-0.17, [3, -0.76, 0], [3, 0, 0]]])

		names.append("LKneePitch")
		times.append([0.04, 2.44, 4.72])
		keys.append([[-0.09, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.09, [3, -0.8, 0], [3, 0.76, 0]], [-0.09, [3, -0.76, 0], [3, 0, 0]]])

		names.append("LShoulderPitch")
		times.append([0.04, 2.44, 4.72])
		keys.append([[1.47236, [3, -0.0133333, 0], [3, 0.8, 0]], [1.47236, [3, -0.8, 0], [3, 0.76, 0]], [1.47236, [3, -0.76, 0], [3, 0, 0]]])

		names.append("LShoulderRoll")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.185419, [3, -0.0133333, 0], [3, 0.8, 0]], [0.185419, [3, -0.8, 0], [3, 0.76, 0]], [0.185419, [3, -0.76, 0], [3, 0, 0]]])

		names.append("LWristYaw")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.1, [3, -0.0133333, 0], [3, 0.8, 0]], [0.1, [3, -0.8, 0], [3, 0.76, 0]], [0.1, [3, -0.76, 0], [3, 0, 0]]])

		names.append("RAnklePitch")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.09, [3, -0.0133333, 0], [3, 0.8, 0]], [0.09, [3, -0.8, 0], [3, 0.76, 0]], [0.09, [3, -0.76, 0], [3, 0, 0]]])

		names.append("RAnkleRoll")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.13, [3, -0.0133333, 0], [3, 0.8, 0]], [0.13, [3, -0.8, 0], [3, 0.76, 0]], [0.13, [3, -0.76, 0], [3, 0, 0]]])

		names.append("RElbowRoll")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.410388, [3, -0.0133333, 0], [3, 0.8, 0]], [0.39831, [3, -0.8, 0.0062628], [3, 0.76, -0.00594966]], [0.37375, [3, -0.76, 0], [3, 0, 0]]])

		names.append("RElbowYaw")
		times.append([0.04, 2.44, 4.72])
		keys.append([[1.1937, [3, -0.0133333, 0], [3, 0.8, 0]], [1.17088, [3, -0.8, 0], [3, 0.76, 0]], [1.19705, [3, -0.76, 0], [3, 0, 0]]])

		names.append("RHand")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.3, [3, -0.0133333, 0], [3, 0.8, 0]], [0.3, [3, -0.8, 0], [3, 0.76, 0]], [0.3, [3, -0.76, 0], [3, 0, 0]]])

		names.append("RHipPitch")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.13, [3, -0.0133333, 0], [3, 0.8, 0]], [0.13, [3, -0.8, 0], [3, 0.76, 0]], [0.13, [3, -0.76, 0], [3, 0, 0]]])

		names.append("RHipRoll")
		times.append([0.04, 2.44, 4.72])
		keys.append([[-0.1, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.1, [3, -0.8, 0], [3, 0.76, 0]], [-0.1, [3, -0.76, 0], [3, 0, 0]]])

		names.append("RHipYawPitch")
		times.append([0.04, 2.44, 4.72])
		keys.append([[-0.17, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.17, [3, -0.8, 0], [3, 0.76, 0]], [-0.17, [3, -0.76, 0], [3, 0, 0]]])

		names.append("RKneePitch")
		times.append([0.04, 2.44, 4.72])
		keys.append([[-0.09, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.09, [3, -0.8, 0], [3, 0.76, 0]], [-0.09, [3, -0.76, 0], [3, 0, 0]]])

		names.append("RShoulderPitch")
		times.append([0.04, 2.44, 4.72])
		keys.append([[1.47236, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.9518, [3, -0.8, 0], [3, 0.76, 0]], [2.08567, [3, -0.76, 0], [3, 0, 0]]])

		names.append("RShoulderRoll")
		times.append([0.04, 2.44, 4.72])
		keys.append([[-0.185419, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.122768, [3, -0.8, 0], [3, 0.76, 0]], [-0.189514, [3, -0.76, 0], [3, 0, 0]]])

		names.append("RWristYaw")
		times.append([0.04, 2.44, 4.72])
		keys.append([[0.1, [3, -0.0133333, 0], [3, 0.8, 0]], [0.1, [3, -0.8, 0], [3, 0.76, 0]], [0.1, [3, -0.76, 0], [3, 0, 0]]])

		self.s.ALMotion.angleInterpolationBezier(names, times, keys)


	def animated_speech_end(self, args):
		print("Animated speech ended..")

		if args:
			print(args)

		self.events.disconnect("ALAnimatedSpeech/EndOfAnimatedSpeech")
		self.s.ALAnimatedSpeech.say("This is another test!")



if __name__ == "__main__":
    Python3NaoExample()
