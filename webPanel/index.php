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
            <a href="#" onClick="window.location.reload();">Refresh</a>
            <script src="./btnClick.js"></script>
            <span class="contact100-form-title">
                BTC: <?php include('rialText.php'); ?> | Rial: <?php include('btcText.php'); ?>
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