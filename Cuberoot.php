
    <head>
        <title>Cube_Root</title>
    </head>
    <body>
        <style>
        body{
            text-align:center;
            font-size:1.5em;
            font-family:serif;
            background:black;
            color:rgb(5, 253, 17);
        }
        </style>
    </body>

<?php
    $n=mt_rand(1, 1000);
    echo "Number: $n<br>Cube Root: ";
    echo round(cube_root($n),4);
    function Sub($n, $m) {
        if($n > $m*$m*$m)
            return ($n-($m*$m*$m));
        else
            return (($m*$m*$m)-$n);
    }
    function cube_root($n) {
        if($n<0) { 
            $n=-$n; echo "-"; }
        $a=0; 
        $b=$n; 
        $e=0.0001; 
        while (true) {
            $m=($a+$b)/2;
            $p=Sub($n,$m); 
            if($p<=$e)
                return $m;
      
            if(($m*$m*$m)>$n)
                $b=$m; 
            else
                $a=$m; 
        }
    }
?>