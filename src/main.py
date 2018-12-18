from math_module import calculate
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window (WIP).ui', self)
        self.digit_1.clicked.connect(self.add_digit_1)
        self.digit_2.clicked.connect(self.add_digit_2)
        self.digit_3.clicked.connect(self.add_digit_3)
        self.digit_4.clicked.connect(self.add_digit_4)
        self.digit_5.clicked.connect(self.add_digit_5)
        self.digit_6.clicked.connect(self.add_digit_6)
        self.digit_7.clicked.connect(self.add_digit_7)
        self.digit_8.clicked.connect(self.add_digit_8)
        self.digit_9.clicked.connect(self.add_digit_9)
        self.digit_0.clicked.connect(self.add_digit_0)
        self.func_plus.clicked.connect(self.add_func_plus)
        self.func_minus.clicked.connect(self.add_func_minus)
        self.func_div.clicked.connect(self.add_func_div)
        self.func_mult.clicked.connect(self.add_func_mult)
        self.func_int_div.clicked.connect(self.add_func_int_div)
        self.func_rem.clicked.connect(self.add_func_rem)
        self.func_sqrt.clicked.connect(self.add_func_sqrt)
        self.func_degr.clicked.connect(self.add_func_degr)
        self.func_sin.clicked.connect(self.add_func_sin)
        self.func_cos.clicked.connect(self.add_func_cos)
        self.func_tg.clicked.connect(self.add_func_tg)
        self.func_ctg.clicked.connect(self.add_func_ctg)
        self.func_arcsin.clicked.connect(self.add_func_arcsin)
        self.func_arccos.clicked.connect(self.add_func_arccos)
        self.func_arctg.clicked.connect(self.add_func_arctg)
        self.func_arcctg.clicked.connect(self.add_func_arcctg)
        self.func_log10.clicked.connect(self.add_func_log10)
        self.func_log2.clicked.connect(self.add_func_log2)
        self.func_pi.clicked.connect(self.add_func_pi)
        self.func_e.clicked.connect(self.add_func_e)
        self.func_abs.clicked.connect(self.add_func_abs)
        self.var_x.clicked.connect(self.add_x)
        self.dot.clicked.connect(self.add_dot)
        self.func_left_bracket.clicked.connect(self.add_left_bracket)
        self.func_right_bracket.clicked.connect(self.add_right_bracket)
        self.delete_2.clicked.connect(self.delete_f)  # I don't know, why '_2'.
        self.calculate.clicked.connect(self.calculate_f)

    def add_digit_1(self):  # Add a digit/func to expression.
        self.expression.setText(self.expression.text() + '1')

    def add_digit_2(self):
        self.expression.setText(self.expression.text() + '2')

    def add_digit_3(self):
        self.expression.setText(self.expression.text() + '3')

    def add_digit_4(self):
        self.expression.setText(self.expression.text() + '4')

    def add_digit_5(self):
        self.expression.setText(self.expression.text() + '5')

    def add_digit_6(self):
        self.expression.setText(self.expression.text() + '6')

    def add_digit_7(self):
        self.expression.setText(self.expression.text() + '7')

    def add_digit_8(self):
        self.expression.setText(self.expression.text() + '8')

    def add_digit_9(self):
        self.expression.setText(self.expression.text() + '9')

    def add_digit_0(self):
        self.expression.setText(self.expression.text() + '0')

    def add_func_plus(self):
        self.expression.setText(self.expression.text() + '+')

    def add_func_minus(self):
        self.expression.setText(self.expression.text() + '-')

    def add_func_div(self):
        self.expression.setText(self.expression.text() + '/')

    def add_func_mult(self):
        self.expression.setText(self.expression.text() + '*')

    def add_func_int_div(self):
        self.expression.setText(self.expression.text() + '//')

    def add_func_rem(self):
        self.expression.setText(self.expression.text() + '%')

    def add_func_sqrt(self):
        self.expression.setText(self.expression.text() + 'sqrt(')

    def add_func_degr(self):
        self.expression.setText(self.expression.text() + '**')

    def add_func_sin(self):
        self.expression.setText(self.expression.text() + 'sin(')

    def add_func_cos(self):
        self.expression.setText(self.expression.text() + 'cos(')

    def add_func_tg(self):
        self.expression.setText(self.expression.text() + 'tg(')

    def add_func_ctg(self):
        self.expression.setText(self.expression.text() + 'ctg(')

    def add_func_arcsin(self):
        self.expression.setText(self.expression.text() + 'arcsin(')

    def add_func_arccos(self):
        self.expression.setText(self.expression.text() + 'arccos(')

    def add_func_arctg(self):
        self.expression.setText(self.expression.text() + 'arctg(')

    def add_func_arcctg(self):
        self.expression.setText(self.expression.text() + 'arcctg(')

    def add_func_log10(self):
        self.expression.setText(self.expression.text() + 'log10(')

    def add_func_log2(self):
        self.expression.setText(self.expression.text() + 'log2(')

    def add_func_pi(self):
        self.expression.setText(self.expression.text() + 'pi')

    def add_func_e(self):
        self.expression.setText(self.expression.text() + 'e')

    def add_func_abs(self):
        self.expression.setText(self.expression.text() + 'abs(')

    def add_dot(self):
        self.expression.setText(self.expression.text() + '.')

    def add_left_bracket(self):
        self.expression.setText(self.expression.text() + '(')

    def add_right_bracket(self):
        self.expression.setText(self.expression.text() + ')')

    def add_x(self):
        self.expression.setText(self.expression.text() + 'x')

    def delete_f(self):
        self.expression.setText(self.expression.text()[:-1])
        while len(self.expression.text()) > 0 and self.expression.text()[-1].isalpha():
            self.expression.setText(self.expression.text()[:-1])

    def calculate_f(self):
        try:
            resolution = 5000
            start = int(self.start.text())
            end = int(self.end.text())
            top = 0
            bottom = 0
            top_lim = 100
            bot_lim = -100
            graphics = [[]]  # There can be many graphics. For example, y = 1/x.
            x_positions = [[]]
            for i in range(resolution + 1):
                try:
                    graphics[-1].append(calculate(self.expression.text(), start + (end - start) / resolution * i))
                    x_positions[-1].append(start + (end - start) / resolution * i)

                    if graphics[-1][-1] > top_lim or graphics[-1][-1] < bot_lim:
                        del graphics[-1][-1]
                        del x_positions[-1][-1]
                        continue

                    if graphics[-1][-1] > top:
                        top = graphics[-1][-1]
                    if graphics[-1][-1] < bottom:
                        bottom = graphics[-1][-1]

                    if len(graphics[-1]) > 1 and graphics[-1][-1] * graphics[-1][-2] < 0 and abs(
                            graphics[-1][-1] - graphics[-1][-2]) > (
                            1.5 * min(abs(graphics[-1][-2]), abs(graphics[-1][-1]))):
                        raise ValueError
                except Exception:
                    if len(graphics[-1]) > 0:
                        x_positions.append([x_positions[-1][-1]])
                        graphics.append([graphics[-1][-1]])
                        del graphics[-2][-1]
                        del x_positions[-2][-1]

            print(graphics)
            print(x_positions)
            self.graphic.clear()
            for x, y in zip(x_positions, graphics):
                self.graphic.plot(x, y)
            self.graphic.plot([start - abs(start) * 0.05, end + abs(end) * 0.05], [0, 0], pen='r')
            self.graphic.plot([0, 0], [bottom - 10, top + 10], pen='r')
        except Exception:
            print('Draw error.')

    def run(self):
        pass


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
