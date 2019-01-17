<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="60">
<meta name="robots" content="none">
<meta name="robots" content="noindex">
<meta name="robots" content="nofollow">
<title>W318</title>
</head>
<body>
<h2>松田研究室（W318）</h2>
<hr>
<?php
$filename = 'reserchers';
$reserchers = file($filename);
if (empty($reserchers)) {
	echo 'ただいまW318には誰もいません。';
	echo "\n</body>\n</html>";
	exit();
} else {
	echo "現在W318には\n<br>\n<br>";
}
foreach ($reserchers as $resercher) {
	echo $resercher.'<br>';
}
?>
<br>
がいます。
</body>
</html>
