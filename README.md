# 一键探测存活的邮箱

> 目前只实现了同时探测相同企业的邮箱，若需要探测多个不同后缀的邮箱，请分开运行。
>
> 项目依赖：pip install fire

- 将探测到的目标邮箱输入target.txt中。
- 获取目标企业的smtp邮箱服务器地址。

```
nslookup -type=mx 163.com
```

![image-20220512152502273](https://huihui-1258180155.cos.ap-nanjing.myqcloud.com/image-20220512152502273.png)

> 在真实项目中，建议将所有的 smtp 服务器都试一遍。

- 执行命令：

```
python main.py smtp_server_address port
PS: python main.py 163mx01.mxmail.netease.com 25
```

- 执行结束后，会在本地生成探测为存活的邮箱的文本文件。

![image-20220512160623674](https://huihui-1258180155.cos.ap-nanjing.myqcloud.com/image-20220512160623674.png)

## 其他配置：

- 用户可自定义修改 FROM

```
MAIL FROM:<aaa@aaa.com>
```

**注意：FROM字段最好不要与目标邮箱域名一样，否则可能触发SPF检测，导致请求被SPF协议拦截。若检查了该企业的邮箱未使用SPF的话，则可随意使用FROM**

如：目标邮箱是 aaa@163.com 且存在SPF时，则from字段就不要使用 163.com 后缀的了。

```
检查SPF：
nslookup -type=txt domain
```

![image-20220516105158348](https://huihui-1258180155.cos.ap-nanjing.myqcloud.com/image-20220516105158348.png)

- 修改判断逻辑

通常情况下，若邮箱存在，则  RCPT TO: 字段的响应状态码为 250 ，但是有些特殊情况下，如SMTP配置特殊，导致响应状态码没有250的，则可以根据实际情况修改源码。

- EHLO

自己可以自定义跟EHLO向SMTP服务器表面身份。
