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
                        <p>Welcome to the Pomodora Time Tracker! Time is the only non-renewable resource. Here you can
                            make sure you are spending it wisely!</p>
                        <p>Create your account below and start tracking where you spend your valuable time today!</p>
                    </div>
                </div>
                <form action='/api/users' method='post'>
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12">
                            <h2>Create User:</h2>
                            <br>
                            <label class="email" for="email"><b>Email:</b></label>
                            <input type="text" placeholder="Enter Email" name="email" required>
                            <br><br>
                            <label class="first_name" for="first_name"><b>First Name:</b></label>
                            <input type="text" placeholder="Enter First Name" name="first_name" required>
                            <br><br>
                            <label class="middle_name" for="middle_name"><b>Middle Name:</b></label>
                            <input type="text" placeholder="Enter Middle Name" name="middle_name">
                            <br><br>
                            <label class="last_name" for="last_name"><b>Last Name:</b></label>
                            <input type="text" placeholder="Enter Last Name" name="last_name" required>
                            <br><br>
                            <label class="display_name" for="display_name"><b>Display Name:</b></label>
                            <input type="text" placeholder="Enter Display Name" name="display_name">
                            <br><br>
                            <label class="password" for="password"><b>Password:</b></label>
                            <input type="password" placeholder="Enter Password" name="password" required>
                            <br><br><br>
                            <button class="btn btn-primary" type="submit">Create User</button>
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