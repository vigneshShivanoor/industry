<!-- <html>
<head>
<style>
.c1{
	padding: 150 600;
	display: inline-block;
	align: center;
}
legend
{
	background-color: white;
align: center;
border: 1px solid black;
}
fieldset{
	background-color: cyan;
	display: inline-block;
}
input[type=submit]
{
	background-color: chartreuse;
}
</style>
<title>
Project</title></head>
<body>
<div class="c1">
<form method="post" enctype="multipart/form-data">
		<fieldset><legend align=center>
<h3 align=center>Upload Your Files</h3></legend>
<label align=center>Select File</label><br>
<input type="file" name="image"><br>
<input type="submit" name="Upload">
</fieldset>
</form></div>
</body></html> -->
<?php

$localhost = "localhost";
$dbus="root";
$dbpw="";
$dbname="suptech";
$x=0;
$conn = mysqli_connect($localhost,$dbus,$dbpw,$dbname);
if (isset($_POST['Upload']))
{
	$pname =$_FILES['image']['name'];
	$tname = $_FILES['image']['tmp_name'];
	$uploads_dir= "images/" .$pname;
	$t=date('d-m-y')."-".time();
	if(file_exists($uploads_dir))
	die('<font color="Crimson" size=5px >File already Exists</font>');
	if($_FILES['image']['size']>500000)
	die('<font color="yellow" size=5px>Choose a file size below 5MB</font>');
	$f1=explode(".",$pname);
	if(sizeof($f1)>2)
	{
		die('<font color="blue" size=5px>Multiple file extensions used</font>');
		echo "<br>";
	}
	$ok=array("jpg","jpeg","png");
	for($i=1;$i<sizeof($f1);$i++)
	{
	if(!in_array($f1[$i],$ok))
		$x=1;
	}
	if($x==1)
	{
		die('<font color="#FF19F3" size=5px>Wrong file format</font>');
	}
	if($x==0)
	{
	move_uploaded_file($tname, $uploads_dir);
	$sql = "INSERT INTO temp(images,Uploaded_on) values('$uploads_dir',now())";
	if(mysqli_query($conn,$sql))
	die('<font color="green" size=5px>Successfully Uploaded</font>');	
	}
}