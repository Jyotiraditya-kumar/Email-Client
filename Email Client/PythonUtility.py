import os
import json
import base64


def Decode(data):
    return(base64.urlsafe_b64decode(data))


def save_file(data, name):
    print(name)
    with open(name, "wb") as f:
        f.write(data)


def MakeDirs(path):
    try:
        os.makedirs(path)
    #         print('Making Directory',dire)
    except Exception as e:
        pass
    #         print(e)
