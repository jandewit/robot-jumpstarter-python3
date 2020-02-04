# robot-jumpstarter-python3
Creates a bridge between python 2.7 (needed for NaoQi) and python 3, so that you won't need to install all of python 2.7 and the NaoQi SDK to talk to the robot.

Based heavily on the [robot-jumpstarter](https://github.com/pepperhacking/robot-jumpstarter) project by SoftBank Robotics.

## Getting started ##
1. Check out the repository
2. (Optional, but why else would you use this): convert the python27 part to executable files so that you won't need to have python 2.7 installed, e.g. using py2exe for Windows or py2app for Mac (untested)
3. Start the newly created executable file and pass the command-line argument --qi-url=[ip address] to connect to your robot (or simulator)
4. Start your python 3 code and call upon the robot's features as you normally would using the robot-jumpstarter. Also see a small example included in the python3\main.py file

## Disclaimer ##
This software has not been thoroughly tested yet, and is provided "as is". Your contributions are greatly appreciated!