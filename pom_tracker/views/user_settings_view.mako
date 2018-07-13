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
                        <p>Login below and start tracking where you spend your valuable time!</p>
                        <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has
                            been the industry's standard dummy text ever since the 1500s, when an unknown printer took a
                            galley of type and scrambled it to make a type specimen book. It has survived not only five
                            centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
                            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum
                            passages, and more recently with desktop publishing software like Aldus PageMaker including
                            versions of Lorem Ipsum.</p>
                        <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has
                            been the industry's standard dummy text ever since the 1500s, when an unknown printer took a
                            galley of type and scrambled it to make a type specimen book. It has survived not only five
                            centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
                            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum
                            passages, and more recently with desktop publishing software like Aldus PageMaker including
                            versions of Lorem Ipsum.</p>
                    </div>
                </div>
                <form action='/app/login' method='post'>
                    <div class="row">
                        <div class="col-12">
                            <h2>Settings:</h2>
                            <br>
                            <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
                                has been the industry's standard dummy text ever since the 1500s, when an unknown
                                printer took a galley of type and scrambled it to make a type specimen book. It has
                                survived not only five centuries, but also the leap into electronic typesetting,
                                remaining essentially unchanged. It was popularised in the 1960s with the release of
                                Letraset sheets containing Lorem Ipsum passages, and more recently with desktop
                                publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
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