<?php
include("definitions.php");

$conn = new PDO("mysql:host=".DBHOST.";dbname=".DBNAME,DBUSER,DBPASS);

$sql = "SELECT * FROM CV2015";
$q = $conn->prepare($sql);
$q->execute();
$row= $q->fetchAll();
echo json_encode($row);

?>