# -*- coding: UTF-8 -*-
import requests
import user_config
import vultr.api_url
import vultr.snapshot
import vultr.server
import argparse
import unit

methods = [""]

allMethod = [unit.Vurltrmethod()]


def main(args):
    print("--method {0}".format(args.method))  # 如果命令行中该参数输入的值不在choices列表中，则报错
    obj = __import__(allMethod[1].pyname, None, None, "vultr")
    mtd = getattr(obj, allMethod[1].funname)
    print(mtd())


if __name__ == '__main__':
    allMethod = allMethod+vultr.server.initMethod()
    for a in allMethod:
        methods.append(a.displayname)

    parser = argparse.ArgumentParser(
        usage="it's usage tip.", description="help info.")
    parser.add_argument(
        "--method", choices=methods, required=True, help="the file type")
    args = parser.parse_args()

    main(args)

"""
def main(args):

    obj = __import__(clsname) # import module
    c = getattr(obj,clsname)
    obj = c() # new class
    #print(obj)
    #obj.echo()
    mtd = getattr(obj,method)
    mtd() # call def

    # args.address会报错，因为指定了dest的值
    print("--address {0}".format(args.method))
    print("--flag {0}".format(args.flag))  # 如果命令行中该参数输入的值不在choices列表中，则报错
    print("--port {0}".format(args.port))  # prot的类型为int类型，如果命令行中没有输入该选项则报错
    print("-l {0}".format(args.log))# 如果命令行中输入该参数，则该值为True。因为为短格式"-l"指定了别名"--log"，所以程序中用args.log来访问


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage="it's usage tip.", description="help info.")
    parser.add_argument("--address", default=80,
                        help="the port number.", dest="code_address")
    parser.add_argument(
        "--flag", choices=['.txt', '.jpg', '.xml', '.png'], default=".txt", help="the file type")
    parser.add_argument("--port", type=int, required=True,
                        help="the port number.")
    parser.add_argument("-l", "--log", default=False,
                        action="store_true", help="active log info.")

    args = parser.parse_args()
"""
