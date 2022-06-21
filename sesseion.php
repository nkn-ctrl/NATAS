<?php
session_start();
$_SESSION['test'] = 'hogehoge';
$_SESSION['test2'] = 'hugahuga';

echo $_SESSION['test']."\n";
echo $_SESSION['test2']."\n";
echo session_id()."\n";

echo session_name()."\n";

echo session_encode()."\n";
echo session_unset()."\n";
#echo $_SESSION['test']."\n";
?>