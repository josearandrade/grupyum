# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGroupBox,
    QLabel, QListWidget, QListWidgetItem, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_Grupy1(object):
    def setupUi(self, Grupy1):
        if not Grupy1.objectName():
            Grupy1.setObjectName(u"Grupy1")
        Grupy1.resize(1498, 482)
        self.label = QLabel(Grupy1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 191, 16))
        self.importButton = QPushButton(Grupy1)
        self.importButton.setObjectName(u"importButton")
        self.importButton.setGeometry(QRect(200, 10, 80, 23))
        self.list_selected_images = QListWidget(Grupy1)
        self.list_selected_images.setObjectName(u"list_selected_images")
        self.list_selected_images.setGeometry(QRect(20, 40, 256, 192))
        self.label_3 = QLabel(Grupy1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 10, 71, 16))
        self.bluecell_LB = QSpinBox(Grupy1)
        self.bluecell_LB.setObjectName(u"bluecell_LB")
        self.bluecell_LB.setGeometry(QRect(510, 130, 51, 23))
        self.bluecell_LB.setMaximum(255)
        self.bluecell_LB.setValue(0)
        self.bluecell_UB = QSpinBox(Grupy1)
        self.bluecell_UB.setObjectName(u"bluecell_UB")
        self.bluecell_UB.setGeometry(QRect(510, 160, 51, 23))
        self.bluecell_UB.setMaximum(255)
        self.bluecell_UB.setValue(0)
        self.bluecell_LG = QSpinBox(Grupy1)
        self.bluecell_LG.setObjectName(u"bluecell_LG")
        self.bluecell_LG.setGeometry(QRect(450, 130, 51, 23))
        self.bluecell_LG.setMaximum(255)
        self.bluecell_UG = QSpinBox(Grupy1)
        self.bluecell_UG.setObjectName(u"bluecell_UG")
        self.bluecell_UG.setGeometry(QRect(450, 160, 51, 23))
        self.bluecell_UG.setMaximum(255)
        self.bluecell_UG.setValue(0)
        self.bluecell_LR = QSpinBox(Grupy1)
        self.bluecell_LR.setObjectName(u"bluecell_LR")
        self.bluecell_LR.setGeometry(QRect(390, 130, 51, 23))
        self.bluecell_LR.setMaximum(255)
        self.bluecell_LR.setValue(0)
        self.bluecell_UR = QSpinBox(Grupy1)
        self.bluecell_UR.setObjectName(u"bluecell_UR")
        self.bluecell_UR.setGeometry(QRect(390, 160, 51, 23))
        self.bluecell_UR.setMaximum(255)
        self.bluecell_UR.setValue(0)
        self.label_4 = QLabel(Grupy1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 40, 191, 16))
        self.label_5 = QLabel(Grupy1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(400, 100, 31, 16))
        self.label_6 = QLabel(Grupy1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(450, 100, 41, 16))
        self.label_7 = QLabel(Grupy1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(510, 100, 41, 16))
        self.label_8 = QLabel(Grupy1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(330, 70, 111, 16))
        self.label_9 = QLabel(Grupy1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(330, 210, 71, 16))
        self.label_10 = QLabel(Grupy1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(330, 130, 41, 16))
        self.label_11 = QLabel(Grupy1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(330, 160, 41, 16))
        self.label_12 = QLabel(Grupy1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(400, 240, 31, 16))
        self.label_13 = QLabel(Grupy1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(450, 240, 41, 16))
        self.label_14 = QLabel(Grupy1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(330, 270, 41, 16))
        self.label_15 = QLabel(Grupy1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(510, 240, 41, 16))
        self.label_16 = QLabel(Grupy1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(330, 300, 41, 16))
        self.line = QFrame(Grupy1)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(283, 0, 20, 641))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(Grupy1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(590, 0, 20, 641))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_19 = QLabel(Grupy1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(450, 420, 41, 16))
        self.label_20 = QLabel(Grupy1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(310, 420, 41, 16))
        self.edge_canny_lower = QSpinBox(Grupy1)
        self.edge_canny_lower.setObjectName(u"edge_canny_lower")
        self.edge_canny_lower.setGeometry(QRect(370, 420, 61, 23))
        self.edge_canny_lower.setMaximum(9999)
        self.edge_canny_lower.setValue(0)
        self.edge_canny_upper = QSpinBox(Grupy1)
        self.edge_canny_upper.setObjectName(u"edge_canny_upper")
        self.edge_canny_upper.setGeometry(QRect(510, 420, 61, 23))
        self.edge_canny_upper.setMaximum(9999)
        self.edge_canny_upper.setValue(0)
        self.perimeter_max = QSpinBox(Grupy1)
        self.perimeter_max.setObjectName(u"perimeter_max")
        self.perimeter_max.setGeometry(QRect(770, 50, 71, 23))
        self.perimeter_max.setMaximum(99999)
        self.perimeter_max.setValue(0)
        self.label_22 = QLabel(Grupy1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(630, 50, 41, 16))
        self.perimeter_min = QSpinBox(Grupy1)
        self.perimeter_min.setObjectName(u"perimeter_min")
        self.perimeter_min.setGeometry(QRect(660, 50, 71, 23))
        self.perimeter_min.setMaximum(99999)
        self.label_23 = QLabel(Grupy1)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(740, 50, 41, 16))
        self.label_24 = QLabel(Grupy1)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(690, 20, 91, 16))
        self.label_25 = QLabel(Grupy1)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(690, 90, 91, 16))
        self.min_circularity = QDoubleSpinBox(Grupy1)
        self.min_circularity.setObjectName(u"min_circularity")
        self.min_circularity.setGeometry(QRect(700, 120, 62, 23))
        self.min_circularity.setMaximum(1.000000000000000)
        self.min_circularity.setValue(0.010000000000000)
        self.list_results = QListWidget(Grupy1)
        self.list_results.setObjectName(u"list_results")
        self.list_results.setGeometry(QRect(885, 80, 591, 361))
        self.progressBar = QProgressBar(Grupy1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(650, 190, 171, 23))
        self.progressBar.setValue(0)
        self.label_27 = QLabel(Grupy1)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(890, 20, 91, 16))
        self.line_3 = QFrame(Grupy1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(850, 0, 20, 641))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.browncell_LR = QSpinBox(Grupy1)
        self.browncell_LR.setObjectName(u"browncell_LR")
        self.browncell_LR.setGeometry(QRect(390, 270, 51, 23))
        self.browncell_LR.setMaximum(255)
        self.browncell_LR.setValue(0)
        self.browncell_LG = QSpinBox(Grupy1)
        self.browncell_LG.setObjectName(u"browncell_LG")
        self.browncell_LG.setGeometry(QRect(450, 270, 51, 23))
        self.browncell_LG.setMaximum(255)
        self.browncell_UG = QSpinBox(Grupy1)
        self.browncell_UG.setObjectName(u"browncell_UG")
        self.browncell_UG.setGeometry(QRect(390, 300, 51, 23))
        self.browncell_UG.setMaximum(255)
        self.browncell_UG.setValue(0)
        self.browncell_UR = QSpinBox(Grupy1)
        self.browncell_UR.setObjectName(u"browncell_UR")
        self.browncell_UR.setGeometry(QRect(450, 300, 51, 23))
        self.browncell_UR.setMaximum(255)
        self.browncell_UR.setValue(0)
        self.browncell_LB = QSpinBox(Grupy1)
        self.browncell_LB.setObjectName(u"browncell_LB")
        self.browncell_LB.setGeometry(QRect(510, 270, 51, 23))
        self.browncell_LB.setMaximum(255)
        self.browncell_LB.setValue(0)
        self.browncell_UB = QSpinBox(Grupy1)
        self.browncell_UB.setObjectName(u"browncell_UB")
        self.browncell_UB.setGeometry(QRect(510, 300, 51, 23))
        self.browncell_UB.setMaximum(255)
        self.browncell_UB.setValue(0)
        self.loadButton = QPushButton(Grupy1)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setGeometry(QRect(100, 280, 101, 23))
        self.load_OK = QLabel(Grupy1)
        self.load_OK.setObjectName(u"load_OK")
        self.load_OK.setGeometry(QRect(130, 310, 58, 15))
        self.processButton = QPushButton(Grupy1)
        self.processButton.setObjectName(u"processButton")
        self.processButton.setGeometry(QRect(680, 220, 101, 23))
        self.groupBox = QGroupBox(Grupy1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(310, 340, 271, 61))
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(90, 30, 71, 21))
        self.edge_select_canny = QRadioButton(self.groupBox)
        self.edge_select_canny.setObjectName(u"edge_select_canny")
        self.edge_select_canny.setGeometry(QRect(20, 30, 61, 21))
        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(170, 30, 71, 21))
        self.exportButton = QPushButton(Grupy1)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setGeometry(QRect(890, 450, 121, 23))

        self.retranslateUi(Grupy1)

        QMetaObject.connectSlotsByName(Grupy1)
    # setupUi

    def retranslateUi(self, Grupy1):
        Grupy1.setWindowTitle(QCoreApplication.translate("Grupy1", u"Grupy1", None))
        self.label.setText(QCoreApplication.translate("Grupy1", u"Import one or more images", None))
        self.importButton.setText(QCoreApplication.translate("Grupy1", u"Import", None))
        self.label_3.setText(QCoreApplication.translate("Grupy1", u"Parameters", None))
        self.label_4.setText(QCoreApplication.translate("Grupy1", u"Color Thresholding", None))
        self.label_5.setText(QCoreApplication.translate("Grupy1", u"Red", None))
        self.label_6.setText(QCoreApplication.translate("Grupy1", u"Green", None))
        self.label_7.setText(QCoreApplication.translate("Grupy1", u"Blue", None))
        self.label_8.setText(QCoreApplication.translate("Grupy1", u"Blue Cells", None))
        self.label_9.setText(QCoreApplication.translate("Grupy1", u"Brown Cells", None))
        self.label_10.setText(QCoreApplication.translate("Grupy1", u"Lower", None))
        self.label_11.setText(QCoreApplication.translate("Grupy1", u"Upper", None))
        self.label_12.setText(QCoreApplication.translate("Grupy1", u"Red", None))
        self.label_13.setText(QCoreApplication.translate("Grupy1", u"Green", None))
        self.label_14.setText(QCoreApplication.translate("Grupy1", u"Lower", None))
        self.label_15.setText(QCoreApplication.translate("Grupy1", u"Blue", None))
        self.label_16.setText(QCoreApplication.translate("Grupy1", u"Upper", None))
        self.label_19.setText(QCoreApplication.translate("Grupy1", u"Upper", None))
        self.label_20.setText(QCoreApplication.translate("Grupy1", u"Lower", None))
        self.label_22.setText(QCoreApplication.translate("Grupy1", u"min", None))
        self.label_23.setText(QCoreApplication.translate("Grupy1", u"max", None))
        self.label_24.setText(QCoreApplication.translate("Grupy1", u"Perimeter (px)", None))
        self.label_25.setText(QCoreApplication.translate("Grupy1", u"M\u00edn circularity", None))
        self.label_27.setText(QCoreApplication.translate("Grupy1", u"Results", None))
        self.loadButton.setText(QCoreApplication.translate("Grupy1", u"Load Images", None))
        self.load_OK.setText(QCoreApplication.translate("Grupy1", u"Load OK", None))
        self.processButton.setText(QCoreApplication.translate("Grupy1", u"Process", None))
        self.groupBox.setTitle(QCoreApplication.translate("Grupy1", u"Edge Detection Method", None))
        self.radioButton_2.setText(QCoreApplication.translate("Grupy1", u"Other 1", None))
        self.edge_select_canny.setText(QCoreApplication.translate("Grupy1", u"Canny", None))
        self.radioButton_3.setText(QCoreApplication.translate("Grupy1", u"Other 2", None))
        self.exportButton.setText(QCoreApplication.translate("Grupy1", u"Exportar Dados", None))
    # retranslateUi

