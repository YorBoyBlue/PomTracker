from __init__ import *
from pomodoras import Pomodoras
from pomodora_window import PomodoraWindow
from add_menu import AddMenu
from pyforms.controls import ControlDockWidget
import csv
import datetime


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

        # Definition of the forms fields
        self.pom_list = ControlList('Pom Sheet', default="",
                                    remove_function=self.rmv_pom_btn_action)

        self.pom_list.horizontal_headers = ['Task', 'Label', 'Review']
        self.pom_list.select_entire_row = True
        self.pom_list.readonly = True
        self.load_pom_window()

    def close_event(self, event):
        print('Closed!')
        "called on close"

    def open_pom_window(self):
        self.panel.show()

    def save_pom_sheet(self):

        todays_date = datetime.date.today()
        file_name = 'Pom - ' + str(todays_date) + '.csv'

        with open(file_name, 'w') as new_file:
            # Create fieldnames for the Dictionary Writer
            fieldnames = ['Task', 'Label', 'Review']
            # Create new file
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

            # Force the DictWriter to write the headers first
            csv_writer.writeheader()

            # Generate the list of dictionaries for the Pomodoras
            pom_values = self.pom_list.form.value
            poms = []
            for pom_row in pom_values:
                poms.append(dict(zip(fieldnames, pom_row)))

            # Write the Pomodoras to an external csv file
            for pom in poms:
                csv_writer.writerow(pom)

    def load_pom_sheet(self):

        todays_date = datetime.date.today()
        file_name = 'Pom - ' + str(todays_date) + '.csv'

        with open(file_name, 'r') as existing_file:
            # Read existing file
            csv_reader = csv.DictReader(existing_file)

            for pom_row in csv_reader:
                self.pom_list += pom_row.values()

    def add_pom(self, pomodora):
        """
        Redefines the add_pom function from Pomodoras class to update the GUI
        every time a new pomodora is added.
        """
        super(PomSheetWindow, self).add_pom(pomodora)
        self.pom_list += [pomodora.current_task, pomodora.label,
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

    # def move_up_btn_action(self):
    #     """
    #     Remove pom button event
    #     """
    #     if self.pom_list.selected_row_index is not None:
    #         self.remove_pom(self.pom_list.selected_row_index)
    #
    # def move_down_btn_action(self):
    #     """
    #     Remove pom button event
    #     """
    #     if self.pom_list.selected_row_index is not None:
    #         self.remove_pom(self.pom_list.selected_row_index)

    def load_pom_window(self):
        win = PomodoraWindow()
        win.parent = self
        # win.show()
        self.panel.value = win

    # Execute the application


if __name__ == "__main__":
    pyforms.start_app(PomSheetWindow, geometry=(600, 600, 800, 800))
