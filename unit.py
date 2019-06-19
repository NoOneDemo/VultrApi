# -*- coding: UTF-8 -*-
import requests
import json


class Vurltrmethod:
    def __init__(self="", u_displayname="", u_pyname="", u_funname=""):
        self.displayname = u_displayname
        self.pyname = u_pyname
        self.funname = u_funname


def load_config():
    with open("user_config.json", 'r') as f:
        config = json.loads(f.read())
    return config


def set_config(k, v):
    config = load_config()
    config[k] = v
    with open("user_config.json", 'w') as json_file:
        json_file.write(json.dumps(config, indent=4))
    return config


class UnitExt:
    printlog = False
    userkey = ''
    config = load_config()

    def __init__(self):
        self.printlog = self.config['printlog']
        self.userkey = self.config['apikey']

    def fun_printRequestsLog(self, u_url, u_params, u_datas, response):
        if(self.printlog):
            print("request: " + u_url + " --params " +
                  u_params + " --data" + u_datas)
            # print("response: " + response.text)
        return

    def vultrGetReqeust(self, u_url="", u_params=""):
        userhead = {"API-Key": self.userkey}
        response = requests.get(u_url, params=u_params, headers=userhead)
        response.encoding = "utf-8"
        self.fun_printRequestsLog(u_url, str(u_params), "", response)
        return response.text

    def vultrPostReqeust(self, u_url="", u_params="", u_data=""):
        userhead = {"API-Key": self.userkey}
        response = requests.post(u_url, params=u_params,
                                 headers=userhead, data=u_data)
        response.encoding = "utf-8"
        self.fun_printRequestsLog(u_url, str(u_params), str(u_data), response)
        return response.text
