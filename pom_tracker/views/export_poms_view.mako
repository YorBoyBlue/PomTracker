<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodoro Tracker</title>
    <link rel="icon" href="/assets/favicon.ico">
    <link rel="stylesheet" type="text/css" href="/css/style.css">
    <link rel="stylesheet" type="text/css" href="/css/user_create.css">
    <link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css">
    <script src="/js/jquery.js"></script>
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
        <div class="row pom-form">
            <div class="col-md-12">
                <div class="row">
                    <div class="col-12">
                        <h2>Export Pom Sheets:</h2>
                        <br><br>
                        <p>You can choose a start and end date to export all pomodoros within those dates (including the
                            start and end date). This will export all poms into a single file.</p>
                        <br>
                        <p>There is currently only support to export a JSON file but there will be a CSV export coming
                            soon as well.</p>
                        <br><br>
                    </div>
                </div>
                <form action='/app/export_poms' method='post' autocomplete="on">
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12">
                            <label class="date" for="start_date"><b>Start Date:</b></label>
                            <br>
                            <input type="date" title="start_date" name="start_date" required>
                            <br><br><br>
                            <label class="date" for="end_date"><b>End Date:</b></label>
                            <br>
                            <input type="date" title="end_date" name="end_date" required>
                            <br><br><br><br>
                            <button class="btn btn-primary main-button" role="button" type="submit">Export</button>
                        </div>
                        <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12">
                        </div>
                    </div>
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
<script src="/js/bootstrap.bundle.js"></script>
</body>
</html>