# -*- coding: UTF-8 -*-
import requests
import unit
vultr_url = "https://api.vultr.com/v1/snapshot"

# curl -H 'API-Key: YOURKEY' https://api.vultr.com/v1/snapshot/create --data 'SUBID=1312965'
vultr_url_create = vultr_url + "/create"

un = unit.UnitExt()


def fun_create(subid):
    return un.vultrPostReqeust(vultr_url_create, None, {"SUBID": subid})


# curl -H 'API-Key: YOURKEY' https://api.vultr.com/v1/snapshot/create --data 'SUBID=1312965'
vultr_snapshot_list = vultr_url + "/list"


def fun_list():
    return un.vultrGetReqeust(vultr_snapshot_list)
