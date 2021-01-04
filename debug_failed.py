import argparse
import os
import requests
import urllib.parse
from utils import *
import json
import pdb

def parse_args():
    args=argparse.ArgumentParser(description="Download raw Actigraph gt3x files from CentrePoint")
    args.add_argument("-baseUrl",default="https://studyadmin-api.actigraphcorp.com")
    args.add_argument("-apiAccessKey")
    args.add_argument("-apiSecretKey")
    args.add_argument("-failed",nargs="+") 
    return args.parse_args() 

def main():
    args=parse_args()
    for failed in args.failed:
        
        #get metadata for studies the user has access to 
        resource_uri_file="v1/datafiles/"+failed+"/DownloadUrl"
        headers_file=generate_headers(args,'GET',resource_uri_file)
        file_metadata=requests.get('/'.join([args.baseUrl,resource_uri_file]),headers=headers_file)
        pdb.set_trace()
            
if __name__=="__main__":
    main()
    
