# VultrApi
VultrApi 工具
vulter地址  https://www.vultr.com  
vulterApi地址  https://www.vultr.com/api

## 使用步骤
- 申请vultr 并创建 vps 配置 
- 创建 sanpshot 配置default_snapshotid
- 启用 vulter api 配置 apikey
- 运行 vultrapi

## 命令帮助
- 通过快照快速创建 server   
*需要配置 apikey/default_dcid/default_vpsplanid/default_snapshotid
~~~
--method oper_creatandstart
~~~

- 删除上次创建的 server   
*根据配置 temp_creatseverid 进行删除  
*每次server创建成功后 temp_creatseverid 会自动更新  
*也可追加 [serverid] 参数指定serer删除
~~~
--method oper_destroylastcreate -mparams [serverid] 
~~~

## user_config.json 文件说明
~~~ 
{
    "apikey": "K6EYWS1QLWO1VKSUX4QU4Z1FAYJZGV2BIVLQ",
    "default_dcid": "5",
    "default_vpsplanid": "201",
    "default_snapshotid": "",
    "temp_creatseverid": "53423711",
    "temp_serverip": "33.333.333.33",
    "printlog": true
}
~~~ 
- apikey：
- default_dcid
- default_vpsplanid
- default_snapshotid  
    https://my.vultr.com/snapshots/ Snapshot ID
- temp_creatseverid
- temp_serverip
- printlog