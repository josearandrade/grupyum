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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialogButtonBox,
    QDoubleSpinBox, QFrame, QLabel, QListWidget,
    QListWidgetItem, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_Grupy1(object):
    def setupUi(self, Grupy1):
        if not Grupy1.objectName():
            Grupy1.setObjectName(u"Grupy1")
        Grupy1.resize(1253, 482)
        self.label = QLabel(Grupy1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 191, 16))
        self.importButton = QPushButton(Grupy1)
        self.importButton.setObjectName(u"importButton")
        self.importButton.setGeometry(QRect(200, 10, 80, 23))
        self.list_selected_images = QListWidget(Grupy1)
        QListWidgetItem(self.list_selected_images)
        QListWidgetItem(self.list_selected_images)
        self.list_selected_images.setObjectName(u"list_selected_images")
        self.list_selected_images.setGeometry(QRect(10, 40, 256, 192))
        self.checkBox_good_yes = QCheckBox(Grupy1)
        self.checkBox_good_yes.setObjectName(u"checkBox_good_yes")
        self.checkBox_good_yes.setGeometry(QRect(60, 270, 83, 21))
        self.checkBox_good_no = QCheckBox(Grupy1)
        self.checkBox_good_no.setObjectName(u"checkBox_good_no")
        self.checkBox_good_no.setGeometry(QRect(170, 270, 83, 21))
        self.label_2 = QLabel(Grupy1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 250, 201, 16))
        self.label_3 = QLabel(Grupy1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 10, 71, 16))
        self.bluecolor_BL = QSpinBox(Grupy1)
        self.bluecolor_BL.setObjectName(u"bluecolor_BL")
        self.bluecolor_BL.setGeometry(QRect(510, 130, 51, 23))
        self.bluecolor_BL.setMaximum(255)
        self.bluecolor_BL.setValue(120)
        self.bluecell_BU = QSpinBox(Grupy1)
        self.bluecell_BU.setObjectName(u"bluecell_BU")
        self.bluecell_BU.setGeometry(QRect(510, 160, 51, 23))
        self.bluecell_BU.setMaximum(255)
        self.bluecell_BU.setValue(255)
        self.bluecell_GL = QSpinBox(Grupy1)
        self.bluecell_GL.setObjectName(u"bluecell_GL")
        self.bluecell_GL.setGeometry(QRect(450, 130, 51, 23))
        self.bluecell_GL.setMaximum(255)
        self.bluecell_GU = QSpinBox(Grupy1)
        self.bluecell_GU.setObjectName(u"bluecell_GU")
        self.bluecell_GU.setGeometry(QRect(450, 160, 51, 23))
        self.bluecell_GU.setMaximum(255)
        self.bluecell_GU.setValue(140)
        self.bluecell_RL = QSpinBox(Grupy1)
        self.bluecell_RL.setObjectName(u"bluecell_RL")
        self.bluecell_RL.setGeometry(QRect(390, 130, 51, 23))
        self.bluecell_RL.setMaximum(255)
        self.bluecell_RL.setValue(0)
        self.bluecell_RU = QSpinBox(Grupy1)
        self.bluecell_RU.setObjectName(u"bluecell_RU")
        self.bluecell_RU.setGeometry(QRect(390, 160, 51, 23))
        self.bluecell_RU.setMaximum(255)
        self.bluecell_RU.setValue(140)
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
        self.label_17 = QLabel(Grupy1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(380, 350, 141, 16))
        self.edge_select_canny = QRadioButton(Grupy1)
        self.edge_select_canny.setObjectName(u"edge_select_canny")
        self.edge_select_canny.setGeometry(QRect(330, 380, 99, 21))
        self.radioButton_2 = QRadioButton(Grupy1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(410, 380, 99, 21))
        self.radioButton_3 = QRadioButton(Grupy1)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(490, 380, 99, 21))
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
        self.edge_canny_lower.setValue(75)
        self.edge_canny_upper = QSpinBox(Grupy1)
        self.edge_canny_upper.setObjectName(u"edge_canny_upper")
        self.edge_canny_upper.setGeometry(QRect(510, 420, 61, 23))
        self.edge_canny_upper.setMaximum(9999)
        self.edge_canny_upper.setValue(100)
        self.perimeter_max = QSpinBox(Grupy1)
        self.perimeter_max.setObjectName(u"perimeter_max")
        self.perimeter_max.setGeometry(QRect(770, 50, 71, 23))
        self.perimeter_max.setMaximum(99999)
        self.perimeter_max.setValue(100)
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
        self.min_circ_value = QDoubleSpinBox(Grupy1)
        self.min_circ_value.setObjectName(u"min_circ_value")
        self.min_circ_value.setGeometry(QRect(700, 120, 62, 23))
        self.min_circ_value.setMaximum(1.000000000000000)
        self.min_circ_value.setValue(0.010000000000000)
        self.list_results = QListWidget(Grupy1)
        QListWidgetItem(self.list_results)
        QListWidgetItem(self.list_results)
        self.list_results.setObjectName(u"list_results")
        self.list_results.setGeometry(QRect(885, 80, 331, 361))
        self.progressBar = QProgressBar(Grupy1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(650, 240, 171, 23))
        self.progressBar.setValue(24)
        self.label_26 = QLabel(Grupy1)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(710, 210, 91, 16))
        self.startCancel = QDialogButtonBox(Grupy1)
        self.startCancel.setObjectName(u"startCancel")
        self.startCancel.setGeometry(QRect(650, 170, 166, 24))
        self.startCancel.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_27 = QLabel(Grupy1)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(890, 20, 91, 16))
        self.line_3 = QFrame(Grupy1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(850, 0, 20, 641))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_28 = QLabel(Grupy1)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(890, 60, 91, 16))
        self.label_29 = QLabel(Grupy1)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(990, 60, 91, 16))
        self.label_30 = QLabel(Grupy1)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(1080, 60, 91, 16))
        self.label_31 = QLabel(Grupy1)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(1160, 60, 91, 16))
        self.browncell_RL = QSpinBox(Grupy1)
        self.browncell_RL.setObjectName(u"browncell_RL")
        self.browncell_RL.setGeometry(QRect(390, 270, 51, 23))
        self.browncell_RL.setMaximum(255)
        self.browncell_RL.setValue(0)
        self.browncell_GL = QSpinBox(Grupy1)
        self.browncell_GL.setObjectName(u"browncell_GL")
        self.browncell_GL.setGeometry(QRect(450, 270, 51, 23))
        self.browncell_GL.setMaximum(255)
        self.browncell_GU = QSpinBox(Grupy1)
        self.browncell_GU.setObjectName(u"browncell_GU")
        self.browncell_GU.setGeometry(QRect(390, 300, 51, 23))
        self.browncell_GU.setMaximum(255)
        self.browncell_GU.setValue(255)
        self.browncolor_GU = QSpinBox(Grupy1)
        self.browncolor_GU.setObjectName(u"browncolor_GU")
        self.browncolor_GU.setGeometry(QRect(450, 300, 51, 23))
        self.browncolor_GU.setMaximum(255)
        self.browncolor_GU.setValue(255)
        self.browncell_BL = QSpinBox(Grupy1)
        self.browncell_BL.setObjectName(u"browncell_BL")
        self.browncell_BL.setGeometry(QRect(510, 270, 51, 23))
        self.browncell_BL.setMaximum(255)
        self.browncell_BL.setValue(0)
        self.browncell_BU = QSpinBox(Grupy1)
        self.browncell_BU.setObjectName(u"browncell_BU")
        self.browncell_BU.setGeometry(QRect(510, 300, 51, 23))
        self.browncell_BU.setMaximum(255)
        self.browncell_BU.setValue(110)
        self.spinBox = QSpinBox(Grupy1)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(730, 380, 42, 23))

        self.retranslateUi(Grupy1)

        QMetaObject.connectSlotsByName(Grupy1)
    # setupUi

    def retranslateUi(self, Grupy1):
        Grupy1.setWindowTitle(QCoreApplication.translate("Grupy1", u"Grupy1", None))
        self.label.setText(QCoreApplication.translate("Grupy1", u"Import one or more images", None))
        self.importButton.setText(QCoreApplication.translate("Grupy1", u"Import", None))

        __sortingEnabled = self.list_selected_images.isSortingEnabled()
        self.list_selected_images.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_selected_images.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Grupy1", u"New Item", None));
        ___qlistwidgetitem1 = self.list_selected_images.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Grupy1", u"New Item", None));
        self.list_selected_images.setSortingEnabled(__sortingEnabled)

        self.checkBox_good_yes.setText(QCoreApplication.translate("Grupy1", u"Yes", None))
        self.checkBox_good_no.setText(QCoreApplication.translate("Grupy1", u"No", None))
        self.label_2.setText(QCoreApplication.translate("Grupy1", u"Are all images in good condition?", None))
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
        self.label_17.setText(QCoreApplication.translate("Grupy1", u"Edge Detection Method", None))
        self.edge_select_canny.setText(QCoreApplication.translate("Grupy1", u"Canny", None))
        self.radioButton_2.setText(QCoreApplication.translate("Grupy1", u"Other 1", None))
        self.radioButton_3.setText(QCoreApplication.translate("Grupy1", u"Other 2", None))
        self.label_19.setText(QCoreApplication.translate("Grupy1", u"Upper", None))
        self.label_20.setText(QCoreApplication.translate("Grupy1", u"Lower", None))
        self.label_22.setText(QCoreApplication.translate("Grupy1", u"min", None))
        self.label_23.setText(QCoreApplication.translate("Grupy1", u"max", None))
        self.label_24.setText(QCoreApplication.translate("Grupy1", u"Perimeter (px)", None))
        self.label_25.setText(QCoreApplication.translate("Grupy1", u"M\u00edn circularity", None))

        __sortingEnabled1 = self.list_results.isSortingEnabled()
        self.list_results.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.list_results.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Grupy1", u"Image 1 ----------- 1000 ------------- 32000 ------------- 33000", None));
        ___qlistwidgetitem3 = self.list_results.item(1)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Grupy1", u"Image 2 ----------- 300 ------------- 17000  -------------- 17300", None));
        self.list_results.setSortingEnabled(__sortingEnabled1)

        self.label_26.setText(QCoreApplication.translate("Grupy1", u"Loading", None))
        self.label_27.setText(QCoreApplication.translate("Grupy1", u"Results", None))
        self.label_28.setText(QCoreApplication.translate("Grupy1", u"Imagem", None))
        self.label_29.setText(QCoreApplication.translate("Grupy1", u"Blue", None))
        self.label_30.setText(QCoreApplication.translate("Grupy1", u"Brown", None))
        self.label_31.setText(QCoreApplication.translate("Grupy1", u"Total", None))
    # retranslateUi

