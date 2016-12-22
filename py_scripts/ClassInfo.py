


# -*- coding: utf-8 -*-

import os
import types
import datetime

classType_cell = 1
classType_view = 2
classType_viewcontroller = 3
classType_viewmodel = 4

class ClassInfo:

    def __init__(self, baseClassName, className):
        self.className = className
        self.baseClassName = baseClassName
        self.propertyArr = []

        tempName = className.lower()
        if tempName.endswith("cell"):
            self.type = classType_cell
        elif tempName.endswith("view"):
            self.type = classType_view
        elif tempName.endswith("viewcontroller"):
            self.type = classType_viewcontroller
        elif tempName.endswith("viewmodel"):
            self.type = classType_viewmodel



