<?php

$data = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_decrypt($in){
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    for($i=0;$i<strlen($text);$i++){
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    
    return $outText;
}

echo base64_encode(xor_decrypt(json_encode($data)));
echo "\n";
?>