from PyQt5.QtCore import QMetaObject, QRect, QSize, QCoreApplication
from PyQt5.QtGui import QColor, QFont, Qt, QPixmap
from PyQt5.QtWidgets import QTabWidget, QWidget, QHBoxLayout, QLabel, QFrame, QComboBox, QPushButton, QCheckBox, \
    QDoubleSpinBox, QSpinBox, QLineEdit, QVBoxLayout


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle('Inventory Application')
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(640, 550)
        MainWindow.setFixedSize(640, 550)

        font = QFont()
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                 "border-radius:0px;\n"
                                 "font-family: \"Trebuchet MS\";\n"
                                 )
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        font = QFont()
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("\n"
                                         "font-family: \"Trebuchet MS\";"
                                         "background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        font = QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab:selected {\n"
                                     "    background-color: rgb(63, 122, 138);\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "QTabBar::tab:!selected {\n"
                                     "    margin-left: 2px;"
                                     "    color: rgb(63, 122, 138);\n"
                                     "    background-color: rgb(255, 255, 255);\nborder:2px solid rgb(63, 122, 138);"
                                     "}\n"
                                     "QTabWidget{\n"
                                     "    border-radius:15px;\n"
                                     "    color: rgb(63, 122, 138);\n"
                                     "    background-color: rgb(255, 255, 255);\n"
                                     "    border:0px solid rgb(0,0,0);}\n"

                                     "QTabWidget::tab-bar{alignment: centre;border:0px solid rgb(0,0,0);}"

                                     "QTabWidget::pane{border:1px solid black;}"
                                     "")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")

        self.setupInventoryTab()
        self.setupSimulationTab()
        self.setupCombineTab()

        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)
    def setupSimulationTab(self):
        self.sim_tab = QWidget()
        font = QFont()
        self.sim_tab.setFont(font)

        self.sim_tab.setStyleSheet("font-family: \"Trebuchet MS\";border:0px solid rgb(0,0,0);")
        self.sim_tab.setObjectName("sim_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.sim_tab)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_3 = QFrame(self.sim_tab)
        self.frame_3.setMinimumSize(QSize(241, 0))
        font = QFont()
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                   "border-radius:10px;\n"
                                   "font-family: \"Trebuchet MS\"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.background_1 = QLabel(self.frame_3)
        self.background_1.setScaledContents(True)
        self.background_1.setGeometry(QRect(0, 0, 621, 550))
        self.background_1.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                        "border-radius:10px")
        self.background_1.setFrameShape(QFrame.NoFrame)
        self.background_1.setLineWidth(0)
        self.background_1.setText("")
        self.background_1.setPixmap(QPixmap("files\\Background.jpg"))
        self.background_1.setObjectName("background_1")
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setGeometry(QRect(100, 180, 391, 31))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(243, 243, 243);\n"
                                    "border-radius:10px;\n"
                                    "background-color: rgb(63, 122, 138);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font-family: \"Trebuchet MS\"")
        self.label_19.setObjectName("label_19")

        self.label_22 = QLabel(self.frame_3)
        self.label_22.setGeometry(QRect(100, 220, 391, 31))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(243, 243, 243);\n"
                                    "border-radius:10px;\n"
                                    "background-color: rgb(63, 122, 138);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font-family: \"Trebuchet MS\"")
        self.label_22.setObjectName("label_22")

        self.label_20 = QLabel(self.frame_3)
        self.label_20.setGeometry(QRect(100, 140, 391, 31))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(243, 243, 243);\n"
                                    "background-color: rgb(2, 5, 3);\n"
                                    "border-radius:10px;\n"
                                    "background-color: rgb(63, 122, 138);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font-family: \"Trebuchet MS\"")
        self.label_20.setObjectName("label_20")
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setGeometry(QRect(100, 100, 391, 31))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(243, 243, 243);\n"
                                    "background-color: rgb(2, 5, 3);\n"
                                    "border-radius:10px;\n"
                                    "background-color: rgb(63, 122, 138);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font-family: \"Trebuchet MS\"")
        self.label_21.setObjectName("label_21")
        self.Simulation_period = QSpinBox(self.frame_3)
        self.Simulation_period.setGeometry(QRect(250, 105, 150, 22))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.Simulation_period.setFont(font)
        self.Simulation_period.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                             "border-radius:10px;\n"
                                             "background-color: rgb(243, 243, 243);;\n"
                                             "font-family: \"Trebuchet MS\";")
        self.Simulation_period.setMinimum(1)
        self.Simulation_period.setMaximum(10000)
        self.Simulation_period.setProperty("value", 1)
        self.Simulation_period.setObjectName("Simulation_period")

        self.sumulation_duration_type = QComboBox(self.frame_3)
        self.sumulation_duration_type.setGeometry(QRect(410, 107, 71, 22))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Trebuchet MS")
        self.sumulation_duration_type.setFont(font)
        self.sumulation_duration_type.setAutoFillBackground(False)
        self.sumulation_duration_type.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "  border: 1px solid grey;\n"
                                    "  background: white;\n"
                                    "  selection-background-color: blue;\n"
                                    "}\n"
                                    "QComboBox {\n"
                                    "  background: red;\n"
                                    "}\n"
                                    "QListView{background-color: rgb(0, 255, 255)}")

        model = self.sumulation_duration_type.model()
        for row, color in enumerate(['Months','Days']):
            self.sumulation_duration_type.addItem(color)
            model.setData(model.index(row, 0), QColor('white'), Qt.BackgroundRole)


        self.sumulation_duration_type.setObjectName("sumulation_duration_type")



        self.Consumption_Dev = QDoubleSpinBox(self.frame_3)
        self.Consumption_Dev.setGeometry(QRect(250, 145, 231, 22))
        font = QFont()
        font.setPointSize(8)
        self.Consumption_Dev.setFont(font)
        self.Consumption_Dev.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                           "border-radius:10px;\n"
                                           "background-color: rgb(243, 243, 243);\n"
                                           "font-family: \"Trebuchet MS\";")
        self.Consumption_Dev.setMaximum(200)
        self.Consumption_Dev.setSingleStep(1)
        self.Consumption_Dev.setObjectName("Consumption_Dev")
        self.Process_1 = QPushButton(self.frame_3)
        self.Process_1.setGeometry(QRect(230, 350, 131, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Process_1.setFont(font)
        self.Process_1.setObjectName("Process_1")

        self.Process_1.setStyleSheet(
            """
            QPushButton {
                color: rgb(243, 243, 243);
border-color: rgb(243, 243, 243);
border-left-radius:10px;
background-color: rgb(63, 122, 138);
            }
            }
            QPushButton:hover {
                color: rgb(63, 122, 138);
                background-color: rgb(243, 243, 243);
                border-style: inset;
            }
            QPushButton:pressed {
            color: rgb(243, 243, 243);
                background-color: rgb(63, 122, 138);
                border-style: inset;
            }
            """
        )

        self.BrowseFile_1 = QPushButton(self.frame_3)
        self.BrowseFile_1.setGeometry(QRect(420, 300, 71, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.BrowseFile_1.setFont(font)
        self.BrowseFile_1.setStyleSheet("color: rgb(243, 243, 243);\n"
                                        "border-color: rgb(243, 243, 243);\n"
                                        "background-color: rgb(2, 5, 3);\n"
                                        "border-left-radius:10px;\n"
                                        "background-color: rgb(63, 122, 138);\n"
                                        "hover {\n"
                                        "                background-color: rgb(0, 0, 138);\n"
                                        "                border-style: inset;\n"
                                        "            }")
        self.BrowseFile_1.setObjectName("BrowseFile_1")

        self.BrowseFile_1.setStyleSheet(
            """
            QPushButton {
                color: rgb(243, 243, 243);
border-color: rgb(243, 243, 243);
border-left-radius:10px;
background-color: rgb(63, 122, 138);
            }
            }
            QPushButton:hover {
                color: rgb(63, 122, 138);
                background-color: rgb(243, 243, 243);
                border-style: inset;
            }
            QPushButton:pressed {
            color: rgb(243, 243, 243);
                background-color: rgb(63, 122, 138);
                border-style: inset;
            }
            """
        )

        self.label_23 = QLabel(self.frame_3)
        self.label_23.setGeometry(QRect(100, 300, 334, 31))
        self.label_23.setStyleSheet("color: rgb(243, 243, 243);\n"
                                    "border-color: rgb(255, 255, 255);\n"
                                    "border-radius:10px;\n"
                                    "background-color: rgb(63, 122, 138);\n"
                                    "")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.ExcelPath_1 = QLineEdit(self.frame_3)
        self.ExcelPath_1.setGeometry(QRect(110, 307, 301, 20))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.ExcelPath_1.setFont(font)
        self.ExcelPath_1.setStyleSheet("border-radius:10px;\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(149, 149, 149);\n"
                                       "font-family: \"Trebuchet MS\"")
        self.ExcelPath_1.setObjectName("ExcelPath_1")

        self.simulation_title_label = QLabel(self.frame_3)
        self.simulation_title_label.setGeometry(QRect(190, 20, 221, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.simulation_title_label.setFont(font)
        self.simulation_title_label.setAutoFillBackground(False)
        self.simulation_title_label.setStyleSheet("color: rgb(243, 243, 243);\n"
                                                  "background-color: rgb(2, 5, 3);\n"
                                                  "border-radius:10px")
        self.simulation_title_label.setFrameShape(QFrame.WinPanel)
        self.simulation_title_label.setFrameShadow(QFrame.Raised)
        self.simulation_title_label.setLineWidth(47)
        self.simulation_title_label.setMidLineWidth(18)
        self.simulation_title_label.setTextFormat(Qt.RichText)
        self.simulation_title_label.setScaledContents(True)
        self.simulation_title_label.setAlignment(Qt.AlignCenter)
        self.simulation_title_label.setIndent(-1)
        self.simulation_title_label.setObjectName("simulation_title_label")

        self.Close_1 = QPushButton(self.frame_3)
        self.Close_1.setGeometry(QRect(530, 20, 61, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Close_1.setFont(font)
        self.Close_1.setStyleSheet("color: rgb(2, 5, 3);\n"
                                   "background-color: rgb(243, 243, 243);\n"
                                   "border-radius:10px")
        self.Close_1.setObjectName("Close_1")
        self.Minimize_1 = QPushButton(self.frame_3)
        self.Minimize_1.setGeometry(QRect(520, 20, 41, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Minimize_1.setFont(font)
        self.Minimize_1.setStyleSheet("color: rgb(243, 243, 243);\n"
                                      "background-color: rgb(2, 5, 3);\n"
                                      "border-radius:10px")
        self.Minimize_1.setObjectName("Minimize_1")
        self.Remove_Negs = QCheckBox(self.frame_3)
        self.Remove_Negs.setGeometry(QRect(355, 227, 21, 21))
        font = QFont()
        font.setPointSize(8)
        self.Remove_Negs.setFont(font)
        self.Remove_Negs.setStyleSheet("color: rgb(243, 243, 243);\n"
                                       "background-color: rgb(2, 5, 3);\n"
                                       "border-radius:0px;\n"
                                       "background-color: rgb(63, 122, 138);\n"
                                       "font-family: \"Trebuchet MS\";")
        self.Remove_Negs.setObjectName("Count_Negs")
        self.price = QDoubleSpinBox(self.frame_3)
        self.price.setGeometry(QRect(250, 186, 231, 20))
        font = QFont()
        font.setPointSize(8)
        self.price.setFont(font)
        self.price.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                 "border-radius:10px;\n"
                                 "background-color: rgb(243, 243, 243);\n"
                                 "font-family: \"Trebuchet MS\";")
        self.price.setMinimum(1.0)
        self.price.setSingleStep(0.01)
        self.price.setProperty("value", 1.0)
        self.price.setObjectName("price")

        self.label_25 = QLabel(self.frame_3)
        self.label_25.setGeometry(QRect(100, 260, 391, 31))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(243, 243, 243);\n"
                                    "border-radius:10px;\n"
                                    "background-color: rgb(63, 122, 138);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font-family: \"Trebuchet MS\"")
        self.label_25.setObjectName("label_22")

        self.Round_LT = QCheckBox(self.frame_3)
        self.Round_LT.setGeometry(QRect(355, 267, 21, 21))
        font = QFont()
        font.setPointSize(8)
        self.Round_LT.setFont(font)
        self.Round_LT.setStyleSheet("color: rgb(243, 243, 243);\n"
                                       "background-color: rgb(2, 5, 3);\n"
                                       "border-radius:0px;\n"
                                       "background-color: rgb(63, 122, 138);\n"
                                       "font-family: \"Trebuchet MS\";")
        self.Round_LT.setObjectName("Count_Negs")


        self.horizontalLayout_4.addWidget(self.frame_3)
        self.tabWidget.addTab(self.sim_tab, "")
    def setupInventoryTab(self):
        self.inv_tab = QWidget()
        font = QFont()
        self.inv_tab.setFont(font)
        self.inv_tab.setStyleSheet("font-family: \"Trebuchet MS\";border:0px solid rgb(0,0,0);")
        self.inv_tab.setObjectName("inv_tab")
        self.horizontalLayout_1 = QHBoxLayout(self.inv_tab)
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1.setSpacing(0)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.frame = QFrame(self.inv_tab)
        self.frame.setMinimumSize(QSize(241, 0))
        self.frame.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                    "border-radius:10px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")

        self.optimizer_title_label = QLabel(self.frame)
        self.optimizer_title_label.setGeometry(QRect(190, 20, 221, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.optimizer_title_label.setFont(font)
        self.optimizer_title_label.setAutoFillBackground(False)
        self.optimizer_title_label.setStyleSheet("color: rgb(243, 243, 243);\n"
                                                    "background-color: rgb(2, 5, 3);\n"
                                                    "border-radius:10px")
        self.optimizer_title_label.setFrameShape(QFrame.WinPanel)
        self.optimizer_title_label.setFrameShadow(QFrame.Raised)
        self.optimizer_title_label.setLineWidth(47)
        self.optimizer_title_label.setMidLineWidth(18)
        self.optimizer_title_label.setTextFormat(Qt.RichText)
        self.optimizer_title_label.setScaledContents(True)
        self.optimizer_title_label.setAlignment(Qt.AlignCenter)
        self.optimizer_title_label.setIndent(-1)
        self.optimizer_title_label.setObjectName("optimizer_title_label")

        self.BrowseFile = QPushButton(self.frame)
        self.BrowseFile.setGeometry(QRect(420, 300, 71, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.BrowseFile.setFont(font)
        self.BrowseFile.setStyleSheet("color: rgb(243, 243, 243);\n"
                                         "border-color: rgb(243, 243, 243);\n"
                                         "background-color: rgb(2, 5, 3);\n"
                                         "border-left-radius:10px;\n"
                                         "background-color: rgb(63, 122, 138);\n"
                                         "hover {\n"
                                         "                background-color: rgb(0, 0, 138);\n"
                                         "                border-style: inset;\n"
                                         "            }")
        self.BrowseFile.setObjectName("BrowseFile")
        self.label_8 = QLabel(self.frame)
        self.label_8.setGeometry(QRect(100, 300, 334, 31))
        self.label_8.setStyleSheet("color: rgb(243, 243, 243);\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "border-radius:10px;\n"
                                      "background-color:rgb(63, 122, 138);\n"
        "")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.BrowseFile.setStyleSheet(
            """
            QPushButton {
                color: rgb(243, 243, 243);
        border-color: rgb(243, 243, 243);

        border-right-radius:10px;
        border-left-radius:1px;
        background-color: rgb(63, 122, 138);
            }
            }
            QPushButton:hover {
                color: rgb(63, 122, 138);
                background-color: rgb(243, 243, 243);
                border-style: inset;
            }
            QPushButton:pressed {
            color: rgb(243, 243, 243);
                background-color: rgb(63, 122, 138);
                border-style: inset;
            }
            """
        )

        self.Process = QPushButton(self.frame)
        self.Process.setGeometry(QRect(230, 350, 131, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Process.setFont(font)
        self.Process.setStyleSheet(
            """
            QPushButton {
                color: rgb(243, 243, 243);
        border-color: rgb(243, 243, 243);
        border-left-radius:10px;
        background-color: rgb(63, 122, 138);
            }
            }
            QPushButton:hover {
                color: rgb(63, 122, 138);
                background-color: rgb(243, 243, 243);
                border-style: inset;
            }
            QPushButton:pressed {
            color: rgb(243, 243, 243);
                background-color: rgb(63, 122, 138);
                border-style: inset;
            }
            """
        )
        self.Process.setObjectName("Process")

        self.Close = QPushButton(self.frame)
        self.Close.setGeometry(QRect(530, 20, 61, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Close.setFont(font)
        self.Close.setStyleSheet("color: rgb(2, 5, 3);\n"
                                    "background-color: rgb(243, 243, 243);\n"
                                    "border-radius:10px")
        self.Close.setObjectName("Close")
        self.Minimize = QPushButton(self.frame)
        self.Minimize.setGeometry(QRect(520, 20, 41, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Minimize.setFont(font)
        self.Minimize.setStyleSheet("color: rgb(243, 243, 243);\n"
                                       "background-color: rgb(2, 5, 3);\n"
                                       "border-radius:10px")
        self.Minimize.setObjectName("Minimize")

        self.ExcelPath = QLineEdit(self.frame)
        self.ExcelPath.setGeometry(QRect(110, 305, 301, 20))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.ExcelPath.setFont(font)
        self.ExcelPath.setStyleSheet("border-radius:10px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(149, 149, 149);\n"
                                        "font-family: \"Trebuchet MS\"")
        self.ExcelPath.setText("")
        self.ExcelPath.setObjectName("ExcelPath")
        self.background = QLabel(self.frame)
        self.background.setGeometry(QRect(0, 0, 621, 550)) #421
        self.background.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                         "border-radius:10px")
        self.background.setText("")
        self.background.setScaledContents(True)
        self.background.setPixmap(QPixmap("files\\Background.jpg"))
        self.background.setObjectName("background")

        self.label_3 = QLabel(self.frame)
        self.label_3.setGeometry(QRect(100, 200, 391, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(243, 243, 243);\n"
                                      "background-color: rgb(2, 5, 3);\n"
                                      "border-radius:10px;\n"
                                      "background-color: rgb(63, 122, 138);\n"
                                      "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self.frame)
        self.label_4.setGeometry(QRect(100, 150, 391, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(243, 243, 243);\n"
                                      "background-color: rgb(2, 5, 3);\n"
                                      "border-radius:10px;\n"
                                      "background-color: rgb(63, 122, 138);\n"
                                      "color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.label_5 = QLabel(self.frame)
        self.label_5.setGeometry(QRect(100, 100, 391, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(243, 243, 243);\n"
                                      "background-color: rgb(2, 5, 3);\n"
                                      "border-radius:10px;\n"
                                      "background-color: rgb(63, 122, 138);\n"
                                      "color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")

        self.Alpha = QLineEdit(self.frame)
        self.Alpha.setGeometry(QRect(250, 155, 231, 20))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Trebuchet MS")
        self.Alpha.setFont(font)
        self.Alpha.setStyleSheet("border-radius:10px;\n"
                                    "background-color: rgb(255, 255, 255);")
        self.Alpha.setInputMethodHints(Qt.ImhDigitsOnly)
        self.Alpha.setObjectName("Alpha")

        self.LT_Adjustment = QLineEdit(self.frame)
        self.LT_Adjustment.setGeometry(QRect(250, 105, 231, 20))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Trebuchet MS")
        self.LT_Adjustment.setFont(font)
        self.LT_Adjustment.setStyleSheet("border-radius:10px;\n"
                                            "background-color: rgb(255, 255, 255);")
        self.LT_Adjustment.setInputMethodHints(Qt.ImhDigitsOnly)
        self.LT_Adjustment.setObjectName("LT_Adjustment")

        self.ReviewPeriod = QLineEdit(self.frame)
        self.ReviewPeriod.setGeometry(QRect(250, 205, 231, 20))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Trebuchet MS")
        self.ReviewPeriod.setFont(font)
        self.ReviewPeriod.setStyleSheet("border-radius:10px;\n"
                                           "background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
        self.ReviewPeriod.setInputMethodHints(Qt.ImhDigitsOnly)
        self.ReviewPeriod.setObjectName("ReviewPeriod")

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setGeometry(QRect(250, 255, 231, 22))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Trebuchet MS")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);\n"
                                       "QComboBox QAbstractItemView {\n"
                                       "  border: 1px solid grey;\n"
                                       "  background: white;\n"
                                       "  selection-background-color: blue;\n"
                                       "}\n"
                                       "QComboBox {\n"
                                       "  background: red;\n"
                                       "}\n"
                                       "QListView{background-color: rgb(0, 255, 255)}")
        self.comboBox.setObjectName("comboBox")

        self.label_6 = QLabel(self.frame)
        self.label_6.setGeometry(QRect(100, 250, 391, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(243, 243, 243);\n"
                                      "background-color: rgb(2, 5, 3);\n"
                                      "border-radius:10px;\n"
                                      "background-color: rgb(63, 122, 138);\n"
                                      "color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")

        self.background.raise_()
        self.BrowseFile.raise_()
        self.label_8.raise_()
        self.optimizer_title_label.raise_()
        self.Process.raise_()
        self.Close.raise_()
        self.ExcelPath.raise_()
        self.Minimize.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.Alpha.raise_()
        self.LT_Adjustment.raise_()
        self.ReviewPeriod.raise_()
        self.label_6.raise_()
        self.comboBox.raise_()

        self.horizontalLayout_1.addWidget(self.frame)
        self.tabWidget.addTab(self.inv_tab, "")
    def setupCombineTab(self):
        self.combine_tab = QWidget()
        CT_font = QFont()
        self.combine_tab.setFont(CT_font)

        self.combine_tab.setStyleSheet("font-family: \"Trebuchet MS\";border:0px solid rgb(0,0,0);")
        self.combine_tab.setObjectName("CT_combine_tab")
        
        
        #.................................................................................................
        self.CTI_verticalLayout_1 = QVBoxLayout(self.combine_tab)
        self.CTI_verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.CTI_verticalLayout_1.setSpacing(0)
        self.CTI_verticalLayout_1.setObjectName("CTI_verticalLayout_1")
        self.CTI_frame = QFrame(self.inv_tab)
        self.CTI_frame.setMinimumSize(QSize(241, 0))
        self.CTI_frame.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                    "border-radius:10px")
        self.CTI_frame.setFrameShape(QFrame.StyledPanel)
        self.CTI_frame.setFrameShadow(QFrame.Raised)
        self.CTI_frame.setObjectName("CTI_frame")

        self.CTI_optimizer_title_label = QLabel(self.CTI_frame)
        self.CTI_optimizer_title_label.setGeometry(QRect(100, 20, 391, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.CTI_optimizer_title_label.setFont(font)
        self.CTI_optimizer_title_label.setAutoFillBackground(False)
        self.CTI_optimizer_title_label.setStyleSheet("color: rgb(243, 243, 243);\n"
                                                    "background-color: rgb(2, 5, 3);\n"
                                                    "border-radius:10px")
        self.CTI_optimizer_title_label.setFrameShape(QFrame.WinPanel)
        self.CTI_optimizer_title_label.setFrameShadow(QFrame.Raised)
        self.CTI_optimizer_title_label.setLineWidth(47)
        self.CTI_optimizer_title_label.setMidLineWidth(18)
        self.CTI_optimizer_title_label.setTextFormat(Qt.RichText)
        self.CTI_optimizer_title_label.setScaledContents(True)
        self.CTI_optimizer_title_label.setAlignment(Qt.AlignCenter)
        self.CTI_optimizer_title_label.setIndent(-1)
        self.CTI_optimizer_title_label.setObjectName("CTI_optimizer_title_label")

        self.CTI_BrowseFile = QPushButton(self.CTI_frame)
        self.CTI_BrowseFile.setGeometry(QRect(420, 244, 71, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CTI_BrowseFile.setFont(font)
        self.CTI_BrowseFile.setStyleSheet("color: rgb(243, 243, 243);\n"
                                         "border-color: rgb(243, 243, 243);\n"
                                         "background-color: rgb(2, 5, 3);\n"
                                         "border-left-radius:10px;\n"
                                         "background-color: rgb(63, 122, 138);\n"
                                         "hover {\n"
                                         "                background-color: rgb(0, 0, 138);\n"
                                         "                border-style: inset;\n"
                                         "            }")
        self.CTI_BrowseFile.setObjectName("CTI_BrowseFile")
        self.CTI_label_8 = QLabel(self.CTI_frame)
        self.CTI_label_8.setGeometry(QRect(100, 244, 334, 31))
        self.CTI_label_8.setStyleSheet("color: rgb(243, 243, 243);\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "border-radius:10px;\n"
                                      "background-color:rgb(63, 122, 138);\n"
                                      "")
        self.CTI_label_8.setText("")
        self.CTI_label_8.setObjectName("CTI_label_8")

        self.CTI_BrowseFile.setStyleSheet(
            """
            QPushButton {
                color: rgb(243, 243, 243);
        border-color: rgb(243, 243, 243);

        border-right-radius:10px;
        border-left-radius:1px;
        background-color: rgb(63, 122, 138);
            }
            }
            QPushButton:hover {
                color: rgb(63, 122, 138);
                background-color: rgb(243, 243, 243);
                border-style: inset;
            }
            QPushButton:pressed {
            color: rgb(243, 243, 243);
                background-color: rgb(63, 122, 138);
                border-style: inset;
            }
            """
        )


        self.CTI_Close = QPushButton(self.CTI_frame)
        self.CTI_Close.setGeometry(QRect(530, 20, 61, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.CTI_Close.setFont(font)
        self.CTI_Close.setStyleSheet("color: rgb(2, 5, 3);\n"
                                    "background-color: rgb(243, 243, 243);\n"
                                    "border-radius:10px")
        self.CTI_Close.setObjectName("CTI_Close")
        self.CTI_Minimize = QPushButton(self.CTI_frame)
        self.CTI_Minimize.setGeometry(QRect(520, 20, 41, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.CTI_Minimize.setFont(font)
        self.CTI_Minimize.setStyleSheet("color: rgb(243, 243, 243);\n"
                                       "background-color: rgb(2, 5, 3);\n"
                                       "border-radius:10px")
        self.CTI_Minimize.setObjectName("CTI_Minimize")

        self.CTI_ExcelPath = QLineEdit(self.CTI_frame)
        self.CTI_ExcelPath.setGeometry(QRect(110, 249, 301, 20))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CTI_ExcelPath.setFont(font)
        self.CTI_ExcelPath.setStyleSheet("border-radius:10px;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(149, 149, 149);\n"
                                        "font-family: \"Trebuchet MS\"")
        self.CTI_ExcelPath.setText("")
        self.CTI_ExcelPath.setObjectName("CTI_ExcelPath")
        self.CTI_background = QLabel(self.CTI_frame)
        self.CTI_background.setScaledContents(True)
        self.CTI_background.setGeometry(QRect(0, 0, 621, 550))
        self.CTI_background.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                         "border-radius:10px")
        self.CTI_background.setText("")
        self.CTI_background.setPixmap(QPixmap("files\\Background.jpg"))
        self.CTI_background.setObjectName("CTI_background")

        self.CTI_label_3 = QLabel(self.CTI_frame)
        self.CTI_label_3.setGeometry(QRect(100, 172, 391, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CTI_label_3.setFont(font)
        self.CTI_label_3.setStyleSheet("color: rgb(243, 243, 243);\n"
                                      "background-color: rgb(2, 5, 3);\n"
                                      "border-radius:10px;\n"
                                      "background-color: rgb(63, 122, 138);\n"
                                      "color: rgb(255, 255, 255);")
        self.CTI_label_3.setObjectName("CTI_label_3")
        self.CTI_label_4 = QLabel(self.CTI_frame)
        self.CTI_label_4.setGeometry(QRect(100, 136, 391, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CTI_label_4.setFont(font)
        self.CTI_label_4.setStyleSheet("color: rgb(243, 243, 243);\n"
                                      "background-color: rgb(2, 5, 3);\n"
                                      "border-radius:10px;\n"
                                      "background-color: rgb(63, 122, 138);\n"
                                      "color: rgb(255, 255, 255);")
        self.CTI_label_4.setObjectName("CTI_label_4")

        self.CTI_label_5 = QLabel(self.CTI_frame)
        self.CTI_label_5.setGeometry(QRect(100, 100, 391, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CTI_label_5.setFont(font)
        self.CTI_label_5.setStyleSheet("color: rgb(243, 243, 243);\n"
                                      "background-color: rgb(2, 5, 3);\n"
                                      "border-radius:10px;\n"
                                      "background-color: rgb(63, 122, 138);\n"
                                      "color: rgb(255, 255, 255);")
        self.CTI_label_5.setObjectName("CTI_label_5")

        self.CTI_Alpha = QLineEdit(self.CTI_frame)
        self.CTI_Alpha.setGeometry(QRect(250, 141, 231, 20))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Trebuchet MS")
        self.CTI_Alpha.setFont(font)
        self.CTI_Alpha.setStyleSheet("border-radius:10px;\n"
                                    "background-color: rgb(255, 255, 255);")
        self.CTI_Alpha.setInputMethodHints(Qt.ImhDigitsOnly)
        self.CTI_Alpha.setObjectName("CTI_Alpha")

        self.CTI_LT_Adjustment = QLineEdit(self.CTI_frame)
        self.CTI_LT_Adjustment.setGeometry(QRect(250, 105, 231, 20))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Trebuchet MS")
        self.CTI_LT_Adjustment.setFont(font)
        self.CTI_LT_Adjustment.setStyleSheet("border-radius:10px;\n"
                                            "background-color: rgb(255, 255, 255);")
        self.CTI_LT_Adjustment.setInputMethodHints(Qt.ImhDigitsOnly)
        self.CTI_LT_Adjustment.setObjectName("CTI_LT_Adjustment")

        self.CTI_ReviewPeriod = QLineEdit(self.CTI_frame)
        self.CTI_ReviewPeriod.setGeometry(QRect(250, 177, 231, 20))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Trebuchet MS")
        self.CTI_ReviewPeriod.setFont(font)
        self.CTI_ReviewPeriod.setStyleSheet("border-radius:10px;\n"
                                           "background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
        self.CTI_ReviewPeriod.setInputMethodHints(Qt.ImhDigitsOnly)
        self.CTI_ReviewPeriod.setObjectName("CTI_ReviewPeriod")

        self.CTI_comboBox = QComboBox(self.CTI_frame)
        self.CTI_comboBox.setGeometry(QRect(250, 213, 231, 22))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Trebuchet MS")
        self.CTI_comboBox.setFont(font)
        self.CTI_comboBox.setAutoFillBackground(False)
        self.CTI_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);\n"
                                       "QComboBox QAbstractItemView {\n"
                                       "  border: 1px solid grey;\n"
                                       "  background: white;\n"
                                       "  selection-background-color: blue;\n"
                                       "}\n"
                                       "QComboBox {\n"
                                       "  background: red;\n"
                                       "}\n"
                                       "QListView{background-color: rgb(0, 255, 255)}")
        self.CTI_comboBox.setObjectName("CTI_comboBox")

        self.CTI_label_6 = QLabel(self.CTI_frame)
        self.CTI_label_6.setGeometry(QRect(100, 208, 391, 31))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CTI_label_6.setFont(font)
        self.CTI_label_6.setStyleSheet("color: rgb(243, 243, 243);\n"
                                      "background-color: rgb(2, 5, 3);\n"
                                      "border-radius:10px;\n"
                                      "background-color: rgb(63, 122, 138);\n"
                                      "color: rgb(255, 255, 255);")
        self.CTI_label_6.setObjectName("CTI_label_6")

        self.CTI_background.raise_()
        self.CTI_BrowseFile.raise_()
        self.CTI_label_8.raise_()
        self.CTI_optimizer_title_label.raise_()
        # self.CTI_Process.raise_()
        self.CTI_Close.raise_()
        self.CTI_ExcelPath.raise_()
        self.CTI_Minimize.raise_()
        self.CTI_label_3.raise_()
        self.CTI_label_4.raise_()
        self.CTI_label_5.raise_()
        self.CTI_Alpha.raise_()
        self.CTI_LT_Adjustment.raise_()
        self.CTI_ReviewPeriod.raise_()
        self.CTI_label_6.raise_()
        self.CTI_comboBox.raise_()


        self.CTS_label_19 = QLabel(self.CTI_frame)
        self.CTS_label_19.setGeometry(QRect(100, 352, 391, 31))
        CTS_font = QFont()
        CTS_font.setPointSize(8)
        CTS_font.setBold(True)
        self.CTS_label_19.setFont(CTS_font)
        self.CTS_label_19.setStyleSheet("color: rgb(243, 243, 243);\n"
                                       "border-radius:10px;\n"
                                       "background-color: rgb(63, 122, 138);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font-family: \"Trebuchet MS\"")
        self.CTS_label_19.setObjectName("CTS_label_19")

        self.CTS_label_22 = QLabel(self.CTI_frame)
        self.CTS_label_22.setGeometry(QRect(100, 388, 391, 31))
        CTS_font = QFont()
        CTS_font.setPointSize(8)
        CTS_font.setBold(True)
        self.CTS_label_22.setFont(CTS_font)
        self.CTS_label_22.setStyleSheet("color: rgb(243, 243, 243);\n"
                                       "border-radius:10px;\n"
                                       "background-color: rgb(63, 122, 138);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font-family: \"Trebuchet MS\"")
        self.CTS_label_22.setObjectName("CTS_label_22")

        self.CTS_label_20 = QLabel(self.CTI_frame)
        self.CTS_label_20.setGeometry(QRect(100, 316, 391, 31))
        CTS_font = QFont()
        CTS_font.setPointSize(8)
        CTS_font.setBold(True)
        self.CTS_label_20.setFont(CTS_font)
        self.CTS_label_20.setStyleSheet("color: rgb(243, 243, 243);\n"
                                       "background-color: rgb(2, 5, 3);\n"
                                       "border-radius:10px;\n"
                                       "background-color: rgb(63, 122, 138);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font-family: \"Trebuchet MS\"")
        self.CTS_label_20.setObjectName("CTS_label_20")
        self.CTS_label_21 = QLabel(self.CTI_frame)
        self.CTS_label_21.setGeometry(QRect(100, 280, 391, 31))
        CTS_font = QFont()
        CTS_font.setPointSize(8)
        CTS_font.setBold(True)
        self.CTS_label_21.setFont(CTS_font)
        self.CTS_label_21.setStyleSheet("color: rgb(243, 243, 243);\n"
                                       "background-color: rgb(2, 5, 3);\n"
                                       "border-radius:10px;\n"
                                       "background-color: rgb(63, 122, 138);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font-family: \"Trebuchet MS\"")
        self.CTS_label_21.setObjectName("CTS_label_21")
        self.CTS_Simulation_period = QSpinBox(self.CTI_frame)
        self.CTS_Simulation_period.setGeometry(QRect(250, 285, 150, 22))
        CTS_font = QFont()
        CTS_font.setPointSize(8)
        CTS_font.setBold(False)
        self.CTS_Simulation_period.setFont(CTS_font)
        self.CTS_Simulation_period.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                                "border-radius:10px;\n"
                                                "background-color: rgb(243, 243, 243);;\n"
                                                "font-family: \"Trebuchet MS\";")
        self.CTS_Simulation_period.setMinimum(1)
        self.CTS_Simulation_period.setMaximum(10000)
        self.CTS_Simulation_period.setProperty("value", 1)
        self.CTS_Simulation_period.setObjectName("CTS_Simulation_period")

        self.CTS_simulation_duration_type = QComboBox(self.CTI_frame)
        self.CTS_simulation_duration_type.setGeometry(QRect(410, 285, 71, 22))
        CTS_font = QFont()
        CTS_font.setPointSize(8)
        CTS_font.setBold(False)
        CTS_font.setWeight(50)
        CTS_font.setFamily("Trebuchet MS")
        self.CTS_simulation_duration_type.setFont(CTS_font)
        self.CTS_simulation_duration_type.setAutoFillBackground(False)
        self.CTS_simulation_duration_type.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                       "color: rgb(0, 0, 0);\n"
                                                       "QComboBox QAbstractItemView {\n"
                                                       "  border: 1px solid grey;\n"
                                                       "  background: white;\n"
                                                       "  selection-background-color: blue;\n"
                                                       "}\n"
                                                       "QComboBox {\n"
                                                       "  background: red;\n"
                                                       "}\n"
                                                       "QListView{background-color: rgb(0, 255, 255)}")

        CTS_model = self.CTS_simulation_duration_type.model()
        for row, color in enumerate(['Months', 'Days']):
            self.CTS_simulation_duration_type.addItem(color)
            CTS_model.setData(CTS_model.index(row, 0), QColor('white'), Qt.BackgroundRole)

        self.CTS_simulation_duration_type.setObjectName("CTS_sumulation_duration_type")

        self.CTS_Consumption_Dev = QDoubleSpinBox(self.CTI_frame)
        self.CTS_Consumption_Dev.setGeometry(QRect(250, 321, 231, 22))
        CTS_font = QFont()
        CTS_font.setPointSize(8)
        self.CTS_Consumption_Dev.setFont(CTS_font)
        self.CTS_Consumption_Dev.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                              "border-radius:10px;\n"
                                              "background-color: rgb(243, 243, 243);\n"
                                              "font-family: \"Trebuchet MS\";")
        self.CTS_Consumption_Dev.setMaximum(200)
        self.CTS_Consumption_Dev.setSingleStep(1)
        self.CTS_Consumption_Dev.setObjectName("CTS_Consumption_Dev")
        self.CTS_Process_1 = QPushButton(self.CTI_frame)
        self.CTS_Process_1.setGeometry(QRect(230, 496, 131, 31))
        CTS_font = QFont()
        CTS_font.setFamily("Trebuchet MS")
        CTS_font.setPointSize(8)
        CTS_font.setBold(False)
        CTS_font.setWeight(50)
        self.CTS_Process_1.setFont(CTS_font)
        self.CTS_Process_1.setObjectName("CTS_Process_1")

        self.CTS_Process_1.setStyleSheet(
            """
            QPushButton {
                color: rgb(243, 243, 243);
        border-color: rgb(243, 243, 243);
        border-left-radius:10px;
        background-color: rgb(63, 122, 138);
            }
            }
            QPushButton:hover {
                color: rgb(63, 122, 138);
                background-color: rgb(243, 243, 243);
                border-style: inset;
            }
            QPushButton:pressed {
            color: rgb(243, 243, 243);
                background-color: rgb(63, 122, 138);
                border-style: inset;
            }
            """
        )

        self.CTS_BrowseFile_1 = QPushButton(self.CTI_frame)
        self.CTS_BrowseFile_1.setGeometry(QRect(420, 460, 71, 31))
        CTS_font = QFont()
        CTS_font.setFamily("Trebuchet MS")
        CTS_font.setPointSize(8)
        CTS_font.setBold(False)
        CTS_font.setWeight(50)
        self.CTS_BrowseFile_1.setFont(CTS_font)
        self.CTS_BrowseFile_1.setStyleSheet("color: rgb(243, 243, 243);\n"
                                           "border-color: rgb(243, 243, 243);\n"
                                           "background-color: rgb(2, 5, 3);\n"
                                           "border-left-radius:10px;\n"
                                           "background-color: rgb(63, 122, 138);\n"
                                           "hover {\n"
                                           "                background-color: rgb(0, 0, 138);\n"
                                           "                border-style: inset;\n"
                                           "            }")
        self.CTS_BrowseFile_1.setObjectName("CTS_BrowseFile_1")

        self.CTS_BrowseFile_1.setStyleSheet(
            """
            QPushButton {
                color: rgb(243, 243, 243);
                border-color: rgb(243, 243, 243);
                border-left-radius:10px;
                background-color: rgb(63, 122, 138);
            }
            QPushButton:hover {
                color: rgb(63, 122, 138);
                background-color: rgb(243, 243, 243);
                border-style: inset;
            }
            QPushButton:pressed {
                color: rgb(243, 243, 243);
                background-color: rgb(63, 122, 138);
                border-style: inset;
            }
            """
        )

        self.CTS_label_23 = QLabel(self.CTI_frame)
        self.CTS_label_23.setGeometry(QRect(100, 460, 334, 31))
        self.CTS_label_23.setStyleSheet("color: rgb(243, 243, 243);\n"
                                       "border-color: rgb(255, 255, 255);\n"
                                       "border-radius:10px;\n"
                                       "background-color: rgb(63, 122, 138);\n"
                                       "")
        self.CTS_label_23.setText("")
        self.CTS_label_23.setObjectName("CTS_label_23")

        self.CTS_ExcelPath_1 = QLineEdit(self.CTI_frame)
        self.CTS_ExcelPath_1.setGeometry(QRect(110, 465, 301, 20))
        font = QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.CTS_ExcelPath_1.setFont(font)
        self.CTS_ExcelPath_1.setStyleSheet("border-radius:10px;\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "color: rgb(149, 149, 149);\n"
                                          "font-family: \"Trebuchet MS\"")
        self.CTS_ExcelPath_1.setObjectName("CTS_ExcelPath_1")



        self.CTS_Remove_Negs = QCheckBox(self.CTI_frame)
        self.CTS_Remove_Negs.setGeometry(QRect(355, 393, 21, 21))
        font = QFont()
        font.setPointSize(8)
        self.CTS_Remove_Negs.setFont(font)
        self.CTS_Remove_Negs.setStyleSheet("color: rgb(243, 243, 243);\n"
                                          "background-color: rgb(2, 5, 3);\n"
                                          "border-radius:0px;\n"
                                          "background-color: rgb(63, 122, 138);\n"
                                          "font-family: \"Trebuchet MS\";")
        self.CTS_Remove_Negs.setObjectName("CTS_Count_Negs")

        self.CTS_price = QDoubleSpinBox(self.CTI_frame)
        self.CTS_price.setGeometry(QRect(250, 357, 231, 20))
        font = QFont()
        font.setPointSize(8)
        self.CTS_price.setFont(font)
        self.CTS_price.setStyleSheet("background-color: rgb(23, 24, 26);\n"
                                    "border-radius:10px;\n"
                                    "background-color: rgb(243, 243, 243);\n"
                                    "font-family: \"Trebuchet MS\";")
        self.CTS_price.setMinimum(1.0)
        self.CTS_price.setSingleStep(0.01)
        self.CTS_price.setProperty("value", 1.0)
        self.CTS_price.setObjectName("CTS_price")

        self.CTS_label_25 = QLabel(self.CTI_frame)
        self.CTS_label_25.setGeometry(QRect(100, 424, 391, 31))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.CTS_label_25.setFont(font)
        self.CTS_label_25.setStyleSheet("color: rgb(243, 243, 243);\n"
                                       "border-radius:10px;\n"
                                       "background-color: rgb(63, 122, 138);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font-family: \"Trebuchet MS\"")
        self.CTS_label_25.setObjectName("CTS_label_22")

        self.CTS_Round_LT = QCheckBox(self.CTI_frame)
        self.CTS_Round_LT.setGeometry(QRect(355, 429, 21, 21))
        font = QFont()
        font.setPointSize(8)
        self.CTS_Round_LT.setFont(font)
        self.CTS_Round_LT.setStyleSheet("color: rgb(243, 243, 243);\n"
                                       "background-color: rgb(2, 5, 3);\n"
                                       "border-radius:0px;\n"
                                       "background-color: rgb(63, 122, 138);\n"
                                       "font-family: \"Trebuchet MS\";")
        self.CTS_Round_LT.setObjectName("CTS_Count_Negs")

        self.CTI_verticalLayout_1.addWidget(self.CTI_frame)
        self.tabWidget.addTab(self.combine_tab, "")
    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inventory Application"))

        self.optimizer_title_label.setText(_translate("MainWindow", "Inventory Optimizer"))
        self.BrowseFile.setText(_translate("MainWindow", "Browse"))
        self.Process.setText(_translate("MainWindow", "Process"))
        self.Minimize.setText(_translate("MainWindow", "M"))
        self.Close.setText(_translate("MainWindow", "     X"))
        self.ExcelPath.setPlaceholderText(_translate("MainWindow", "   Browse Excel"))
        self.label_3.setText(_translate("MainWindow", "  Review Period"))
        self.label_4.setText(_translate("MainWindow", "  Service Level"))
        self.label_5.setText(_translate("MainWindow", "  Lead Time Adjustment"))
        self.Alpha.setPlaceholderText(_translate("MainWindow", "  0-1"))
        self.LT_Adjustment.setPlaceholderText(_translate("MainWindow", "  Days"))
        self.ReviewPeriod.setPlaceholderText(_translate("MainWindow", "  Months"))
        self.label_6.setText(_translate("MainWindow", " Benchmark"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inv_tab), _translate("MainWindow", "    Inventory    "))
        self.label_19.setText(_translate("MainWindow", "  Price/Unit (if NA in File)"))
        self.label_22.setText(_translate("MainWindow", "  Remove Negative(s)"))
        self.label_25.setText(_translate("MainWindow", "  Round Lead Time"))
        self.label_20.setText(_translate("MainWindow", "  Consumption Deviation (%)"))
        self.label_21.setText(_translate("MainWindow", "  Simulation Period"))
        self.Process_1.setText(_translate("MainWindow", "Process"))
        self.BrowseFile_1.setText(_translate("MainWindow", "Browse"))
        self.ExcelPath_1.setPlaceholderText(_translate("MainWindow", "   Browse Excel"))
        self.simulation_title_label.setText(_translate("MainWindow", "Inventory Simulation"))
        self.Close_1.setText(_translate("MainWindow", "     X"))
        self.Minimize_1.setText(_translate("MainWindow", "M"))
        self.Remove_Negs.setText(_translate("MainWindow", ""))
        self.Round_LT.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sim_tab), _translate("MainWindow", "    Simulation    "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.combine_tab), _translate("MainWindow", "    Both   "))







        self.CTI_optimizer_title_label.setText(_translate("MainWindow", "Inventory Optimizer & Simulation"))
        self.CTI_BrowseFile.setText(_translate("MainWindow", "Browse"))
        self.CTI_Minimize.setText(_translate("MainWindow", "M"))
        self.CTI_Close.setText(_translate("MainWindow", "     X"))
        self.CTI_ExcelPath.setPlaceholderText(_translate("MainWindow", "   Browse Inventory Input Excel"))
        self.CTI_label_3.setText(_translate("MainWindow", "  Review Period"))
        self.CTI_label_4.setText(_translate("MainWindow", "  Service Level"))
        self.CTI_label_5.setText(_translate("MainWindow", "  Lead Time Adjustment"))
        self.CTI_Alpha.setPlaceholderText(_translate("MainWindow", "  0-1"))
        self.CTI_LT_Adjustment.setPlaceholderText(_translate("MainWindow", "  Days"))
        self.CTI_ReviewPeriod.setPlaceholderText(_translate("MainWindow", "  Months"))
        self.CTI_label_6.setText(_translate("MainWindow", " Benchmark"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inv_tab),
                                     _translate("MainWindow", "    Inventory    "))
        self.CTS_label_19.setText(_translate("MainWindow", "  Price/Unit (if NA in File)"))
        self.CTS_label_22.setText(_translate("MainWindow", "  Remove Negative(s)"))
        self.CTS_label_25.setText(_translate("MainWindow", "  Round Lead Time"))
        self.CTS_label_20.setText(_translate("MainWindow", "  Consumption Deviation (%)"))
        self.CTS_label_21.setText(_translate("MainWindow", "  Simulation Period"))
        self.CTS_Process_1.setText(_translate("MainWindow", "Process"))
        self.CTS_BrowseFile_1.setText(_translate("MainWindow", "Browse"))
        self.CTS_ExcelPath_1.setPlaceholderText(_translate("MainWindow", "   Browse Simulation Input Excel"))
        self.CTS_Remove_Negs.setText(_translate("MainWindow", ""))
        self.CTS_Round_LT.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sim_tab),
                                     _translate("MainWindow", "    Simulation    "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.combine_tab),
                                     _translate("MainWindow", "    Both   "))