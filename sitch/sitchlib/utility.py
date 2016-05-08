import datetime
import json
import os
import subprocess
import requests


class Utility:
    def __init__():
        return

    @classmethod
    def get_now_string(cls):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return now

    @classmethod
    def get_platform_info(cls):
        lshw = "/usr/bin/lshw -json"
        try:
            raw_response = subprocess.check_output(lshw.split())
            platform_info = json.loads(raw_response.replace('\n', ''))
        except:
            platform_info = {}
        return platform_info

    @classmethod
    def start_component(cls, runcmd):
        try:
            subprocess.Popen(runcmd.split())
        except KeyError as e:
            return False
        return True

    @classmethod
    def create_path_if_nonexistent(cls, path):
        if os.path.exists(path) and os.path.isdir(path):
            return
        elif os.path.exists(os.path.dirname(path)):
            return
        # elif os.path.isfile(path):
        #    os.remove(path)
        os.mkdir(os.path.dirname(path))
        return

    @classmethod
    def create_file_if_nonexistent(cls, path, lfile):
        fullpath = os.path.join(path, lfile)
        if os.path.isfile(fullpath):
            return
        else:
            print "Creating log file: %s" % fullpath
            open(fullpath, 'a').close()
        return

    @classmethod
    def write_file(cls, location, contents):
        with open(location, 'w') as fh:
            fh.write(contents)

    @classmethod
    def get_platform_name(cls):
        lshw = "/usr/bin/lshw -json"
        try:
            raw_response = subprocess.check_output(lshw.split())
            platform_info = json.loads(raw_response.replace('\n', ''))
        except:
            platform_info = {}
        try:
            platform_name = platform_info["product"]
        except:
            platform_name = "Unspecified"
        return platform_name

    @classmethod
    def strip_list(cls, raw_struct):
        """Strips contents from single-item list"""
        if (type(raw_struct) is list and len(raw_struct)) == 1:
            return raw_struct[0]
        else:
            return raw_struct

    @classmethod
    def get_public_ip(cls):
        url = 'https://api.ipify.org/?format=json'
        result = (requests.get(url).json())['ip']
        return result
