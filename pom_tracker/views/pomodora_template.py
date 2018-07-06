from mako.template import Template
from helpers.yaml_helper import YamlHelper

times = tuple()
filepath = '../templates/pom_sheet_times_template.yaml'
data = YamlHelper().loader(filepath)
time_blocks = data.get('time_blocks')
for val, time_block in time_blocks.items():
    times = times + ('<tr> <td>' + time_block + '</td> <br> </tr>',)

mytemplate = Template(
    filename='C:/Work/Python/PomTracker/pom_tracker/views/pomodora_view.html')
print(mytemplate.render(time_blocks=times))
