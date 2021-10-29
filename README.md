# FoFaApiServer

# FoFaApiServer可以干什么

你只需要在客户端运行client.py脚本，就可以使用FOFA。

**在使用FOFA的过程中**，**客户端**并不需要配置FOFA会员的邮箱与KEY，**只需要简单的运行脚本，输入查询语句就能查询。**

同时，理论上这个**客户端**可以是**无限多且同时存在的**(FOFA Api查询无限制的情况下)。

这里有心的同学可能会思考一个问题：
  这不就和FOFA网站调用FOFA的API一个道理吗？
    FOFA API为后端，FOFA 网站为前端
  
  是的，同理FOFA网站，这个Client脚本为前端，FOFA API为后端，只不过这里添加了服务器这一中间件来作为会员账号的一个跳板。

# 如何使用

1.你需要拥有一个FOFA会员的账号

2.`ServerSocket.py` **填写FOFA邮箱和KEY**，以及**填写服务器绑定的Socket端口**

3.将` ServerSocket.py `**放在服务器上，用python3运行**(其中可能需要安装requests库 ` pip3 install requests`)

4.`Client.py` 填写服务器IP和服务器绑定的端口即可

5.python3运行Client.py，开始使用

# 免责声明：
本程序仅用于日常编程学习，请使用者遵守《中华人民共和国网络安全法》，开发者与使用者在使用中产生的任何责任均与本作者无关。下载使用即代表使用者同意上述观点。
