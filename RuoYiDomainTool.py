import os
import json
print("this is " + __name__ )
# 模板地址
templatesPath = "Templates"
# 配置文件
configPath = "Config"
# 对象配置
domainConfig = "main.cfg"
fp = open(configPath + "\\" + domainConfig, "r")
text = fp.read()
fp.close()
cfg = json.loads(text)
# 对象属性
dateDict = cfg["domain"]
# 对象名称
obj = cfg["name"]
Obj = chr(ord(obj[0]) - ord('a') + ord('A')) + obj[1:]
# 模板名称
templateName = "{Object}.java"
# 文件名称
fileName = templateName.replace("{Object}", Obj)
# 输出地址
outPath = "RuoYi\\ruoyi-system\\src\\main\\java\\com\\ruoyi\\system\\domain"
if os.path.exists(outPath) == False:
    os.makedirs(outPath)
# 输出模板
appendListDefineTemplate = "\n\t\t\t.append(\"{key}\", get{Key}())"
dateDefineTemplate = "\tprivate {type} {key};\n"
getfunctiondefineTemplate_0 = "\tpublic {type} get{Key}()\n"
getfunctiondefineTemplate_1 = "\n\t\treturn {key};\n"
setfunctiondefineTemplate_0 = "\tpublic void set{Key}({type} {key})\n"
setfunctiondefineTemplate_1 = "\n\t\tthis.{key} = {key};\n"

dateDefine = "\n"
functiondefine = "\n"
appendListDefine = ""
for k in dateDict.keys():
    K = chr(ord(k[0]) + ord('A') - ord('a')) + k[1:]
    dateDefine += dateDefineTemplate.format(type = dateDict[k]["type"], key = k)
    functiondefine += getfunctiondefineTemplate_0.format(type = dateDict[k]["type"], Key = K)
    functiondefine += "\t{" + getfunctiondefineTemplate_1.format(type = dateDict[k]["type"], key = k) + "\t}\n"
    functiondefine += setfunctiondefineTemplate_0.format(type = dateDict[k]["type"], Key = K, key = k)
    functiondefine += "\t{" + setfunctiondefineTemplate_1.format(type = dateDict[k]["type"], key = k) + "\t}\n"
    appendListDefine += appendListDefineTemplate.format(key = k, Key = K)

fp = open(templatesPath + "\\" + templateName, "r", encoding = "utf-8")
fpout = open(outPath + "\\"+ fileName, "w", encoding = "utf-8")
print(outPath + "\\"+ fileName)
text = fp.read()
text = text.replace("{dateDefine}", dateDefine)
text = text.replace("{functionDefine}", functiondefine)
text = text.replace("{appendListDefine}", appendListDefine)
text = text.replace("{Object}", Obj)
text = text.replace("{object}", obj)
fpout.write(text)
fpout.close()
fp.close()