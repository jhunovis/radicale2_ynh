# Radicale

Radical is a calendar and contact server CalDAV/CardDAV with administration interface.

To connect another client to radical, we must inform these addresses:

## Complete CalDAV/CardDAV collection of a user:
URL : https://domain.tld/path/user/

Exemple : https://example.org/radicale/me/

## To connect a calendar in particular:
URL : https://domain.tld/path/user/calendar.ics/

Exemple : https://example.org/radicale/me/calendar.ics/

## To connect an address book in particular:
URL : https://domain.tld/path/user/AddressBook.vcf/

Exemple : https://example.org/radicale/me/AddressBook.vcf/

Authenticated users can read and write their own collections under the path /USERNAME/

See the documentation for more features: 

http://radicale.org/configuration/


## Create a new schedule or a new address book:

Use the new interface at: 
    https://example.org/radicale/.web

The login is the same of your yunohost account



## Making Radical log more verbose:
By default, the Radical log is set to INFO. This method savings the hard drive but does not debug Radicale in case of problems.  
To pass Radicale in DEBUG mode, edit the */etc/radicale/logging* and change INFO to DEBUG in sections *[logger_root]* and *[handler_file]*. Then reload the uwsgi service.  
Now, the log displays all requests that are made to Radicale and analysis of *rights* file.  
However, do not stay on this mode because the log is filled very quickly.

---


