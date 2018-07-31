<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodoro Tracker</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
    <link rel="stylesheet" type="text/css" href="/css/pomodoro.css">
    <link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css"><link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/dt-1.10.18/datatables.min.css"/>

    <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>

</head>
<body class="my-body">

<header>
    <section>
        <h2 class="header-title">Pomodoro Time Tracker</h2>
        <nav>
            <ul>
                <li><a class="btn" role="button" href="/app/settings">&#9881;</a></li>
                <li><a class="btn" role="button" href="/app/logout">Logout</a></li>
                <li><a class="btn" role="button" href="/app/login">Login/Create</a></li>
                <li><a class="btn" role="button" href="/app/export_poms">Export Poms</a></li>
                <li><a class="btn" role="button" href="/app/pomodoro_set">Display Poms</a></li>
                <li><a class="btn" role="button" href="/app/pomodoro">Pomodoro</a></li>
                <li><a class="btn" role="button" href="/app/home">Home</a></li>
            </ul>
        </nav>
    </section>
</header>

<main class="container">
    <div class="container pom-app">
        <div class="row">
            <div class="col-md-12">
                <a class="btn btn-secondary" role="button">Filter</a>
                <a class="btn btn-secondary" role="button">Filter</a>
                <a class="btn btn-secondary" role="button">Filter</a>
                <a class="btn btn-secondary" role="button">Filter</a>
                <a class="btn btn-secondary" role="button">Filter</a>
            </div>
        </div>
    </div>
    <br>
    <div style="padding: 15px"></div>
    <div class="container pom-app">
        <div class="row pom-sheet">
            <div class="col-md-12">
                <h1>Pomodoros</h1>
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
                    <tr>
                        <td class="center-text">
                        </td>
                        <td class="keep-format">
                        </td>
                        <td class="center-text">
                        </td>
                        <td class="center-text">
                        </td>
                        <td class="center-text">
                        </td>
                        <td class="center-text">
                        </td>
                        <td class="center-text">
                        </td>
                        <td class="keep-format">
                        </td>
                    </tr>
                </table>
                <br>
            </div>
        </div>
    </div>
    <div id="derp"></div>
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
<script type="text/javascript" src="/js/underscore-min.js"></script>
<script type="text/javascript" src="/js/backbone-min.js"></script>

<script src="/js/filter_poms.js"></script>
</body>
</html>