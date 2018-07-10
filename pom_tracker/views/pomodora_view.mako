<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodora Tracker</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body>
<form action='http://localhost:8000/api/poms' method='post'>
    <fieldset style="width:1570px">
        <legend>Submit Pomodora:</legend>

        Time Block:<br>
        <select name="time_block">
            % for time in time_blocks:
                <option>${time}</option>
            % endfor
        </select>
        <br><br>

        Flags: <br>
        % for flag in flag_types:
            <input type="checkbox" name="flags" value="${flag[0]}"> ${flag[0]} </input><br>
        % endfor
        ##             <option value="volvo">Volvo</option>
            ##             <option value="saab">Saab</option>
            ##             <option value="opel">Opel</option>
            ##             <option value="audi">Audi</option>
##         <select name="flags" multiple>
##             % for flag in flag_types:
##                 <input type="checkbox" name="flags" value="${flag[0]}"> ${flag[0]}<br>
##             % endfor
##         </select>
##         <br><br>

        Title:<br>
        <textarea rows="4" cols="50" type='text' name='task'></textarea>
        <br>
        Review:<br>
        <textarea rows="8" cols="50" type='text' name='review'></textarea><br><br>
        <input type='submit' value='Submit Pomodora'>
    </fieldset>
</form>

<br>
<h1>Todays Pom Sheet</h1>
<table id="pom-table" width="1600px">
    <tr>
        <th width="10%">Date</th>
        <th width="30%">Task</th>
        <th width="10%">Flags</th>
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
                % for flag in row.flags:
                    ${flag.flag_type}<br>
                % endfor
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