import os
import json
print("this is " + __name__ )

# 模板地址
templatesPath = "Templates"
# 输出地址
outPath = "RuoYi\\ruoyi-system\\src\\main\\resources\\mapper\\system"
# outPath = "RuoYi\\ruoyi-admin\\src\\main\\resources\\templates\\{object}".replace("{object}", obj)
if os.path.exists(outPath) == False:
    os.makedirs(outPath)
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
templateName = "{Object}Mapper.xml"
# 文件名称
fileName = templateName.replace("{object}", obj).replace("{Object}", Obj)
#表格名称
sheet = cfg["sheet"]
# 输出模板         
resultMapperTemplate = "\t\t<result property=\"{key}\" column=\"{sqlName}\"/>\n"
selectListTemplate = "\t\t\t<if test=\"{isNullTemplate}\"> and {sqlName} = #{{key}}</if>\n"
insertKeyTemplate = "\t\t<if test=\"{isNullTemplate}\">{sqlName},</if>\n"
insertValueTemplate = "\t\t<if test=\"{isNullTemplate}\"> #{{key}},</if>\n"
updateTemplate = "\t\t\t<if test=\"{isNullTemplate}\">{sqlName} = #{{key}},</if>\n"

resultMapDefine = ""
selectListDefine = ""
insertKeyDefine = ""
insertValueDefine = ""
updateDefine = ""
for k in dateDict.keys():
    if dateDict[k]["type"] != "String":
        isNullTemplate = "{key} != null"
    else: 
        isNullTemplate = "{key} != null and {key} != ''"
    resultMapDefine += resultMapperTemplate.replace("{key}", k).replace("{sqlName}", dateDict[k]["sqlName"])
    isNullNode = isNullTemplate.replace("{key}", k)
    selectListDefine += selectListTemplate.replace("{isNullTemplate}", isNullNode).replace("{key}", k).replace("{sqlName}", dateDict[k]["sqlName"])
    insertKeyDefine += insertKeyTemplate.replace("{isNullTemplate}", isNullNode).replace("{key}", k).replace("{sqlName}", dateDict[k]["sqlName"])
    insertValueDefine += insertValueTemplate.replace("{isNullTemplate}", isNullNode).replace("{key}", k).replace("{sqlName}", dateDict[k]["sqlName"])
    updateDefine += updateTemplate.replace("{isNullTemplate}", isNullNode).replace("{key}", k).replace("{sqlName}", dateDict[k]["sqlName"])

fp = open(templatesPath + "\\" + templateName, "r", encoding = "utf-8")
text = fp.read()
fp.close()
text = text.replace("{object}", obj)
text = text.replace("{Object}", Obj)
text = text.replace("{resultMapDefine}", resultMapDefine)
text = text.replace("{selectListDefine}", selectListDefine)
text = text.replace("{insertKeyDefine}", insertKeyDefine)
text = text.replace("{insertValueDefine}", insertValueDefine)
text = text.replace("{updateDefine}", updateDefine)
text = text.replace("{sheet}", sheet)

fpout = open(outPath + "\\"+ fileName, "w", encoding = "utf-8")
fpout.write(text)
fpout.close()