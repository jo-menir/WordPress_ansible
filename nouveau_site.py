import os

http_host = input("quel est le nom du http host ? ")
cmd1 = "ansible-playbook -i /home/ansible/virtualans/inventaire.inv /home/ansible/virtualans/wordpress/tasks/main.yml --extra-vars http_host="
cmdFinal = cmd1 + http_host
os.system(cmdFinal)
