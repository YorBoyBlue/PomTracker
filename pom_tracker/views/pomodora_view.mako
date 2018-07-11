<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodora Tracker</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
    <link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">
    <script src="/js/jquery.js"></script>
    <script src="/js/bootstrap.min.js"></script>
</head>
<body class="my-body">
<header class="container">
    <h1 class="center-text">Pomodora Time Tracker</h1>
    <br>
    <div class="row header">
        <div class="col-md-12">
        </div>
    </div>
</header>
<div class="container pom-app">
##     <div class="row pom-form">
##         <form action='http://localhost:8000/api/poms' method='post'>
##             <div class="col-md-4">
##                 <h2>Pomodora:</h2>
##                 <br>
##                 <h5>Time Block:</h5>
##                 <select class="custom-select" name="time_block">
##                     % for time in time_blocks:
##                         <option>${time}</option>
##                     % endfor
##                 </select>
##                 <br><br>
##                 <h5>Flags:</h5>
##                 % for flag in flag_types:
##                     <input type="checkbox" name="flags" value="${flag[0]}"> ${flag[0]} </input><br>
##                 % endfor
##             </div>
##             <div class="col-md-4">
##                 <h5>Title:</h5>
##                 <textarea rows="4" cols="50" type='text' name='task'></textarea>
##             </div>
##             <div class="col-md-4">
##                 <h5>Review:</h5>
##                 <textarea rows="8" cols="50" type='text' name='review'></textarea><br><br>
##                 <input class="btn btn-primary" type='submit' value='Submit Pomodora'>
##             </div>
##         </form>
##     </div>
    <div class="row pom-form">
        <div class="col-md-12">
            <form action='http://localhost:8000/api/poms' method='post'>
                <fieldset style="width:1570px">
                    <h2>Pomodora:</h2>
                    <br>
                    <h5>Time Block:</h5>
                    <select class="custom-select" name="time_block">
                        % for time in time_blocks:
                            <option>${time}</option>
                        % endfor
                    </select>
                    <br><br>
                    <h5>Flags:</h5>
                    % for flag in flag_types:
                        <input type="checkbox" name="flags" value="${flag[0]}"> ${flag[0]} </input><br>
                    % endfor
                    <br>
                    <h5>Title:</h5>
                    <textarea rows="4" cols="50" type='text' name='task'></textarea>
                    <br>
                    <h5>Review:</h5>
                    <textarea rows="8" cols="50" type='text' name='review'></textarea><br><br>
                    <input class="btn btn-primary" type='submit' value='Submit Pomodora'>
                </fieldset>
            </form>
        </div>
    </div>
</div>
<br>
<div></div>

<div class="container pom-app">
    <div class="row pom-sheet">
        <div class="col-md-12">
            <br>
            <h1>Todays Pom Sheet</h1>
            <table id="pom-table">
                <tr>
                    <th class="center-text" width="10%">Date</th>
                    <th width="30%">Title</th>
                    <th class="center-text" width="10%">Flags</th>
                    <th class="center-text" width="10%">Start Time</th>
                    <th class="center-text" width="10%">End Time</th>
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
                            ${row.start_time.strftime('%I:%M%p').strip('0')}
                        </td>
                        <td class="center-text">
                            ${row.end_time.strftime('%I:%M%p').strip('0')}
                        </td>
                        <td class="keep-format">
                            ${row.review}
                        </td>
                    </tr>
                % endfor
            </table>
        </div>
    </div>
</div>
<div></div>
<div class="footer">
    <p class="footer">&copy; Arin Blue 2018</p>
</div>
</body>
</html>