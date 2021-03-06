<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodoro Tracker</title>
    <link rel="icon" href="/assets/favicon.ico">
    <link rel="stylesheet" type="text/css" href="/css/style.css">
    <link rel="stylesheet" type="text/css" href="/css/display_poms.css">
    <link rel="stylesheet" type="text/css" href="/css/pomodoro.css">
    <link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css"
          href="https://cdn.datatables.net/v/dt/dt-1.10.18/datatables.min.css"/>

    <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
    <script type="text/javascript"
            src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>

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
            <div class="col-12">
                <div id="filters" class="col-12">
                    <div class="row">
                        <div class="col-12">
                            <h2>Filters</h2>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-12">
                            <div style="display: inline-block; top: 0">
                                <br>
                                <h6>Date</h6>
                                <label class="date">
                                    <input class='date_filter' type="date">
                                </label>
                                <br>
                                <br>
                                <h6>Unsuccessful</h6>
                                <label class="switch">
                                    <input class='unsuccessful_filter' type="checkbox">
                                    <span class="slider round"></span>
                                </label>
                                <br>
                                <br>
                                <h6>Distractions</h6>
                                <label class="switch">
                                    <input class='distractions_filter' type="checkbox">
                                    <span class="slider round"></span>
                                </label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <br>
    <div style="padding: 15px"></div>
    <div class="container pom-app">
        <div class="row pom-sheet">
            <div class="col-md-12">
                <h1>Pomodoros</h1>
                <div class="pagination">
                    <ul>
                        <li>
                            <a id="first" class="pagination-offset-link" data-pagenum="1"
                               href="#">First</a>
                        </li>
                        <li class="active">
                            <a id="offset1" class="pagination-offset-link" data-pagenum="1"
                               href="#">1</a>
                        </li>
                        <li>
                            <a id="offset2" class="pagination-offset-link" data-pagenum="2"
                               href="#">2</a>
                        </li>
                        <li>
                            <a id="offset3" class="pagination-offset-link" data-pagenum="3"
                               href="#">3</a>
                        </li>
                        <li>
                            <a id="offset4" class="pagination-offset-link" data-pagenum="4"
                               href="#">4</a>
                        </li>
                        <li>
                            <a id="offset5" class="pagination-offset-link" data-pagenum="5"
                               href="#">5</a>
                        </li>
                        <li>
                            <a id="last" class="pagination-offset-link" data-pagenum="1" href="#">Last</a>
                        </li>
                    </ul>
                    <span id="pagination-count-info"></span>
                </div>
                <table id="pom-table" width="100%">
                    <thead>
                    <tr>
                        <th width="11%"></th>
                        <th width="20%"></th>
                        <th class="center-text" width="2%"></th>
                        <th class="center-text" width="2%"></th>
                        <th class="center-text" width="2%"></th>
                        <th class="center-text" width="2%"></th>
                        <th class="center-text" width="2%"></th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody>
                    </tbody>
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
<script src="/js/bootstrap.bundle.js"></script>
<script type="text/javascript" src="/js/underscore-min.js"></script>
<script type="text/javascript" src="/js/backbone-min.js"></script>

<script src="/js/pom_collection_app.js"></script>
</body>
</html>