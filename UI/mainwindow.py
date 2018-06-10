# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\workspace\pycharm_proj\PythonDiff\UI\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from config import ConfigManager


class Ui_MainWindow(object):
    def configInit(self):
        config = ConfigManager("config/default.ini")
        self.title = config.config_get("project", "title")
        self.version = config.config_get("project", "version")

        self.shortcut_new_file_compare = config.config_get("shortcut", "new_file_compare")
        self.shortcut_new_dir_compare = config.config_get("shortcut", "new_dir_compare")
        self.shortcut_choose_left = config.config_get("shortcut", "choose_left")
        self.shortcut_choose_right = config.config_get("shortcut", "choose_right")
        self.shortcut_settings = config.config_get("shortcut", "settings")
        self.shortcut_exit = config.config_get("shortcut", "exit")

        self.shortcut_compare = config.config_get("shortcut", "compare")
        self.shortcut_copy_to_left = config.config_get("shortcut", "copy_to_left")
        self.shortcut_copy_to_right = config.config_get("shortcut", "copy_to_right")

        self.shortcut_next_diff = config.config_get("shortcut", "next_diff")
        self.shortcut_pre_diff = config.config_get("shortcut", "pre_diff")

        self.shortcut_help = config.config_get("shortcut", "help")

    def menubarInit(self, menubar):
        ### MENU FILE
        fileMenu = menubar.addMenu('&File')
        # new file compare
        submenu = QtWidgets.QMenu('&New File Compare', menubar)
        # file type : bin
        binSubMenu = QtWidgets.QAction(QtGui.QIcon(''), '&Bin File', self)
        binSubMenu.setStatusTip('compare bin files')
        binSubMenu.triggered.connect(lambda: self.action_test("binSubMenu"))
        submenu.addAction(binSubMenu)
        # file type : hex
        hexSubMenu = QtWidgets.QAction(QtGui.QIcon(''), '&Hex File', self)
        hexSubMenu.setStatusTip('compare hex files')
        hexSubMenu.triggered.connect(lambda: self.action_test("hexSubMenu"))
        submenu.addAction(hexSubMenu)
        # file type : text
        textSubMenu = QtWidgets.QAction(QtGui.QIcon(''), '&Text File', self)
        textSubMenu.setStatusTip('compare text files')
        textSubMenu.triggered.connect(lambda: self.action_test("textSubMenu"))
        submenu.addAction(textSubMenu)

        fileMenu.addMenu(submenu)
        # new dir compare
        newDirCompareAction = QtWidgets.QAction(QtGui.QIcon('new_dir_compare.png'), 'New &Dir Compare', self)
        newDirCompareAction.setShortcut(self.shortcut_new_dir_compare)
        newDirCompareAction.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        newDirCompareAction.setStatusTip('Start a new dir compare')
        newDirCompareAction.triggered.connect(lambda: self.action_test("newDirCompareAction"))
        fileMenu.addAction(newDirCompareAction)
        fileMenu.addSeparator()
        # choose left file/dir
        chooseLeftCompareAction = QtWidgets.QAction(QtGui.QIcon('choose_left.png'), 'Choose &Left File/Dir', self)
        chooseLeftCompareAction.setShortcut(self.shortcut_choose_left)
        chooseLeftCompareAction.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        chooseLeftCompareAction.setStatusTip('Choose left file or dir to compare')
        chooseLeftCompareAction.triggered.connect(lambda: self.action_test("chooseLeftCompareAction"))
        fileMenu.addAction(chooseLeftCompareAction)
        # choose right file/dir
        chooseRightCompareAction = QtWidgets.QAction(QtGui.QIcon('choose_right.png'), 'Choose &Right File/Dir', self)
        chooseRightCompareAction.setShortcut(self.shortcut_choose_right)
        chooseRightCompareAction.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        chooseRightCompareAction.setStatusTip('Choose right file or dir to compare')
        chooseRightCompareAction.triggered.connect(lambda: self.action_test("chooseRightCompareAction"))
        fileMenu.addAction(chooseRightCompareAction)
        fileMenu.addSeparator()
        # settings
        settingsAction = QtWidgets.QAction(QtGui.QIcon('settings.png'), '&Settings', self)
        settingsAction.setShortcut(self.shortcut_settings)
        settingsAction.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        settingsAction.setStatusTip('Settings')
        settingsAction.triggered.connect(lambda: self.action_test("settingsAction"))
        fileMenu.addAction(settingsAction)
        fileMenu.addSeparator()
        # exit
        exitAction = QtWidgets.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        #exitAction.setShortcut(self.shortcut_exit)
        exitAction.setShortcut(self.shortcut_exit)
        exitAction.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtWidgets.qApp.quit)
        fileMenu.addAction(exitAction)

        ### ACTION
        actionMenu = menubar.addMenu('A&ction')
        # compare
        compareAction = QtWidgets.QAction(QtGui.QIcon('compare.png'), '&Compare', self)
        compareAction.setShortcut(self.shortcut_compare)
        compareAction.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        compareAction.setStatusTip('Start compare')
        compareAction.triggered.connect(lambda: self.action_test("compareAction"))
        actionMenu.addAction(compareAction)
        # copy to left
        copyToLeftAction = QtWidgets.QAction(QtGui.QIcon('copy_to_left.png'), 'Copy to &Left', self)
        copyToLeftAction.setShortcut(self.shortcut_copy_to_left)
        copyToLeftAction.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        copyToLeftAction.setStatusTip('Copy to left')
        copyToLeftAction.triggered.connect(lambda: self.action_test("copyToLeftAction"))
        actionMenu.addAction(copyToLeftAction)
        # copy to right
        copyToRightAction = QtWidgets.QAction(QtGui.QIcon('copy_to_right.png'), 'Copy to &Right', self)
        copyToRightAction.setShortcut(self.shortcut_copy_to_right)
        copyToRightAction.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        copyToRightAction.setStatusTip('Copy to right')
        copyToRightAction.triggered.connect(lambda: self.action_test("copyToRightAction"))
        actionMenu.addAction(copyToRightAction)

        ### SEARCH
        searchMenu = menubar.addMenu('&Search')
        # find next diff
        nextDiffAction = QtWidgets.QAction(QtGui.QIcon('next_diff.png'), 'Find &Next Diff', self)
        nextDiffAction.setShortcut(self.shortcut_next_diff)
        nextDiffAction.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        nextDiffAction.setStatusTip('find next diff')
        nextDiffAction.triggered.connect(lambda: self.action_test("nextDiffAction"))
        searchMenu.addAction(nextDiffAction)
        # find pre diff
        preDiffAction = QtWidgets.QAction(QtGui.QIcon('pre_diff.png'), 'Find &Pre Diff', self)
        preDiffAction.setShortcut(self.shortcut_pre_diff)
        preDiffAction.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        preDiffAction.setStatusTip('find pre diff')
        preDiffAction.triggered.connect(lambda: self.action_test("preDiffAction"))
        searchMenu.addAction(preDiffAction)

        ### VIEW
        viewMenu = menubar.addMenu('&View')
        # exchange sides
        exchangeAction = QtWidgets.QAction(QtGui.QIcon(''), '&Exchange Sides', self)
        exchangeAction.setStatusTip('exchange windows')
        exchangeAction.triggered.connect(lambda: self.action_test("exchangeAction"))
        viewMenu.addAction(exchangeAction)
        viewMenu.addSeparator()
        # show diff only
        showDiffAction = QtWidgets.QAction(QtGui.QIcon(''), 'Show &Diff Only', self)
        showDiffAction.setStatusTip('only show diff')
        showDiffAction.triggered.connect(lambda: self.action_test("showDiffAction"))
        viewMenu.addAction(showDiffAction)
        # show same only
        showSameAction = QtWidgets.QAction(QtGui.QIcon(''), 'Show &Same Only', self)
        showSameAction.setStatusTip('only show same')
        showSameAction.triggered.connect(lambda: self.action_test("showSameAction"))
        viewMenu.addAction(showSameAction)
        # show all
        showAllAction = QtWidgets.QAction(QtGui.QIcon(''), 'Show &All', self)
        showAllAction.setStatusTip('show all')
        showAllAction.triggered.connect(lambda: self.action_test("showAllAction"))
        viewMenu.addAction(showAllAction)

        ### About
        aboutMenu = menubar.addMenu('&About')
        # help
        helpAction = QtWidgets.QAction(QtGui.QIcon('help.png'), '&Help', self)
        helpAction.setShortcut(self.shortcut_help)
        helpAction.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        helpAction.setStatusTip('help')
        helpAction.triggered.connect(lambda: self.action_test("helpAction"))
        aboutMenu.addAction(helpAction)
        aboutMenu.addSeparator()
        # check update
        checkUpdateAction = QtWidgets.QAction(QtGui.QIcon('check_update.png'), '&Check Update', self)
        checkUpdateAction.setStatusTip('check soft update')
        checkUpdateAction.triggered.connect(lambda: self.action_test("checkUpdateAction"))
        aboutMenu.addAction(checkUpdateAction)
        aboutMenu.addSeparator()
        # about
        aboutUsAction = QtWidgets.QAction(QtGui.QIcon('about.png'), '&About us ...', self)
        aboutUsAction.setStatusTip('about')
        aboutUsAction.triggered.connect(lambda: self.action_test("aboutUsAction"))
        aboutMenu.addAction(aboutUsAction)

    def action_test(self, action):
        print("action test: %s" % action)

    def setupUi(self, MainWindow):
        self.configInit()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubarInit(self.menubar)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "PythonDiff"))
        MainWindow.setWindowTitle(_translate("MainWindow", self.title + '  ' + self.version))
