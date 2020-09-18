from pywinauto.application import Application
from pywinauto import Desktop
import time


class calculations:

    def __init__(self):
        self.app = Application(backend="uia").start('calc.exe')

    def add(self, a, b):
        self.calcdlg = Desktop(backend="uia").Calculator
        self.calcdlg.wait('visible')
        self.calcdlg.type_keys(a + b)
        time.sleep(4)
        #self.calcdlg.type_keys("C")
        self.calcdlg.children()[1].children()[1].children()[3].descendants()[2].click()
        self.calcdlg.print_control_identifiers()

    def multiply(self, a, b):
        self.calcdlg.type_keys(a * b)
        self.calcdlg.print_control_identifiers()
        self.calcdlg.children()[1].children()[1].children()[3].descendants()[2].click()

    def operations(self):
        self.calcdlg.minimize()
        Desktop(backend="uia").window(title='Calculator', visible_only=False).restore()
        self.calcdlg.close()


if __name__ == '__main__':
    c = calculations()
    c.add(2, 3)
    c.multiply(5, 5)
