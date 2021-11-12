# WordPress Ansible Playbook

This repository contains an ansible playbook launched with a python script to speed up and automate the creation and configuration of a WordPress site.

> Note:  currently this is works with a  Debian distribution.

## Requirements

- An Ansible server
- A server configured as an apache web server + php7.3 + php-xml + php-mysql
- A server configured as a mariadb database server. (type the command `mysql_secure_installation` to configure mariadb and remember the root password for mariadb, you will need it when running the python script.

> Note: All the machines must be able to communicate with each other and the ansible server must also be able to connect in SSH to the other two (enable ssh root login).

## Roles

The following roles are in this playbook.

| Role | Description | 
|-------|------------|
| Wordpress | Downloads latest Wordpress. Installs and sets up wp sites for given domains. Sets the owner of the folder that contains wordpress. Sets permissions for directories. Sets permissions for files
| Apache | Creates document root. Sets up Apache VirtualHost. Enables rewrite module, new site and default apache site
| Mariadb |  Creates database for WordPress. Creates MySQL user for WordPress.

## Usages 

### 1. Verify and modify the file inventaire.inv to match your infrastructure.

### 2. Execute the playbook with the python script.
```
python3 ./nouveau_site.py.
```
### 3. Answer script questions
```
-
-
-
-
-
-
```
### 4. Open a web browser.
```
Go to localhost/{{ host }}
```
