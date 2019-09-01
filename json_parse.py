import json
import re
import os
import wget

owd = os.getcwd()

with open("data.json", "r") as read_file:
    data = json.load(read_file)

requests = data["log"]["entries"]
hosturl = data["log"]["pages"][0]["title"]

hosturl_parsed = re.search("www.*.com", hosturl)[0]

for entry in requests:

    url = entry["request"]["url"]
    x = re.search(hosturl, url)

    if x is not None:

        directory = url.split(hosturl)[1].split('/')
        print(url)
        if len(directory) > 1:
            url_length = len(directory)
            file_name = directory[-1]
            directory.pop()
            #directory.pop(0)
            new_directory = "/".join(directory)
            # Create directory
            print(new_directory) 
           
            try:
                # Create target Directory
                os.makedirs(new_directory)
                print("Directory ", new_directory,  " Created ")

            except FileExistsError:
                print("Directory ", new_directory,  " already exists")

            os.chdir(new_directory)
            os.system("wget " + url)
            os.chdir(owd)
