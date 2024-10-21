<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Datenbankabfrage]</title>
</head>
<style>
.res {
    font-size: 24px;
    font-weight: 750;
}
th, td, tr{
    border: 1px solid black;
    background-color: white;
    text-align: center;
    font-size: 24px;
    font-weight: 750;
    padding: 0.6em 1em;
}
table {
    border: 1px solid black;
}
</style>
<body>
    <center>
<?php
$servername = "localhost";
$username = "jumbo";
$password = "jumbo";
$dbname = "jumbo";
 
$conn = new mysqli($servername, $username, $password, $dbname);
 
if ($conn->connect_error) {
    die("Verbindung fehlgeschlagen: " . $conn->connect_error);
}
 
$sql = "SELECT * FROM `testadressen` WHERE `anrede` LIKE 'Frau' AND `familienstand` LIKE 'Single'";
$result = $conn->query($sql);
 
$row_cnt = $result->num_rows;
echo "<div>Ergebnisse: $row_cnt</div>";
 
if ($result->num_rows > 0) {
    echo "  <table>
                <tr>
                    <th>
                        Vorname
                    </th>
                    <th>
                        Nachnamen
                    </th>
                    <th>
                        Anrede
                    </th>
                    <th>
                        Familienstand
                    </th>
 
                </tr>";
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row['vorname'] . "</td><td>" . $row['nachname'] . "</td><td>" . $row['anrede'] . "</td><td>" . $row['familienstand'] . "</td></tr>";
    }
    echo "</table>";
} else {
    echo "0 Ergebnisse";
}
$conn->close();
?>
<a href="index.html">Back to the homepage</a>
    </center>
</body>
</html>