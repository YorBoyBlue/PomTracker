import pyforms
from PyQt5 import QtGui
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton


class AddMenuFuntionality(BaseWidget):
    """
    This class is a module of the application PeopleWindow.py
    It is a simple a example of how applications can be devided in modules with pyforms.
    It adds the Open and Save functionality
    """

    def __init__(self):
        super(AddMenuFuntionality, self).__init__('Pomodoro Tracker')

        # Definition of the forms fields
        self._firstname = ControlText('First name', 'Default value')
        self._middlename = ControlText('Middle name')
        self._lastname = ControlText('Lastname name')
        self._fullname = ControlText('Full name')
        self._button = ControlButton('Press this button')

        self.mainmenu = [
            {'File': [
                {'Open': self.open_event},
                '-',
                {'Save': self.save_event},
                {'Save as': self.save_as_event}
            ]
            },
            {'Edit': [
                {'Copy': self.edit_event},
                {'Past': self.past_event}
            ]
            }
        ]

        # Define the organization of the forms
        # Use dictionaries for tabs
        # Use the sign '=' for a vertical splitter
        # Use the signs '||' for a horizontal splitter
        self.formset = [{
            'Tab1': ['_firstname', '||', '_middlename', '||', '_lastname'],
            'Tab2': ['_fullname']
        },
            '=', (' ', '_button', ' ')]
        # The ' ' is used to indicate that a empty space should be placed at
        # the bottom of the window
        # If you remove the ' ' the forms will occupy the entire window
        # self.formset = [('_firstname', '_middlename', '_lastname'),
        #                 '_button',
        #                 '_fullname', ' ']

        # Define the button action
        self._button.value = self.button_action

    def button_action(self):
        """Button action event"""
        self._fullname.value = self._firstname.value + " " + \
                               self._middlename.value + " " + self._lastname.value

    def open_event(self):
        pass

    def save_event(self):
        pass

    def save_as_event(self):
        pass

    def edit_event(self):
        pass

    def past_event(self):
        pass

    def __savePeople(self):
        filename, _ = QtGui.QFileOpenEvent.getSaveFileName(parent=self,
                                                           caption="Save file",
                                                           directory=".",
                                                           filter="*.dat")

        if filename != None and filename != '': self.save(filename)

    def __loadPeople(self):
        filename, _ = QtGui.QFileOpenEvent.getOpenFileName(parent=self,
                                                           caption="Import file",
                                                           directory=".",
                                                           filter="*.dat")

        if filename != None and filename != '':
            self.load(filename)
            for person in self._people:
                self._peopleList += [person._firstName, person._middleName,
                                     person._lastName]

    def __exit(self):
        exit()
