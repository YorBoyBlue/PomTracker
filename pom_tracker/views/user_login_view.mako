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
                        % if login_failed:
                            <div class="alert alert-warning">
                                <strong>Oops!</strong> We could not find a user with that email and/or password. Please
                                double check
                                your info or create a new account.
                            </div>
                        % endif
                        % if session_expired:
                            <div class="alert alert-warning">
                                <strong>Oops!</strong> Your session has expired. Please login to verify it is still you.
                            </div>
                        % endif
                        <p>Welcome to the Pomodoro Time Tracker! Time is the only non-renewable resource. Here you can
                            make sure you are spending it wisely!</p>
                        <br>
                        <p>If you do not already have an account, you can create a new one by clicking the button below
                            and
                            filling out the form that follows. Start tracking where you spend your valuable time
                            today!</p>

                        <br>
                        <a class="btn btn-success main-button" href="/app/create" role="button">Create New Account</a>
                        <br><br><br>

                        <p>If you do already have an account, login below.</p>
                    </div>
                </div>
                <form action='/app/login' method='post' autocomplete="on">
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12">
                            <h2>Login:</h2>
                            <br>
                            <label class="email" for="email"><b>Email:</b></label>
                            <input type="text" placeholder="Enter Email" name="email" required>
                            <br><br>
                            <label class="password" for="password"><b>Password:</b></label>
                            <input type="password" placeholder="Enter Password" name="password" autocomplete="off"
                                   required>
                            <br><br><br>
                            <button class="btn btn-primary main-button" role="button" type="submit">Login</button>
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