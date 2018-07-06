<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodora Tracker</title>
    ##     <link rel="stylesheet" type="text/css" href="css/style.css">

    <style>
        #pom-table {
            border: 1px solid black;
        }

        td, th {
            padding: 10px;
            border: 1px solid black;
        }

        table {
            border-collapse: collapse;
        }
    </style>
</head>
<body>
<form action='http://localhost:8000/submitPom' method='post'>
    <fieldset>
        <legend>Submit Pomodora:</legend>

        Pomodora Time Block:<br>
        <select name="time_block">
            % for time in time_blocks:
                <option>${time}</option>
            % endfor
        </select>
        <br><br>

        Task:<br>
        <textarea rows="4" cols="50" type='text' name='task' value='Arin'></textarea>
        <br>
        Review:<br>
        <textarea rows="4" cols="50" type='text' name='review' value='Blue'></textarea><br><br>
        <input type='submit' value='Submit Pomodora'>
    </fieldset>

    <h1>Pomodora Sheet</h1>
    <table id="pom-table">
        <tr>
            <th>Date</th>
            <th>Task</th>
            <th>Start Time</th>
            <th>End Time</th>
            <th>Review</th>
        </tr>
        % for row in pom_rows:
            <tr>
                <td>
                    ${row.date}
                </td>
                <td>
                    ${row.task}
                </td>
                <td>
                    ${row.start_time}
                </td>
                <td>
                    ${row.end_time}
                </td>
                <td>
                    ${row.review}
                </td>
            </tr>
        % endfor
    </table>
</form>
</body>
</html>