# -*- coding: UTF-8 -*-
import requests
import vultr.api_url
import vultr.snapshot
import vultr.server
import argparse
import unit
import vultroper

methods = [""]

allMethod = []


def main(args):
    res1 = list(filter(lambda x: x.displayname == args.method, allMethod))[0]
    el = eval(res1.pyname+"."+res1.funname)
    parastr = args.mparams

    if args.mhelp:
        print("======参数说明======")
        print(el.__annotations__)
        print("====================")
    else:
        print("exeute method " + res1.displayname)
        if parastr:
            paras = parastr.split(',')
            kwargs = {}
            print(paras)
            print(el(*paras, **kwargs))
        else:
            print(el())


if __name__ == '__main__':
    allMethod = vultr.server.initMethod()
    allMethod = vultroper.initMethod()
    for a in allMethod:
        methods.append(a.displayname)

    parser = argparse.ArgumentParser()

    parser.add_argument("--method", required=True,
                        choices=methods, help="需要执行的函数")
    parser.add_argument(
        "--mparams", help="函数参数 value1,value2...")
    parser.add_argument(
        "--mhelp", help="函数帮助", action="store_true")

    args = parser.parse_args()

    main(args)
