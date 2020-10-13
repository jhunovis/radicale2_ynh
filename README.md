# Radicale for YunoHost
Self-host a [Radicale 2](http://radicale.org/) instance on your [Yunohost](https://yunohost.org/#/) server.

## Upgrading from kitoy30's package
- backup your user data
  1. by using Yunohost backup facility
  2. by creating a tar archive 
     - connect to your Yunohost instance with `ssh`
     - execute `sudo tar --directory /home/radicale/collections -czf radicale-collection.tgz .` 
- uninstall kitoy30's app
- install this package
  - `sudo yunohost app install https://github.com/jhunovis/radicale_ynh`
- restore the tar archive and restore ownership
  - `sudo tar --directory /home/radicale -xzf radicale-collection.tgz`
  - `sudo chown -R radicale.radicale /home/radicale`
- restart Radicale
  - `sudo systemctl restart radicale`  

## About this repository
This is a fork from [kitoy30/radicale2_ynh](https://github.com/kitoy30/radicale2_ynh) which promised support for Radicale 2.
Alas, it seems to be unmaintained at the moment. There is a sanctioned version of Radicale [listed in the YunoHost
application catalog](https://github.com/YunoHost-Apps/radicale_ynh), but it is for the heavily outdated version 1
of Radicale.  

Main differences to the kitoy30 version are:
- use the [latest version 2.1.12](https://github.com/Kozea/Radicale/blob/2.1.x/NEWS.md) of Radicale 2
- switch to a different [LDAP authorization](https://github.com/marcoh00/radicale-auth-ldap) library
  which at least attempts to sanitize user provided inputs
- clean up the code

Plans for the future are:
- update to Radicale 3
- get rid of LDAP
- automated testing  
