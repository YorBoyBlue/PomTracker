import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlTextArea
from pyforms.controls import ControlButton
from pyforms.controls import ControlCheckBox
from pyforms.controls import ControlLabel


class PomTracker(BaseWidget):

    def __init__(self):
        super(PomTracker, self).__init__('Pomodoro Tracker')

        # Pom Submit Section
        # Pom 1
        self.pom_1 = ControlLabel('Pom 1 \n 9:00 - 9:25-')
        self.pom_passed_1 = ControlCheckBox('Solid Pom', True)
        self.task_1 = ControlTextArea('Task', 'Default value')
        self.label_1 = ControlText('Label')
        self.review_1 = ControlTextArea('Review')
        # Pom 2
        self.pom_2 = ControlLabel('Pom 2 \n 9:30 - 9:55 ')
        self.pom_passed_2 = ControlCheckBox('Solid Pom', True)
        self.task_2 = ControlTextArea('Task', 'Default value')
        self.label_2 = ControlText('Label')
        self.review_2 = ControlTextArea('Review')
        # Pom 3
        self.pom_3 = ControlLabel('Pom 3 \n10:00 - 10:25')
        self.pom_passed_3 = ControlCheckBox('Solid Pom', True)
        self.task_3 = ControlTextArea('Task', 'Default value')
        self.label_3 = ControlText('Label')
        self.review_3 = ControlTextArea('Review')
        # Pom 4
        self.pom_4 = ControlLabel('Pom 4 \n10:35 - 11:00')
        self.pom_passed_4 = ControlCheckBox('Solid Pom', True)
        self.task_4 = ControlTextArea('Task', 'Default value')
        self.label_4 = ControlText('Label')
        self.review_4 = ControlTextArea('Review')
        # Pom 5
        self.pom_5 = ControlLabel('Pom 5 \n11:05 - 11:30')
        self.pom_passed_5 = ControlCheckBox('Solid Pom', True)
        self.task_5 = ControlTextArea('Task', 'Default value')
        self.label_5 = ControlText('Label')
        self.review_5 = ControlTextArea('Review')
        # Pom 6
        self.pom_6 = ControlLabel('Pom 6 \n11:35 - 12:00')
        self.pom_passed_6 = ControlCheckBox('Solid Pom', True)
        self.task_6 = ControlTextArea('Task', 'Default value')
        self.label_6 = ControlText('Label')
        self.review_6 = ControlTextArea('Review')
        # Pom 7
        self.pom_7 = ControlLabel('Pom 7 \n12:30 - 12:55')
        self.pom_passed_7 = ControlCheckBox('Solid Pom', True)
        self.task_7 = ControlTextArea('Task', 'Default value')
        self.label_7 = ControlText('Label')
        self.review_7 = ControlTextArea('Review')
        # Pom 8
        self.pom_8 = ControlLabel('Pom 8 \n 1:00 - 1:25 ')
        self.pom_passed_8 = ControlCheckBox('Solid Pom', True)
        self.task_8 = ControlTextArea('Task', 'Default value')
        self.label_8 = ControlText('Label')
        self.review_8 = ControlTextArea('Review')
        # Pom 9
        self.pom_9 = ControlLabel('Pom 9 \n 1:30 - 1:55 ')
        self.pom_passed_9 = ControlCheckBox('Solid Pom', True)
        self.task_9 = ControlTextArea('Task', 'Default value')
        self.label_9 = ControlText('Label')
        self.review_9 = ControlTextArea('Review')
        # Pom 10
        self.pom_10 = ControlLabel('Pom 10 \n 2:05 - 2:30 ')
        self.pom_passed_10 = ControlCheckBox('Solid Pom', True)
        self.task_10 = ControlTextArea('Task', 'Default value')
        self.label_10 = ControlText('Label')
        self.review_10 = ControlTextArea('Review')
        # Pom 11
        self.pom_11 = ControlLabel('Pom 11 \n 2:35 - 3:00 ')
        self.pom_passed_11 = ControlCheckBox('Solid Pom', True)
        self.task_11 = ControlTextArea('Task', 'Default value')
        self.label_11 = ControlText('Label')
        self.review_11 = ControlTextArea('Review')
        # Pom 12
        self.pom_12 = ControlLabel('Pom 12 \n 3:05 - 3:30 ')
        self.pom_passed_12 = ControlCheckBox('Solid Pom', True)
        self.task_12 = ControlTextArea('Task', 'Default value')
        self.label_12 = ControlText('Label')
        self.review_12 = ControlTextArea('Review')
        # Pom 13
        self.pom_13 = ControlLabel('Pom 13 \n 3:40 - 4:05 ')
        self.pom_passed_13 = ControlCheckBox('Solid Pom', True)
        self.task_13 = ControlTextArea('Task', 'Default value')
        self.label_13 = ControlText('Label')
        self.review_13 = ControlTextArea('Review')
        # Pom 14
        self.pom_14 = ControlLabel('Pom 14 \n 4:10 - 4:35 ')
        self.pom_passed_14 = ControlCheckBox('Solid Pom', True)
        self.task_14 = ControlTextArea('Task', 'Default value')
        self.label_14 = ControlText('Label')
        self.review_14 = ControlTextArea('Review')
        # Pom 15
        self.pom_15 = ControlLabel('Pom 15 \n 4:40 - 5:05 ')
        self.pom_passed_15 = ControlCheckBox('Solid Pom', True)
        self.task_15 = ControlTextArea('Task', 'Default value')
        self.label_15 = ControlText('Label')
        self.review_15 = ControlTextArea('Review')

        # Submit Button
        self.submit_button = ControlButton('Submit Pom')

        # Pom List
        self.pom_passed_display = ControlLabel()
        self.task_display = ControlLabel()
        self.label_display = ControlLabel()
        self.review_display = ControlLabel('Review')

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
        self.formset = [
            ('pom_1', 'pom_passed_1', 'task_1', 'label_1', 'review_1'),
            ('pom_2', 'pom_passed_2', 'task_2', 'label_2', 'review_2'),
            ('pom_3', 'pom_passed_3', 'task_3', 'label_3', 'review_3'),
            ('pom_4', 'pom_passed_4', 'task_4', 'label_4', 'review_4'),
            ('pom_5', 'pom_passed_5', 'task_5', 'label_5', 'review_5'),
            ('pom_6', 'pom_passed_6', 'task_6', 'label_6', 'review_6'),
            ('pom_7', 'pom_passed_7', 'task_7', 'label_7', 'review_7'),
            ('pom_8', 'pom_passed_8', 'task_8', 'label_8', 'review_8'),
            ('pom_9', 'pom_passed_9', 'task_9', 'label_9', 'review_9'),
            ('pom_10', 'pom_passed_10', 'task_10', 'label_10', 'review_10'),
            ('pom_11', 'pom_passed_11', 'task_11', 'label_11', 'review_11'),
            ('pom_12', 'pom_passed_12', 'task_12', 'label_12', 'review_12'),
            ('pom_13', 'pom_passed_13', 'task_13', 'label_13', 'review_13'),
            ('pom_14', 'pom_passed_14', 'task_14', 'label_14', 'review_14'),
            ('pom_15', 'pom_passed_15', 'task_15', 'label_15', 'review_15')
        ]

        # Define the button action
        self.submit_button.value = self.submit_action

    def submit_action(self):
        """Button action event"""
        # self._pom_passed_display.value = self._pom_passed.value
        # self.task_display.value = self.task.value
        # self.label_display.value = self.label.value
        # self.review_display.value = self.review.value

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
if __name__ == "__main__":
    pyforms.start_app(PomTracker)
