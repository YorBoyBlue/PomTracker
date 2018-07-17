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

<header>
    <section>
        <h2 class="header-title">Pomodora Time Tracker</h2>
        <nav>
            <ul>
                <li><a class="btn" role="button" href="/app/settings">&#9881;</a></li>
                <li><a class="btn" role="button" href="/app/export_poms">Export Poms</a></li>
                <li><a class="btn" role="button" href="/app/logout">Logout</a></li>
                <li><a class="btn" role="button" href="/app/login">Login/Create</a></li>
                <li><a class="btn" role="button" href="/app/pomodora">Pomodora</a></li>
                <li><a class="btn" role="button" href="/app/home">Home</a></li>
            </ul>
        </nav>
    </section>
</header>

<main class="container">
    <div class="container pom-app">
        <div class="row pom-form">
            <div class="col-md-12">
                <form action='/api/poms' method='post'>
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
                            <textarea rows="3" cols="50" type='text' name='task' required></textarea>
                            <br>
                            <h5>Description:</h5>
                            <textarea rows="6" cols="50" type='text' name='review' required></textarea><br><br>
                            <input class="btn btn-primary float-right" type='submit' role="button"
                                   value='Submit Pomodora'>
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
                <a class="btn btn-success float-right" href="/api/pom_sheet_export" role="button">Export</a>
                <h1>Todays Pom Sheet</h1>
                <table id="pom-table" width="100%">
                    <tr>
                        <th class="center-text" width="11%">Date</th>
                        <th width="25%">Title</th>
                        <th class="center-text" width="10%">Flags</th>
                        <th class="center-text" width="11%">Start Time</th>
                        <th class="center-text" width="10%">End Time</th>
                        <th>Review</th>
                    </tr>
                    % for row in pom_rows:
                        <tr>
                            <td class="center-text">
                                ${row.created}
                            </td>
                            <td class="keep-format">
                                ${row.task}
                            </td>
                            <td class="center-text">
                                % if len(row.flags) > 0:
                                    % for flag in row.flags:
                                    ${flag.flag_type}<br>
                                    % endfor
                                % else :
                                    ${row.flags[0]}
                                % endif
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