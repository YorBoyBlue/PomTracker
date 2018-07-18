<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pomodora Tracker</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
    <link rel="stylesheet" type="text/css" href="/css/user_create.css">
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
                <div class="row">
                    <div class="col-12">
                        <h1>Home Page</h1><br>
                        <p>Welcome to the Pomodora Time Tracker! Time is the only non-renewable resource. Here you can
                            make sure you are spending it wisely!</p>
                        <p>Click the button below to create a new account right now and you will be amazed at how much
                            you can get done in one day!</p>
                        <br>
                        <a class="btn btn-success main-button" href="/app/create" role="button">Create New Account</a>
                        <br><br><br>
                        <p>I started creating this application as an exercise to learn more about Python and HTTP. It
                            it was a fantastic learning experience and I hope you enjoy using this if you decide it is
                            right for you.</p>
                        <p>The concept is simple, the day is broken down into 25 minute blocks plus a 5 or 10 minute
                            break in between. This is called a Pomodora. The point is to focus 100% on a single task for
                            25 minutes and then take a break to review your progress and re evaluate the path you are
                            taking. There are studies done where the results of this approach show a significant
                            increase in productivity and decrease in mental fatigue. In other words, you get more done
                            in less time.</p>
                        <p>Sounds too good to be true? Try it for yourself and you will be surprised at the result.</p>
                        <p>Hope to see you back here soon!</p>
                    </div>
                </div>
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