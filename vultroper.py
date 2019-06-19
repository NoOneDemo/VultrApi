# -*- coding: UTF-8 -*-
import requests
import vultr.api_url
import vultr.snapshot
import vultr.server
import argparse
import unit
import json
import time


def initMethod():
    vurltrmethod = vultr.server.initMethod()
    vurltrmethod.append(unit.Vurltrmethod(
        "oper_creatbysnapshot", "vultroper", "oper_creatandstart"))
    vurltrmethod.append(unit.Vurltrmethod(
        "oper_destroylastcreate", "vultroper", "oper_destroylastcreate"))
    vurltrmethod.append(unit.Vurltrmethod(
        "oper_checkserverstatus", "vultroper", "oper_checkserverstatus"))
    return vurltrmethod


configs = unit.load_config()


def oper_creatandstart(u_dcid=None, u_vpsplanid=None, u_snapshotid=None):
    dicd = u_dcid
    if not u_dcid:
        dicd = configs['default_dcid']
    vpsplanid = u_vpsplanid
    if not u_vpsplanid:
        vpsplanid = configs['default_vpsplanid']
    snapshotid = u_snapshotid
    if not u_snapshotid:
        snapshotid = configs['default_snapshotid']

    print('dicd:{} vpsid:{} snapshotid:{}'.format(dicd, vpsplanid, snapshotid))
    #server_result = '{\"SUBID\":\"26461531\"}'
    server_result = vultr.server.fun_createbyshapshot(u_dcid=dicd,
                                                      u_vpsplanid=vpsplanid,
                                                      _snapshotid=snapshotid)
    creakeys = json.loads(server_result)

    if 'SUBID' not in creakeys.keys():
        print('create error :'+str(server_result))
        return

    serverid = creakeys['SUBID']
    print('creat success id:'+serverid)
    unit.set_config('temp_creatseverid', serverid)
    statsok = False
    maxcnt = 60*5  # 最大查询次数
    while((statsok == False) and (maxcnt > 0)):
        server_status = oper_checkserverstatus(serverid)
        print(str(maxcnt)+'-->check newserver power_status:{},server_state:{},status:{}'.format(
            server_status['power_status'],
            server_status['server_state'],
            server_status['status'],
        ))
        statsok = (
            server_status['power_status'] == 'running' and
            server_status['server_state'] == "ok" and
            server_status['status'] == 'active')
        time.sleep(1)
        maxcnt = maxcnt-1
    if maxcnt <= 0:
        print('exceed time limitation. exit.')
    else:
        print('new server[{}] start success'.format(serverid))
        unit.set_config('temp_serverip', server_status['main_ip'])
        print('new ip {}'.format(server_status['main_ip']))


def oper_checkserverstatus(u_serverid=None):
    serverid = u_serverid
    if not u_serverid:
        serverid = configs['temp_creatseverid']

    server_list = vultr.server.fun_list()
    dic = json.loads(server_list)
    return dic[serverid]


def oper_destroylastcreate():
    if 'temp_creatseverid' not in configs.keys():
        print('destroy error  user_config.json ->temp_creatseverid null')
        return

    serverid = configs['temp_creatseverid']
    vultr.server.fun_destroy(serverid)
    print('destory server [{}]'.format(serverid))
