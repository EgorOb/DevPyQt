# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cpu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(525, 549)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_8.addWidget(self.label_16)

        self.spinBoxSystemInfoDelay = QSpinBox(self.frame_3)
        self.spinBoxSystemInfoDelay.setObjectName(u"spinBoxSystemInfoDelay")
        self.spinBoxSystemInfoDelay.setMinimum(1)
        self.spinBoxSystemInfoDelay.setMaximum(6000)

        self.horizontalLayout_8.addWidget(self.spinBoxSystemInfoDelay)

        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_8.addWidget(self.label_17)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_3.addWidget(self.label_4)

        self.progressBarCPU = QProgressBar(self.frame_3)
        self.progressBarCPU.setObjectName(u"progressBarCPU")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBarCPU.sizePolicy().hasHeightForWidth())
        self.progressBarCPU.setSizePolicy(sizePolicy)
        self.progressBarCPU.setMaximumSize(QSize(150, 16777215))
        self.progressBarCPU.setValue(0)
        self.progressBarCPU.setAlignment(Qt.AlignCenter)
        self.progressBarCPU.setOrientation(Qt.Vertical)
        self.progressBarCPU.setInvertedAppearance(False)
        self.progressBarCPU.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_3.addWidget(self.progressBarCPU)

        self.labelCPUPercent = QLabel(self.frame_3)
        self.labelCPUPercent.setObjectName(u"labelCPUPercent")
        self.labelCPUPercent.setMaximumSize(QSize(150, 16777215))
        self.labelCPUPercent.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelCPUPercent)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_4.addWidget(self.label_15)

        self.progressBarRAM = QProgressBar(self.frame_3)
        self.progressBarRAM.setObjectName(u"progressBarRAM")
        sizePolicy.setHeightForWidth(self.progressBarRAM.sizePolicy().hasHeightForWidth())
        self.progressBarRAM.setSizePolicy(sizePolicy)
        self.progressBarRAM.setMaximumSize(QSize(150, 16777215))
        self.progressBarRAM.setValue(0)
        self.progressBarRAM.setOrientation(Qt.Vertical)

        self.verticalLayout_4.addWidget(self.progressBarRAM)

        self.labelRAMPercent = QLabel(self.frame_3)
        self.labelRAMPercent.setObjectName(u"labelRAMPercent")
        self.labelRAMPercent.setMaximumSize(QSize(150, 16777215))
        self.labelRAMPercent.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelRAMPercent)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0441\u0438\u0441\u0442\u0435\u043c\u044b:", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u043b\u044f\u0442\u044c \u043a\u0430\u0436\u0434\u044b\u0435:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u0441\u0435\u043a.", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"CPU", None))
        self.labelCPUPercent.setText(QCoreApplication.translate("Form", u"X%", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"RAM", None))
        self.labelRAMPercent.setText(QCoreApplication.translate("Form", u"X%", None))
    # retranslateUi

