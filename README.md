# 一键探测存活的邮箱

> 目前只实现了同时探测相同企业的邮箱，若需要探测多个不同后缀的邮箱，请分开运行。
>
> 项目依赖：fire

- 将探测到的目标邮箱输入target.txt中。
- 获取目标企业的smtp邮箱服务器地址。

```
nslookup -type=mx 163.com
```

![image-20220512152502273](https://huihui-1258180155.cos.ap-nanjing.myqcloud.com/image-20220512152502273.png)

- 执行命令：

```
python main.py smtp_server_address port
PS: python main.py 163mx01.mxmail.netease.com 25
```

- 执行结束后，会在本地生成探测为存活的邮箱的文本文件。

![image-20220512152753302](https://huihui-1258180155.cos.ap-nanjing.myqcloud.com/image-20220512152753302.png)