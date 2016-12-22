
# -*- coding: utf-8 -*-

import os
import types
import datetime


import ClassInfo
import CodeTemplate



def UIMethod(classInfo):

    setupViewBodyDesc = setupViewMethodBody(classInfo)
    setupConstraintDesc = setupConstraintMethodBody(classInfo)
    setupEventMethodDesc = setupEventMethodBody(classInfo)

    uiMethodDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_view_UIMethod]

    desc = "#pragma mark - UI \n\n"
    desc += uiMethodDesc % (setupViewBodyDesc, setupConstraintDesc, setupEventMethodDesc)
    return desc


def SetMethod(classInfo):

    setMethodDesc = ''
    for propertyItem in classInfo.propertyArr:

        propertyClassName = propertyItem[0]
        propertyName = propertyItem[1]

        tempClassName = propertyClassName.lower()
        if tempClassName.endswith("label"):
            setMethodDesc += createLabel(propertyClassName, propertyName)
        elif tempClassName.endswith("imageview"):
            setMethodDesc += createImageView(propertyClassName, propertyName)
        elif tempClassName.endswith("button"):
            setMethodDesc += createButton(propertyClassName, propertyName)
        elif tempClassName.endswith("textfield"):
            setMethodDesc += createTextField(propertyClassName, propertyName)
        else:
            setMethodDesc += createView.createView(propertyClassName, propertyName)

    desc = "#pragma mark - Setter \n\n"
    return desc + setMethodDesc







######################### set方法 #############################

def createView(className, propertyName):

    methodDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_set_method_UIView]
    return methodDesc % (className, propertyName, propertyName, propertyName, className, "", propertyName)


def createLabel(className, propertyName):

    methodDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_set_method_UIView]

    bodyDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_set_method_UITextField]
    bodyDesc = bodyDesc % (propertyName)

    return methodDesc % (className, propertyName, propertyName, propertyName, className, bodyDesc, propertyName)


def createImageView(className, propertyName):

    methodDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_set_method_UIView]

    bodyDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_set_method_UIImageView]
    bodyDesc = bodyDesc % (propertyName)

    return methodDesc % (className, propertyName, propertyName, propertyName, className, bodyDesc, propertyName)


def createButton(className, propertyName):

    methodDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_set_method_UIView]

    bodyDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_set_method_UIButton]
    bodyDesc = bodyDesc % (propertyName, propertyName)

    return methodDesc % (className, propertyName, propertyName, propertyName, className, bodyDesc, propertyName)



def createTextField(className, propertyName):

    methodDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_set_method_UIView]

    bodyDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_set_method_UITextField]
    bodyDesc = bodyDesc % (propertyName)

    return methodDesc % (className, propertyName, propertyName, propertyName, className, bodyDesc, propertyName)








######################### UI方法 #############################


def setupViewMethodBody(classInfo):

    addViewDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_view_addview]
    if classInfo.type == ClassInfo.classType_cell:
        #cell
        addViewDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_cell_addview]
    elif classInfo.type == ClassInfo.classType_view:
        #view
        addViewDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_view_addview]
    elif classInfo.type == ClassInfo.classType_viewcontroller:
        #viewController
        addViewDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_viewcontroller_addview]

    methodBodyDesc = ''
    for propertyItem in classInfo.propertyArr:
        methodBodyDesc += addViewDesc % propertyItem[1]

    return methodBodyDesc




def setupConstraintMethodBody(classInfo):

    makeConstraintDesc = CodeTemplate.templateDic[CodeTemplate.templateKey_view_makeConstraint]

    methodBodyDesc = ''
    for propertyItem in classInfo.propertyArr:
        methodBodyDesc += makeConstraintDesc % propertyItem[1]

    return methodBodyDesc



def setupEventMethodBody(classInfo):

    return ""



