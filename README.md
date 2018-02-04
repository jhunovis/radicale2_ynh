Radicale for YunoHost
==================

[Yunohost project](https://yunohost.org/#/)

Radicale est un serveur CalDAV (calendrier) et CardDAV (contact) complet.

http://radicale.org/

==================

Radicale permet de créé ses calendriers et carnets d'adresses depuis une interface de configuration
accessible depuis : https://votredomain.tld/radicale/.web/

Il est moins friendly-user que [baikal](https://github.com/julienmalik/baikal_ynh),

La version 2 apporte des améliorations au niveau de la gestion mémoire,
et une gestion des plugins permettant d'intergré de nouvelles fonctionnalitées facilement
et de manière plus organisé.

Pour éffectuer une migration de la version 1 vers la 2 vous pouvez vous rendre sur :
http://radicale.org/1to2/


(Optionnel)
La configuration des partages se fait à l'aide du fichier de configuration des droits '/etc/radicale/rights'.

Les calendriers et les carnet d'adresses créé avec Radicale version 1.x ne sont pas compatible avec la version 2.x
==================

Le script installe les paquets *libjansson4* *libldap2-dev* *libmatheval1* *libpgm-5.1-0* *libpython-dev* *libsasl2-dev* *libsodium13* *libzmq3* *python-chardet-whl*
*python-colorama-whl* *python-dev* *python-distlib-whl* *python-html5lib-whl* *python-pip-whl* *python-requests-whl* *python-setuptools-whl* *python-six-whl* *python-urllib3-whl* *python-virtualenv* *python3-virtualenv* *virtualenv*.
