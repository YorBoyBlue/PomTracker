from __init__ import *
from views_controllers.pomodora_window import PomodoraWindow
from helpers.add_menu import AddMenu
from pyforms.controls import ControlDockWidget
from models.pomodora_model import PomodoraModel


class PomSheetWindow(AddMenu, BaseWidget):

    def __init__(self):
        BaseWidget.__init__(self, 'Pomodora Tracker')
        AddMenu.__init__(self)
        self.panel = ControlDockWidget()
        self.pom_list = self.init_pom_list()
        self.load_pom_window()
        self.populate_pom_list()

    def init_pom_list(self):
        pom_list = ControlList('Pom Sheet', default="",
                               remove_function=self.rmv_pom_btn_action)

        pom_list.horizontal_headers = ['Time Block', 'Task', 'Flags',
                                       'Review']
        pom_list.select_entire_row = True
        pom_list.readonly = True
        return pom_list

    def populate_pom_list(self):
        self.pom_list.clear()
        pom_model = PomodoraModel()
        pom_rows = pom_model.get_todays_poms()
        for pom_row in pom_rows:
            time_block = '' + pom_row['start_time'] + '-' + \
                         pom_row['end_time']
            task = pom_row['task']
            flags = ''
            flag_rows = pom_model.get_flags_by_pom_id(pom_row['id'])
            index = 0
            for flag_row in flag_rows:
                index += 1
                flags += flag_row['flag_type']
                if index < len(flag_rows):
                    flags += '\n'

            review = pom_row['review']

            self.pom_list += [time_block, task,
                              flags,
                              review]
        self.pom_list.resize_rows_contents()

    def open_pom_window(self):
        self.panel.show()

    def add_pom(self, pomodora):
        pom_model = PomodoraModel()
        pom_model.insert_pom_and_pom_flags(pomodora)
        pomodora.close()
        self.load_pom_window()
        self.populate_pom_list()

    def remove_pom(self, index):
        pass

    def rmv_pom_btn_action(self):
        if self.pom_list.selected_row_index is not None:
            self.remove_pom(self.pom_list.selected_row_index)

    def load_pom_window(self):
        win = PomodoraWindow()
        win.parent = self
        self.panel.value = win
