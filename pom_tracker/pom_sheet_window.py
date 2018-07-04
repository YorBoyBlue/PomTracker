from __init__ import *
from pomodoras import Pomodoras
from pomodora_window import PomodoraWindow
from add_menu import AddMenu
from pyforms.controls import ControlDockWidget
from pomodora_model import PomodoraModel
from pomodora import Pomodora


class PomSheetWindow(AddMenu, Pomodoras, BaseWidget):
    """
    This application is a GUI implementation for the Pomodora Concept for
    tracking time
    """

    def __init__(self):
        Pomodoras.__init__(self)
        BaseWidget.__init__(self, 'Pomodora Tracker')
        AddMenu.__init__(self)
        self.panel = ControlDockWidget()
        self.pom_list = self.init_pom_list()
        self.load_pom_window()

    def init_pom_list(self):
        # Definition of the forms fields
        pom_list = ControlList('Pom Sheet', default="",
                               remove_function=self.rmv_pom_btn_action)

        pom_list.horizontal_headers = ['Time Block', 'Task', 'Flags',
                                       'Review']
        pom_list.select_entire_row = True
        pom_list.readonly = True
        return pom_list

    def open_pom_window(self):
        self.panel.show()

    def save_pom_sheet(self):
        pom_model = PomodoraModel()
        for pom_row in self.pom_list.value:
            time_block = pom_row[0]
            task = pom_row[1]
            flags = pom_row[2].split('\n')
            review = pom_row[3]
            pom = Pomodora(time_block, task, flags, review)
            pom_model.insert_pom_and_pom_flags(pom)
        self.pom_list.clear()

    def add_pom(self, pomodora):
        """
        Redefines the add_pom function from Pomodoras class to update the GUI
        every time a new pomodora is added.
        """
        super(PomSheetWindow, self).add_pom(pomodora)
        flags = ''
        for i in range(len(pomodora.flags)):
            flags += str(pomodora.flags[i])
            if i != len(pomodora.flags) - 1:
                flags += '\n'
        self.pom_list += [pomodora.time_block, pomodora.current_task,
                          flags,
                          pomodora.review]
        pomodora.close()
        self.pom_list.resize_rows_contents()
        self.load_pom_window()

    def remove_pom(self, index):
        """
        Redefines the remove_pom function from Pomodoras class to update the
        GUI every time a pomodora is removed.
        """
        super(PomSheetWindow, self).remove_pom(index)
        self.pom_list -= index

    def rmv_pom_btn_action(self):
        """
        Remove pom button event
        """
        if self.pom_list.selected_row_index is not None:
            self.remove_pom(self.pom_list.selected_row_index)

    def load_pom_window(self):
        win = PomodoraWindow()
        win.parent = self
        # win.show()
        self.panel.value = win


if __name__ == "__main__":
    pyforms.start_app(PomSheetWindow, geometry=(600, 600, 800, 800))
