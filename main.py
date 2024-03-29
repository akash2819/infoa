#!/bin/env python3
import os, sys
sys.path.append(os.getcwd()+"/.lib/")
import argparse
from lib import api_data as api


ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", required=True, help="username of account to scan")
ap.add_argument("-p", "--post", action="store_true", help="image info of user uploads")
args = vars(ap.parse_args())
	
os.system("clear")

if args['user']:
	api.user_info(usrname=args["user"])

if args['post']:
	api.post_info()
