<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodora Tracker</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body>
<form action='http://localhost:8000/api/poms' method='post'>
    <fieldset style="width:1600px">
        <legend>Submit Pomodora:</legend>

        Time Block:<br>
        <select name="time_block">
            % for time in time_blocks:
                <option>${time}</option>
            % endfor
        </select>
        <br><br>

        Flag:<br>
        <select name="label">
            % for time in time_blocks:
                <option>${time}</option>
            % endfor
        </select>
        <br><br>

        Task:<br>
        <textarea rows="4" cols="50" type='text' name='task'></textarea>
        <br>
        Review:<br>
        <textarea rows="8" cols="50" type='text' name='review'></textarea><br><br>
        <input type='submit' value='Submit Pomodora'>
    </fieldset>
</form>


<h1>Pomodora Sheet</h1>
<table id="pom-table" width="1600px">
    <tr>
        <th width="10%">Date</th>
        <th width="35%">Task</th>
        <th width="10%">Start Time</th>
        <th width="10%">End Time</th>
        <th>Review</th>
    </tr>
    % for row in pom_rows:
        <tr>
            <td class="center-text">
                ${row.add_date}
            </td>
            <td class="keep-format">
                ${row.task}
            </td>
            <td class="center-text">
                ${row.start_time.strftime('%I:%M%p')}
            </td>
            <td class="center-text">
                ${row.end_time.strftime('%I:%M%p')}
            </td>
            <td class="keep-format">
                ${row.review}
            </td>
        </tr>
    % endfor
</table>
</body>
</html>