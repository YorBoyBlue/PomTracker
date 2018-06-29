import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton


class PomTracker(BaseWidget):

    def __init__(self):
        super(PomTracker, self).__init__('Pomodoro Tracker')

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

# Execute the application
if __name__ == "__main__":   pyforms.start_app(PomTracker)
