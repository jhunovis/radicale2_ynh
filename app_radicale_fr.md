# Radicale 2

Radicale est un serveur de calendrier et de contact CalDAV/CardDAV. 
Depuis la version 2 il y a maintenant une interface d'administration.


Pour connecter un client au serveur radicale, il faut renseigner ces adresses:

## Collection CalDAV/CardDAV complète d'un utilisateur:
URL : https://domain.tld/path/user/

Exemple : https://example.org/radicale/moi/

## Pour connecter un calendrier en particulier:
URL : https://domain.tld/path/user/calendar.ics/

Exemple : https://example.org/radicale/moi/calendar.ics/

## Pour connecter un carnet d'adresses en particulier:
URL : https://domain.tld/path/user/AddressBook.vcf/

Exemple : https://example.org/radicale/moi/AddressBook.vcf/


Par  default Un utilisateur authentifié peut lire et écrire sur son dossier uniquement.
Radicale permet de faire plus voir la documentation.

 http://radicale.org/configuration/



## Créer un nouveau calendrier ou un nouveau carnet d'adresses:
 Rendez-vous sur l'interface d'administation pour les crée
Exemple: https://example.org/radicale/.web/



---

## Rendre le log de Radicale plus loquace:
Par défaut, le log de Radicale est réglé sur INFO. Ce mode épargne le disque dur mais ne permet pas de débugger Radicale en cas de problème.  
Pour passer Radicale en mode DEBUG, il faut éditer le fichier */etc/radicale/logging* et passer INFO à DEBUG dans les sections *[logger_root]* et *[handler_file]* puis recharger le service uwsgi.  
Dés lors, le log affiche toutes les requêtes qui sont faite à Radicale ainsi que l'analyse du fichier *rights*.  
Il est toutefois déconseillé de rester sur ce mode, car le log se rempli très rapidement.

---


