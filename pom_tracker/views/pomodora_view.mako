<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodora Tracker</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
    <link rel="stylesheet" type="text/css" href="/css/pomodora.css">
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
                <li><a class="btn" role="button" href="/app/logout">Logout</a></li>
                <li><a class="btn" role="button" href="/app/login">Login/Create</a></li>
                <li><a class="btn" role="button" href="/app/export_poms">Export Poms</a></li>
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
                        % if pom_exists:
                            <div class="alert alert-warning">
                                <strong>Oops!</strong> You have already submitted a pomodora with that start time
                                today.
                                You can delete it and submit a new one if you like but you must delete it first.
                            </div>
                        % endif
                        <div class="col-xl-6 col-lg-4 col-md-12 col-sm-12">
                            <div class="row">
                                <h2>Pomodora:</h2>
                            </div>
                            <br><br>
                            <div class="row">
                                <h5 style="padding-top: 5px; margin-right: 5px">Time Block:</h5>
                                <select style="width: auto" class="custom-select" name="time_block">
                                    % for time in time_blocks:
                                        <option>${time}</option>
                                    % endfor
                                </select>
                            </div>
                            <br><br>
                            <div class="row">
                                <div style="float: left; margin-right: 30px">
                                    <h5>Flags:</h5>
                                    % for flag in flag_types:
                                        <input type="checkbox" name="flags" value="${flag[0]}"> ${flag[0]}  <br>
                                    % endfor
                                </div>
                                <div class="distractions">
                                    <h5>Distractions:</h5>
                                    <input class="distractions_check top" type="checkbox" name="distractions" value="1">
                                    <input class="distractions_check" type="checkbox" name="distractions" value="1"><br>
                                    <input class="distractions_check middle" type="checkbox" name="distractions"
                                           value="1"><br>
                                    <input class="distractions_check bottom" type="checkbox" name="distractions"
                                           value="1">
                                    <input class="distractions_check" type="checkbox" name="distractions" value="1">
                                </div>
                            </div>
                        </div>
                        <div class="col-xl-6 col-lg-8 col-md-12 col-sm-12 form-text">
                            <div class="row">
                                <h5 class="title">Title:</h5>
                                <textarea rows="3" cols="50" type='text' name='task'></textarea>
                                <h5 style="margin-top: 10px">Description:</h5>
                                <textarea rows="6" cols="50" type='text' name='review'></textarea>
                            </div>
                            <br>
                            <div class="row">
                                <div class="col-xl-8 col-lg-8 col-md-8 col-sm-6" style="padding-left: 0">
                                    <input style="margin-top: 5px; margin-right: 5px" type="checkbox" name="pom_success"
                                           value="1"> Was this pom successful? <br>
                                </div>
                                <div class="col-xl-4 col-lg-4 col-md-4 col-sm-6" style="padding-right: 0">
                                    <input class="btn btn-primary main-button float-right" type='submit' role="button"
                                           value='Submit Pomodora'>
                                </div>
                            </div>
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
                <form action='/api/delete_poms' method='post'>
                    <br>
                    <a class="btn btn-success float-right main-button" href="/api/pom_sheet_export" role="button">Export
                        Sheet</a>
                    <input style="margin-right: 15px" class="btn btn-secondary float-right main-button" type='submit'
                           role="button"
                           value='Delete Selected Poms'>
                    <h1>Todays Pom Sheet</h1>
                    <table id="pom-table" width="100%">
                        <tr>
                            <th width="2%"></th>
                            <th width="20%">Title</th>
                            <th class="center-text" width="2%">Flags</th>
                            <th class="center-text" width="2%">Start Time</th>
                            <th class="center-text" width="2%">End Time</th>
                            <th class="center-text" width="2%">Distractions</th>
                            <th class="center-text" width="2%">Pom Success</th>
                            <th>Review</th>
                        </tr>
                        % for row in pom_rows:
                            <tr>
                                <td class="center-text">
                                    <input type="checkbox" name="poms_to_delete" value="${row.id}">
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
                                <td class="center-text">
                                    ${row.distractions}
                                </td>
                                <td class="center-text">
                                    % if row.pom_success == 1:
                                        &#x2714;
                                    % else:
                                        &#x2718;
                                    % endif
                                </td>
                                <td class="keep-format">
                                    ${row.review}
                                </td>
                            </tr>
                        % endfor
                    </table>
                    <br>
                </form>
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