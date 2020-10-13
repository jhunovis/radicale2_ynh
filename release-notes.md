# Release Notes
## 2.1.12~ynh1
Initial release. Notable changes from [kitoy30/radicale2_ynh](https://github.com/kitoy30/radicale2_ynh) release are:

- update to [Radicale 2.1.12](https://github.com/Kozea/Radicale/blob/2.1.x/NEWS.md#2112---wild-radish)
- switch Python module for LDAP authentication to [marcoh00/radicale-auth-ldap](https://github.com/marcoh00/radicale-auth-ldap)
- no more file logging, only journald logging
- [migrating away from the legacy permission management](https://yunohost.org/#/groups_and_permissions#migrating-away-from-the-legacy-permission-management)
- use the unique app id `radicale_jh`
  - this is required because the ID `radicale` is already in use by the officially accepted app
- general clean-up