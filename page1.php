<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="edge">
<link rel="icon" href="logo2.ico" type="image/x-icon" sizes="16">

<meta name="viewport" content="width=device-width, scale=1.0">
<title>mentoriny_Centrale</title>
<link rel="stylesheet" href="stylepage1.css">
<link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
    <div class="wrapper">
        <form id="loginForm" action="page2.php" method="POST">
            <h1>login</h1>
            <div class="input_box">
                <input type="text" placeholder="adress mail" id="adress mail" required>
                <i class='bx bxs-user'></i>
            </div>
            <div class="input_text">
                <input type="password" placeholder="password" id="password" required>
                <i class='bx bxs-lock-alt'></i>
            </div>
            <div class="remember_forgot">
                <label><input type="checkbox">remember me</label>
                <a href="#">forget password?</a>
            </div>
            <button type="submit" class="btn">login</button>
            <div class="register_link">
                <p>Don't have an account</p>
                <a href="#">sign up</a>
            </div>
        </form>
    </div>

    <!-- Logos des réseaux sociaux -->
    <div class="footer">
    <ul class="social-icons">
        <li><a href="https://www.linkedin.com/in/malikagareh/"><img src="télécharger.jpeg" alt="LinkedIn"></a></li>
        <li><a href="https://www.instagram.com/malikagareh/"><img src="th.jpeg" alt="Instagram"></a></li>
    </ul>
    </div>
    

    
</body>
</html>