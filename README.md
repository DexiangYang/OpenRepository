作者联系方式：
QQ：3061474178
该工具适用于若依开发系统，工具用于傻瓜式添加页面，将工具拷贝至RuoYi的上级文件夹即
/RuoYi
    系统原始文件夹
/RuoYiTemplates
    总模板
/Templates
    部分特殊部分模板
RuoYiDomainTool.py
    实体类替换程序
RuoYiMainHTMLTool.py
    主页面替换程序
RuoYiMapperTool.py
    JDBC交互替换程序
RuoYiTool.py
    系统总替换程序
系统简单原理是直接根据规则替换原有代码中的对应字符借以生成同样效果的页面，接口部分通用，但仍有部分页面需要自己设置模板。