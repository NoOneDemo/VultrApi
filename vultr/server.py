# -*- coding: UTF-8 -*-
import requests
import unit
import user_config

server_url = "https://api.vultr.com"
server_url_create = server_url + "/v1/server/create"
server_url_destroy = server_url + "/v1/server/destroy"
server_url_list = server_url + "/v1/server/list"
server_url_app_change_list = server_url + "/v1/server/app_change_list"
server_url_halt = server_url + "/v1/server/halt"
server_url_reboot = server_url + "/v1/server/reboot"


def initMethod():
    vurltrmethod = [unit.Vurltrmethod(
        "server_list", "vultr.server", "fun_list"),
        unit.Vurltrmethod(
        "server_create", "vultr.server", "fun_create"),
        unit.Vurltrmethod(
        "server_createbyshapshot", "vultr.server", "fun_createbyshapshot"),
        unit.Vurltrmethod(
        "server_destroy", "vultr.server", "fun_destroy"),
        unit.Vurltrmethod(
        "server_restart", "vultr.server", "fun_restart"),
        unit.Vurltrmethod(
        "server_stop", "vultr.server", "fun_stop")]
    return vurltrmethod


def fun_create(
        u_dcid: "机房地区id" = int,
        u_vpsplanid: "VPS型号代码" = int,
        u_osid: "操作系统代码" = int):
    return unit.vultrPostReqeust(
        server_url_create,
        None,
        {"DCID": u_dcid, "VPSPLANID": u_vpsplanid, "OSID": u_osid})


def fun_createbyshapshot(
        u_dcid: "机房地区id" = str,
        u_vpsplanid: "VPS型号代码" = str,
        _snapshotid: "快照编码" = str):
    return unit.vultrPostReqeust(
        server_url_create,
        "",
        {"DCID": u_dcid, "VPSPLANID": u_vpsplanid, "OSID": 164, "SNAPSHOTID": _snapshotid})


def fun_destroy(u_subid: "服务器id" = str):
    return unit.vultrPostReqeust(
        server_url_destroy,
        "",
        {"SUBID": u_subid})


def fun_list():
    return unit.vultrGetReqeust(server_url_list)


def fun_app_change_list(u_subid: "服务器id" = str):
    return unit.vultrGetReqeust(server_url_app_change_list, {"SUBID": u_subid})


def fun_stop(u_subid: "服务器id"):
    return unit.vultrPostReqeust(
        server_url_halt,
        "",
        {"SUBID": u_subid})

def fun_restart(u_subid: "服务器id"):
    return unit.vultrPostReqeust(
        server_url_reboot,
        "",
        {"SUBID": u_subid})