import os
import shutil
import sys
import subprocess

# execfile('osx/setup_py2app.py')
f = open("osx/naoqi.txt", "w")
f.write(sys.argv[1])
f.close()

subprocess.call(['python', 'osx/setup_py2app.py', 'py2app'])
os.system('install_name_tool -add_rpath @executable_path/../Frameworks dist/naoqiconnection.app/Contents/Resources/lib/python2.7/lib-dynload/_qi.so')
shutil.copyfile('osx/run.command', './dist/run.command')
os.system('chmod 755 dist/run.command')
