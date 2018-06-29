from pyforms.utils.settings_manager import conf
import settings
import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlTextArea
from pyforms.controls import ControlCombo
from pyforms.controls import ControlButton
from pomodora import Pomodora

conf += settings


class PomodoraWindow(Pomodora, BaseWidget):

    def __init__(self):
        Pomodora.__init__(self, '', '', '')
        BaseWidget.__init__(self, 'Pomodora Window')
        self.parent = None

        # Definition of the forms fields
        self.current_task_field = ControlTextArea('Current Task')
        self.label_field = ControlCombo('Label')
        self.review_field = ControlTextArea('Review')
        self.submit_button_field = ControlButton('Submit Pom')

        self.label_field.add_item('Code', 'Code')
        self.label_field.add_item('Dev Ops', 'Dev Ops')
        self.label_field.add_item('Training', 'Training')

        # Define the button action
        self.submit_button_field.value = self.submit_button_action

        self.formset = ['current_task_field', 'label_field',
                        'review_field',
                        (' ', 'submit_button_field', ' '), ' ']

    def submit_button_action(self):
        self.current_task = self.current_task_field.value
        self.label = self.label_field.value
        self.review = self.review_field.value

        # In case the window has a parent
        if self.parent is not None:
            self.parent.add_pom(self)


# Execute the application
if __name__ == "__main__":
    pyforms.start_app(PomodoraWindow)
