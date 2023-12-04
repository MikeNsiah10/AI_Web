import sys
import os

os.chdir("/home/user123/AI_Web")
sys.path.append("/home/user123/AI_Web")

from app import app

application = app
