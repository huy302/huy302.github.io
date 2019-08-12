<?php
	// if form was submitted then process it here
	$outstring = "";
	if (!empty($_POST["mytext"]))
	{
		$count = 0;	
		$inputstrarray = explode(" ", trim($_POST["mytext"]));
		for ($i = 0; $i < count($inputstrarray); $i++) {
			if ($inputstrarray[$i] !== "") {
				$inputnum = intval($inputstrarray[$i]);
				$inputnumarray[$count] = $inputnum;
				$count ++;
			}
		}
		// sort $inputnumarray
		for ($i = 0; $i < $count - 1; $i++) {
			for ($j = $i + 1; $j < $count; $j++) {
				if ($inputnumarray[$i] > $inputnumarray[$j]) {
					$temp = $inputnumarray[$i];
					$inputnumarray[$i] = $inputnumarray[$j];
					$inputnumarray[$j] = $temp;
				}
			}
		}
		// output into $outstring
		$outstring = implode(" ", $inputnumarray);
		
	} else 
	{
		$outstring = "ready!";
	}
?>



<html>
	<head>
		<title>khon nan</title>
		<script language="JavaScript">
		<!--
		function setFocus() {
			document.myform.mytext.focus();
		}
		function submitenter(myfield, e) {
			var keycode;
			if (window.event) keycode = windo.event.keyCode;
			else if (e) keycode = e.which;
			else return true;

			if (keycode == 13) {
				myfield.form.submit();
				return false;
			} else
				return true;
			
		}
		//-->
		</script>
	</head>
	<body onload="setFocus()">
		<label>
			<?php echo $outstring; ?>
		</label>
		<br>
		<br>
		<label>
			<?php if (!empty($_POST["mytext"])) echo $count . " numbers entered"; ?>
		</label>
		<br>
		<br>
		<br>
		<form name="myform" action="hieucon.php" method="post">
			<textarea id="mytext" name="mytext" rows="10" cols="100" onkeypress="return submitenter(this, event)"><?php // old submitted value ?></textarea>
		</form>
	</body>
</html>