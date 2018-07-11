<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodora Tracker</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
    <link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">
    <script src="/js/jquery.js"></script>
</head>
<body class="my-body">
<header class="container">
    <div class="row header">
        <div class="col-md-12">
            <h1 class="center-text">Pomodora Time Tracker</h1>
            <br>
        </div>
    </div>
</header>
<main class="container">
    <div class="container pom-app">
        <div class="row pom-form">
            <div class="col-md-12">
                <form action='http://localhost:8000/api/poms' method='post'>
                    <div class="row">
                        <div class="col-xl-6 col-lg-4 col-md-12 col-sm-12">
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
                        </div>
                        <div class="col-xl-6 col-lg-8 col-md-12 col-sm-12 form-text">
                            <h5>Title:</h5>
                            <textarea rows="3" cols="50" type='text' name='task'></textarea>
                            <br>
                            <h5>Description:</h5>
                            <textarea rows="6" cols="50" type='text' name='review'></textarea><br><br>
                            <input class="btn btn-primary float-right" type='submit' role="button" value='Submit Pomodora'>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <br>
    <div style="padding: 15px"></div>
    <div class="container pom-app">
        <div class="row pom-sheet">
            <div class="col-md-12">
                <br>
                <a class="btn btn-success float-right" href="http://localhost:8000/api/pom_sheet_export" role="button">Export</a>
                <h1>Todays Pom Sheet</h1>
                <table id="pom-table" width="100%">
                    <tr>
                        <th class="center-text" width="10%">Date</th>
                        <th width="25%">Title</th>
                        <th class="center-text" width="10%">Flags</th>
                        <th class="center-text" width="11%">Start Time</th>
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
    <div>
        <img class="time-image mx-auto d-block" src="/assets/time.jpg">
    </div>
    <div></div>
</main>
<footer>
    <div class="container">
        <span class="footer">&copy; Arin Blue 2018</span>
    </div>
</footer>
<script src="/js/bootstrap.min.js"></script>
</body>
</html>