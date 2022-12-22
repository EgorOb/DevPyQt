
from PySide2 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()

    def initUi(self):
        main_frame = QtWidgets.QVBoxLayout()
        main_frame.addLayout(self.get_frame_push_button())
        main_frame.addLayout(self.get_frame_tool_button())
        self.setLayout(main_frame)

    def get_frame_push_button(self):

        frame_button = QtWidgets.QHBoxLayout()
        self.button1 = QtWidgets.QPushButton("clicked")
        self.button2 = QtWidgets.QPushButton("pressed")
        self.button3 = QtWidgets.QPushButton("released")
        self.button4 = QtWidgets.QPushButton("toggled")
        self.button4.setCheckable(True)
        self.lableButton = QtWidgets.QLabel("Заглушка")
        frame_button.addWidget(self.button1)
        frame_button.addWidget(self.button2)
        frame_button.addWidget(self.button3)
        frame_button.addWidget(self.button4)
        frame_button.addWidget(self.lableButton)

        return frame_button

    def get_frame_tool_button(self):
        frame_button = QtWidgets.QHBoxLayout()
        self.button1_tool = QtWidgets.QToolButton()
        self.button1_tool.setText("clicked")
        self.button2_tool = QtWidgets.QToolButton()
        self.button2_tool.setText("pressed")
        self.button3_tool = QtWidgets.QToolButton()
        self.button3_tool.setText("released")
        self.button4_tool = QtWidgets.QToolButton()
        self.button4_tool.setText("toggled")
        self.button4_tool.setCheckable(True)
        self.lableButtonTool = QtWidgets.QLabel("Заглушка")
        frame_button.addWidget(self.button1_tool)
        frame_button.addWidget(self.button2_tool)
        frame_button.addWidget(self.button3_tool)
        frame_button.addWidget(self.button4_tool)
        frame_button.addWidget(self.lableButtonTool)
        return frame_button

    def initSignals(self):
        self.button1.clicked.connect(lambda: self.clicked_button(self.lableButton))
        self.button2.pressed.connect(lambda: self.pressed_button(self.lableButton))
        self.button3.released.connect(lambda: self.released_button(self.lableButton))
        self.button4.released.connect(lambda: self.toggled_button(self.lableButton, self.button4))
        self.button1_tool.clicked.connect(lambda: self.clicked_button(self.lableButtonTool))
        self.button2_tool.pressed.connect(lambda: self.pressed_button(self.lableButtonTool))
        self.button3_tool.released.connect(lambda: self.released_button(self.lableButtonTool))
        self.button4_tool.released.connect(lambda: self.toggled_button(self.lableButtonTool, self.button4_tool))

    def clicked_button(self, label: QtWidgets.QLabel):
        label.setText("Нажали и отпустили")

    def pressed_button(self, label: QtWidgets.QLabel):
        label.setText("Нажали")

    def released_button(self, label: QtWidgets.QLabel):
        label.setText("Отпустили")

    def toggled_button(self, label: QtWidgets.QLabel, button: QtWidgets.QPushButton):
        label.setText(str(button.isChecked()))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec_()