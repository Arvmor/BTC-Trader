<!DOCTYPE html>
<html lang="en">
<head>
	<title>.: Panel :.</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="main.css">
</head>
<body>
    <div class="container-contact100">
        <div class="wrap-contact100">
            <div id="MyClockDisplay" class="contact100-form-title" onload="showTime()" style="margin: -80px 0px 0px 0px;"></div>
            <script>function showTime() {
                    var date = new Date();
                    var h = date.getHours(); // 0 - 23
                    var m = date.getMinutes(); // 0 - 59
                    var s = date.getSeconds(); // 0 - 59
                    var session = "AM";
                    if (h == 0) {
                        h = 12;
                    }
                    if (h > 12) {
                        h = h - 12;
                        session = "PM";
                    }
                    h = (h < 10) ? "0" + h : h;
                    m = (m < 10) ? "0" + m : m;
                    s = (s < 10) ? "0" + s : s;
                    var time = h + ":" + m + ":" + s + " " + session;
                    document.getElementById("MyClockDisplay").innerText = time;
                    document.getElementById("MyClockDisplay").textContent = time;
                    setTimeout(showTime, 1000);
                }
                showTime();</script>
            <a href="#" onClick="window.location.reload();">Refresh</a>
            <script src="./btnClick.js"></script>
            <span class="contact100-form-title">
                BTC: <?php include('btcText.php'); ?> | Rial: <?php include('rialText.php'); ?>
			</span>
            <span class="contact100-form-title">
                Sell
            </span>
            <pre><textarea class="input100" name="message" disabled><?php include('sellText.php'); ?></textarea></pre>
            <span class="focus-input100"></span>
            <span class="contact100-form-title">
                Buy
            </span>
            <pre><textarea class="input100" name="message" disabled><?php include('buyText.php'); ?></textarea></pre>
            <span class="focus-input100"></span>
        </form>
		</div>
	</div>
</body>
</html>
