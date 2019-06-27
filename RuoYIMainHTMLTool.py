import os
import json
print("this is " + __name__ )

# 模板地址
templatesPath = "Templates"
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
# 模板名称
templateName = "{object}.html"
# 文件名称
fileName = templateName.replace("{object}", obj)
# 输出地址
# outPath = "out"
outPath = "RuoYi\\ruoyi-admin\\src\\main\\resources\\templates\\system\\{object}".replace("{object}", obj)
if os.path.exists(outPath) == False:
    os.makedirs(outPath)
# 输出模板
InputTemplate = "<li>\n{chinese}:<input type=\"text\" name=\"{key}\"/>\n</li>\n"         
TableTemplate = "\tfield : '{key}',\n\ttitle : '{chinese}',\n\tsortable : {sortable}\n"

tableDefine = "\n"
inputDefine = "\n"

for k in dateDict.keys():
    tableDefine += "{\n" + TableTemplate.format(key= k, chinese = dateDict[k]["chinese"], sortable = dateDict[k]["sortable"]) + "},\n"
    inputDefine += InputTemplate.replace("{chinese}", dateDict[k]["chinese"]).replace("{key}", k)
fp = open(templatesPath + "\\" + templateName, "r", encoding = "utf-8")
fpout = open(outPath + "\\"+ fileName, "w", encoding = "utf-8")
print(outPath + "\\"+ fileName)
text = fp.read()
text = text.replace("{tableDefine}", tableDefine)
text = text.replace("{inputDefine}", inputDefine)
text = text.replace("{object}", obj)
fpout.write(text)
fpout.close()
fp.close()
