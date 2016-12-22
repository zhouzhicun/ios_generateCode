
# -*- coding: utf-8 -*-

import os
import types
import datetime

import ClassInfo
import CodeTemplate
import GenerateMethod



def fileDescInfo(projectName, curDate, classInfo):

    file_desc = CodeTemplate.templateDic[CodeTemplate.templateKey_file_desc]
    return file_desc % (classInfo.className, projectName, curDate)


def propertyDefine(classInfo):

    property_desc = CodeTemplate.templateDic[CodeTemplate.templateKey_property]

    body = ''
    for item in classInfo.propertyArr:

        propertyClassName = item[0]
        propertyName = item[1]

        body += property_desc % (propertyClassName, propertyName)

    return body



def headerFile(projectName, curDate, classInfo):

    fileName = classInfo.className + '.h'

    baseClsName = classInfo.baseClassName
    clsName = classInfo.className

    fileDesc = fileDescInfo(projectName, curDate, classInfo)
    propertyDesc = propertyDefine(classInfo)
    headerFileTemplate = CodeTemplate.templateDic[CodeTemplate.templateKey_header_file]


    body = headerFileTemplate % (fileDesc, baseClsName, clsName, baseClsName, propertyDesc)
    return (fileName, body)



def ImplementFile(projectName, curDate, classInfo):

    fileName = classInfo.className + '.m'

    baseClsName = classInfo.baseClassName
    clsName = classInfo.className

    implementFileTemplate = CodeTemplate.templateDic[CodeTemplate.templateKey_implement_file]

    fileDesc = fileDescInfo(projectName, curDate, classInfo)
    uiMethodDesc = GenerateMethod.UIMethod(classInfo)
    setterDesc = GenerateMethod.SetMethod(classInfo)

    body = ""
    if classInfo.type == ClassInfo.classType_cell:
        #cell
        otherMethodDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_cell_otherMethod]
        body = implementFileTemplate % (fileDesc, clsName, clsName, clsName, uiMethodDesc + otherMethodDesc + setterDesc)
    elif classInfo.type == ClassInfo.classType_view:
        #view
        otherMethodDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_view_otherMethod]
        body = implementFileTemplate % (fileDesc, clsName, clsName, clsName, uiMethodDesc + otherMethodDesc + setterDesc)
    elif classInfo.type == ClassInfo.classType_viewcontroller:
        #viewcontroller
        otherMethodDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_viewcontroller_otherMethod]
        body = implementFileTemplate % (fileDesc, clsName, clsName, clsName, uiMethodDesc + otherMethodDesc + setterDesc)
    elif classInfo.type == ClassInfo.classType_viewmodel:
        #viewmodel
        otherMethodDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_viewmodel_otherMethod]
        body = implementFileTemplate % (fileDesc, clsName, clsName, clsName, otherMethodDesc)

    return (fileName, body)



