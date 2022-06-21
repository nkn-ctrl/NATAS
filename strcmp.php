<?php
$str1 = "iloveyou";
$str2 = "iloveyou";
$str3 = "iloveyou11";
$str4 = "ilove";
$str5 = "ilo4eyou";

echo strcmp($str1,$str1);
echo "\n";

echo strcmp($str1,$str2);
echo "\n";

echo strcmp($str1,$str3);
echo "\n";

echo strcmp($str1,$str4);
echo "\n";

echo strcmp($str1,$str5);
echo "\n";

if(!strcmp($str1,$str5)){
    echo "!";
    echo "\n";
}else{
    echo "!!";
    echo "\n";
}

$fields = array(
    "passwd" => "iloveyou",
    'pw' => 'bar'
);
$a = "danux";
if(!strcmp($a,$fields)){
    echo "This is ZERO";
}else{
    echo "This is NOT zero";
}