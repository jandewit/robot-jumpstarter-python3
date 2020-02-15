# robot-jumpstarter-python3
Creates a bridge between python 2.7 (needed for NAOqi) and python 3, so that you won't need to install all of python 2.7 and the NAOqi SDK to talk to the robot.

Based heavily on the [robot-jumpstarter](https://github.com/pepperhacking/robot-jumpstarter) project by SoftBank Robotics.

## Getting started ##
1. Check out the repository
2. (Optional, but why else would you use this): convert the python27 part to executable files so that you won't need to have python 2.7 installed, e.g. using py2exe for Windows or py2app for Mac. See below for more detailed instructions. **Note: you still need one machine that has python 2.7 with NAOqi installed, I'm looking into whether I can provide prebuilt versions.**
3. Start the 2.7 script or the newly created executable file (e.g. naoqiconnection.exe) and pass the command-line argument --qi-url=[ip address] to connect to your robot (or simulator)
4. Start your python 3 code and call upon the robot's features as you normally would using the robot-jumpstarter. Also see a small example included in the python3\main.py file

## [Windows] Getting py2exe to work ##
First install py2exe from the [website]().

Then build the app with:
`python setup.py py2exe`

This should give you an executable file in the **dist** directory.

## [OSX] Getting py2app to work ##
Install py2app using:
`pip install --user --ignore-installed py2app`

Download the NaoQI Python SDK and make sure your PYTHONPATH and DYLD_LIBRARY_PATH are set (see [here](http://doc.aldebaran.com/2-5/dev/python/install_guide.html))

Then build the app with:
`sudo python setup_osx.py [PATH_TO_NAOQI_LIB]`

And replace [PATH_TO_NAOQI_LIB] with the path to the lib directory of the NaoQI SDK. For example, my [PATH_TO_NAOQI_LIB] would be /Users/jandewit/naoqi/lib

Finally, there should be a command to launch the app already in your **dist** directory.

## Disclaimer ##
This software has not been thoroughly tested yet, and is provided "as is". Your contributions are greatly appreciated!
