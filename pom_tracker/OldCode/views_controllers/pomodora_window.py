from pyforms.utils.settings_manager import conf
from OldCode.config import settings
from OldCode.helpers import yaml_helper
from pyforms import BaseWidget
from pyforms.controls import ControlTextArea
from pyforms.controls import ControlCheckBoxList
from pyforms.controls import ControlCombo
from pyforms.controls import ControlButton
from OldCode.objects.pomodora import Pomodora
from OldCode.models.flag_type_model import FlagTypeModel

conf += settings


class PomodoraWindow(Pomodora, BaseWidget):

    def __init__(self):
        Pomodora.__init__(self, '', [], '', '')
        BaseWidget.__init__(self, 'Pomodora Window')
        self.parent = None

        # Definition of the forms fields
        self.current_task_field = ControlTextArea('Current Task')
        self.flags_fields = ControlCheckBoxList('Flags')
        self.time_blocks_fields = ControlCombo('Pomodora Block')
        self.review_field = ControlTextArea('Review')
        self.submit_button_field = ControlButton('Submit Pom')

        self.init_flag_fields()
        self.init_times()

        # Define the button action
        self.submit_button_field.value = self.submit_button_action

        self.formset = ['current_task_field', '', '=', 'time_blocks_fields',
                        '=', 'flags_fields', 'review_field',
                        (' ', 'submit_button_field', ' '), ' ']

    def submit_button_action(self):
        self.current_task = self.current_task_field.value
        self.flags = []
        for flag in self.flags_fields.value:
            self.flags.append(flag)
        self.review = self.review_field.value
        self.time_block = self.time_blocks_fields.value
        # In case the window has a parent
        if self.parent is not None:
            self.parent.add_pom(self)

    def init_times(self):
        filepath = 'templates/pom_template.yaml'
        data = yaml_helper.loader(filepath)
        time_blocks = data.get('time_blocks')
        for val, time_block in time_blocks.items():
            self.time_blocks_fields.add_item(time_block)

    def init_flag_fields(self):
        flag_type_model = FlagTypeModel()
        flag_types = flag_type_model.get_flag_types()
        for row in flag_types:
            self.flags_fields += (row.flag_type, False)
