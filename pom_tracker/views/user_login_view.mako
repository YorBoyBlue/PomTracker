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
                <div class="row">
                    <div class="col-12">
                        <p>Welcome to the Pomodora Time Tracker! Time is the only non-renewable resource. Here you can
                            make sure you are spending it wisely!</p>
                        <p>Login below and start tracking where you spend your valuable time!</p>
                    </div>
                </div>
                <form action='/app/login' method='post'>
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12">
                            <h2>Login:</h2>
                            <br>
                            <label class="email" for="email"><b>Email:</b></label>
                            <input type="text" placeholder="Enter Email" name="email" required>
                            <br><br>
                            <label class="password" for="password"><b>Password:</b></label>
                            <input type="password" placeholder="Enter Password" name="password" required>
                            <br><br>
                            <button class="btn btn-primary" type="submit">Login</button>
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
<script src="/js/bootstrap.min.js"></script>
</body>
</html>