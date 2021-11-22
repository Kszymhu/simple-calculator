"""Contains the `main` function. Run this file if you want to experience
the pure joy of having your calculations done for you.
"""
import sys

from PyQt5 import QtWidgets

from logic.rpn_generator import generate_rpn
from logic.rpn_solver import calculate_rpn
from logic.tokenizer import tokenize

from gui.calculator_window import Ui_MainWindow

def update_text_box(box: QtWidgets.QTextBrowser, stack: list[str]) -> None:
    result = [x for x in "".join(stack) if x != " "]

    box.setText("".join(result))

def calculate(input_stack: list[str]):
    tokens_raw = "".join(input_stack).split(" ")
    tokens = tokenize(tokens_raw)
    rpn = generate_rpn(tokens)
    result = calculate_rpn(rpn)
    input_stack.clear()
    input_stack.append(str(result))
    

def main():
    """Calculator entry point."""

    application = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    input_stack = []
    ui.button_0.clicked.connect(lambda x: input_stack.append("0"))
    ui.button_0.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_1.clicked.connect(lambda x: input_stack.append("1"))
    ui.button_1.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_2.clicked.connect(lambda x: input_stack.append("2"))
    ui.button_2.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_3.clicked.connect(lambda x: input_stack.append("3"))
    ui.button_3.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_4.clicked.connect(lambda x: input_stack.append("4"))
    ui.button_4.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_5.clicked.connect(lambda x: input_stack.append("5"))
    ui.button_5.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_6.clicked.connect(lambda x: input_stack.append("6"))
    ui.button_6.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_7.clicked.connect(lambda x: input_stack.append("7"))
    ui.button_7.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_8.clicked.connect(lambda x: input_stack.append("8"))
    ui.button_8.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_9.clicked.connect(lambda x: input_stack.append("9"))
    ui.button_9.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_pi.clicked.connect(lambda x: input_stack.append("pi"))
    ui.button_pi.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_e.clicked.connect(lambda x: input_stack.append("e"))
    ui.button_e.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_period.clicked.connect(lambda x: input_stack.append("."))
    ui.button_period.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_left_parenthesis.clicked.connect(lambda x: input_stack.append("( "))
    ui.button_left_parenthesis.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_right_parenthesis.clicked.connect(lambda x: input_stack.append(" )"))
    ui.button_right_parenthesis.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_plus.clicked.connect(lambda x: input_stack.append(" + "))
    ui.button_plus.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_minus.clicked.connect(lambda x: input_stack.append(" - "))
    ui.button_minus.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_asterisk.clicked.connect(lambda x: input_stack.append(" * "))
    ui.button_asterisk.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_slash.clicked.connect(lambda x: input_stack.append(" / "))
    ui.button_slash.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_power.clicked.connect(lambda x: input_stack.append(" ^ "))
    ui.button_power.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_mod.clicked.connect(lambda x: input_stack.append(" % "))
    ui.button_mod.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_root.clicked.connect(lambda x: input_stack.append(" root "))
    ui.button_root.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_log.clicked.connect(lambda x: input_stack.append(" log "))
    ui.button_log.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_clear.clicked.connect(lambda x: input_stack.clear())
    ui.button_clear.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_backspace.clicked.connect(lambda x: input_stack.pop() if len(input_stack) > 0 else None)
    ui.button_backspace.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    ui.button_equals.clicked.connect(lambda x: calculate(input_stack))
    ui.button_equals.clicked.connect(lambda x: update_text_box(ui.expression_browser, input_stack))

    main_window.show()

    sys.exit(application.exec_())

if __name__ == "__main__":
    main()
