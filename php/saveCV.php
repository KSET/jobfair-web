<?php

include("definitions.php");

$postdata = file_get_contents("php://input");
$cv = json_decode($postdata);
echo $cv->email;

// configuration


// database connection
$conn = new PDO("mysql:host=".DBHOST.";dbname=".DBNAME,DBUSER,DBPASS);

// new data


// query
$sql = "INSERT INTO CV2015 (
    name,
    surname,
    adress,
    zip,
    city,
    phone,
    email,
    web,
    birth,
    education,
    experience,
    languages,
    computerskills,
    otherskills)
    VALUES (
    :name,
    :surname,
    :adress,
    :zip,
    :city,
    :phone,
    :email,
    :web,
    :birth,
    :education,
    :experience,
    :languages,
    :computerskills,
    :otherskills
    )";
$q = $conn->prepare($sql);
$q->execute(array( ':name' => $cv->name,
    ':surname' => $cv->surname,
    ':adress' => $cv->adress,
    ':zip' => $cv->zip,
    ':city' => $cv->city,
    ':phone' => $cv->tel,
    ':email' => $cv->email,
    ':web' => $cv->web,
    ':birth'=> $cv->birth->day.'-'.$cv->birth->month.'-'.$cv->birth->year,
    ':education' => json_encode($cv->education),
    ':experience' => json_encode($cv->work) ,
    ':languages' => json_encode($cv->languages),
    ':computerskills' => $cv->computers,
    ':otherskills' => $cv->other
    ));






?>