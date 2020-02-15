from setuptools import setup
import os
import sys

PKGS = ['qi']
FRAMEWORKS = []
f = open("osx/naoqi.txt", "r")
p = f.read()
f.close()

for f in os.listdir(p):
    fullPath = os.path.join(p, f)
    if os.path.isfile(fullPath) and fullPath.endswith('.dylib'):
        FRAMEWORKS.append(fullPath)

print FRAMEWORKS

OPTIONS = {
    'argv_emulation': True,
    'emulate_shell_environment': True,
    'site_packages': True,
    'includes': PKGS,
    'frameworks': FRAMEWORKS
}

setup(
  app=['naoqiconnection.py'],
  options={'py2app': OPTIONS},
  setup_requires=['py2app'],
)
