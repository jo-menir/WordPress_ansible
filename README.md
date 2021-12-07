# Why a WordPress Ansible Playbook ?

WordPress is the most famous CMS, it is important and interesting to be able to simplify the configuration of sites and avoid errors during it.

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
```
[web]
front-srv ansible_host=192.168.0.2

[bdd]
back-srv ansible_host=192.168.0.3
```
### 2. Execute the playbook with the python script.
```
python3 ./nouveau_site.py.
```
### 3. Answer script questions
```
- what is the name of the http host? (Ex: site1)
- what is the name of the database? (WordPress database)
- what is the root password? (mariadb root password ; used when you typed the command mysql_secure_connection)
- what is the username? (name of the WordPress user)
- what is the password? (WordPress user password)
- What is the ip address of the database server? (Ex: 192.168.0.3)
```
### 4. Open a web browser.
```
Go to localhost/{{ http host }}
```
