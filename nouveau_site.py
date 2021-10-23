import os

http_host = input("quel est le nom du http host ? ")
mysql_db = input("quel est le nom de la bdd ? ")
mysql_root_password = input("quel est le mot de passe root ? ")
mysql_user = input("quel est le nom de l'utilisateur ? ")
mysql_password = input("quel est le mot de passe ? ")

cmd_http_host = "\"http_host=" + http_host
cmd_mysql_db = " mysql_db=" + mysql_db
cmd_mysql_root_password = " mysql_root_password=" + mysql_root_password
cmd_mysql_user = " mysql_user=" + mysql_user
cmd_mysql_password = " mysql_password=" + mysql_password + "\""

Cmd1="ansible-playbook -i /home/ansible/virtualans/inventaire.inv /home/ansible/virtualans/playbook.yml --extra-vars "
CmdF=(Cmd1+ cmd_http_host + cmd_mysql_db + cmd_mysql_root_password + cmd_mysql_user + cmd_mysql_password)

print(CmdF)

os.systemmp(CmdF)


