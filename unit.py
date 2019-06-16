# -*- coding: UTF-8 -*-
import user_config
import requests

# -*- coding: UTF-8 -*-


class Vurltrmethod:
    def __init__(self="", u_displayname="", u_pyname="", u_funname="", u_funparam=[""]):
        self.displayname = u_displayname
        self.pyname = u_pyname
        self.funname = u_funname
        self.funparam = u_funparam


def fun_printRequestsLog(u_url, u_params, u_datas, response):
    if(user_config.printlog):
        print("request: " + u_url + " --params " +
              u_params + " --data" + u_datas)
        print("response: " + response.text)
    return


def vultrGetReqeust(u_url="", u_params=""):
    userhead = {"API-Key": user_config.userkey}
    response = requests.get(u_url, params=u_params, headers=userhead)
    response.encoding = "utf-8"
    fun_printRequestsLog(u_url, u_params, "", response)
    return response.text


def vultrPostReqeust(u_url="", u_params="", u_data=""):
    userhead = {"API-Key": user_config.userkey}
    response = requests.post(u_url, params=u_params,
                             headers=userhead, data=u_data)
    response.encoding = "utf-8"
    fun_printRequestsLog(u_url, u_params, u_data, response)
    return response.text
