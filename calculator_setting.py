from pywinauto import Desktop, Application


def run_calculator():
    app = Application().start('calc.exe')
    dlg = Desktop(backend='uia').Calculator
    return dlg
