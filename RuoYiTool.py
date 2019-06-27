import os
import json
# 该工具用来自动生成RuoYi的页面，
# 使用方法是确保输入地址为预设的模板，
# 输出地址便是所设置的地址，
# 将其覆盖原有的文件夹便可以实现功能。

print("this is " + __name__ )

# 模板地址
inPath = "RuoYiTemplates"
# 文件地址
outPath = "RuoYi"
# 配置文件
configPath = "Config"
# 对象配置
domainConfig = "main.cfg"
fp = open(configPath + "\\" + domainConfig, "r", encoding = "utf-8")
text = fp.read()
fp.close()
cfg = json.loads(text)
# 对象属性
dateDict = cfg["domain"]
# 对象名称
obj = cfg["name"]
Obj = chr(ord(obj[0]) - ord('a') + ord('A')) + obj[1:]
# 数据库表名称
sheet = cfg["sheet"]
chinese = cfg["chinese"]
l = len(inPath)
for root, dirs, files in os.walk(inPath, topdown = False):
    outdir = root[l:].replace("{object}", obj)
    outdir = outdir.replace("{Object}", Obj)
    if os.path.exists(outPath + "\\" + outdir) == False:
        os.makedirs(outPath + "\\" + outdir)
    for f in files:
        fp = open(root + "\\" + f, "r", encoding = "utf-8")
        f = f.replace("{object}", obj)
        f = f.replace("{Object}", Obj)
        if len(root[l:]) == 0:
            fpout = open(outPath + "\\" + f, "w+", encoding = "utf-8")
        else:
            fpout = open(outPath + outdir + "\\" + f, "w", encoding = "utf-8")
        text = fp.read()
        text = text.replace("{object}", obj)
        text = text.replace("{Object}", Obj)
        text = text.replace("{chinese}", chinese)
        fpout.write(text)
        fpout.close()
        fp.close()
import RuoYiDomainTool
import RuoYIMainHTMLTool
import RuoYiMapperTool
