2022.10.10更新
更加简化的自动登录request_scholl.py上线
只需要使用Chrome或者fiddler抓包得到pwd和tag填入即可使用。pwd和tag每次都在变化，但是尝试发现使用同一组pwd和tag似乎没有时间限制。
猜测：pwd做了加密，盐值是tag


1. 电脑有python3环境

2. 两个文件都下载，放同一文件夹，chromedriver看自己chrome版本，可以去官网下符合自己版本的

3. pip install requests

   pip install selenium

4. school.py 在self.username和self.password改用户名和密码

5. 打开cmd，运行python school.py



