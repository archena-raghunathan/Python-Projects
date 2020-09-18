from pywinauto.application import Application
from pywinauto import Desktop
import time
from pathlib import Path


class notepadoperations:

    def __init__(self):
        self.app = Application().start('Notepad.exe')


    def type_contents(self):
        time.sleep(3)
        self.app.Notepad.edit.type_keys("Welcome to Python Programming!!",with_spaces=True)

    def savefile(self):
        self.app.Notepad.MenuSelect("File ->SaveAs")
        time.sleep(2)
        path = str(Path.cwd())
        self.app.SaveAs.edit.SetText(path+"windowsdesktopsampletest.txt")
        savaslgbpx = Desktop().SaveAs
        savaslgbpx.wait('visible')
        savaslgbpx.print_control_identifiers()
        time.sleep(2)
        self.app.SaveAs.Save.click()
        time.sleep(5)
        try:
            replacedlg = Desktop().ConfirmSaveAs.Yes.click()
            replacedlg.wait('visible')
            print ("File replaced and saved successfully.")
        except:
            print ("File saved successfully.")
    def exitfile(self):

        self.app.Notepad.menu_select("File ->Exit")


if __name__ == '__main__':
    n = notepadoperations()
    n.type_contents()
    n.savefile()
    n.exitfile()
