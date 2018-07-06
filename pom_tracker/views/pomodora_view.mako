<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodora Tracker</title>
</head>
<body>
<form action='http://localhost:8000/pomodora' method='post'>
    <fieldset>
        <legend>Submit Pomodora:</legend>

        Pomodora Time Block:<br>
        <select name="time_block">
            % for time in {time_blocks}:
                <option></option>
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

    <table>
        % for time in {time_blocks}:
            ${time}
        % endfor
        <tr>
            <td>

            </td>
        </tr>
    </table>
</form>
</body>
</html>