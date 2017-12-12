from radicale.auth import BaseAuth
from ldap3 import Server, Connection, ALL, NTLM

class Auth(BaseAuth):
    def is_authenticated(self, user, password):
        connexion = ""
        ldap_url = ""
        ldap_base = ""
        ldap_attribute = ""

        if self.configuration.has_option("auth", "ldap_url"):
            ldap_url = Server (self.configuration.get("auth", "ldap_url"), get_info=ALL)
            connexion = Connection(ldap_url, auto_bind=True)
        self.logger.info("Configuration option %r is %r", "ldap_url", ldap_url)

        try:
            connexion.extend.standard.who_am_i()
        except:
            self.logger.debug ("Reconnecting the LDAP server")
            connexion = Connection(ldap_url, auto_bind=True)

        if self.configuration.has_option("auth", "ldap_base"):
            ldap_base = self.configuration.get("auth", "ldap_base")
        self.logger.info("Configuration option %r is %r", "ldap_base", ldap_base)

        if self.configuration.has_option("auth", "ldap_attribute"):
            ldap_attribute = self.configuration.get("auth", "ldap_attribute")

        self.logger.info("Configuration option %r is %r", "ldap_attribute", ldap_attribute)
        distinguished_name = "%s=%s" % (ldap_attribute, user)
        self.logger.debug("LDAP bind for %r in base %r", (distinguished_name, ldap_base))



        if connexion.search(ldap_base,  '(%s=%s)' % (ldap_attribute, user)):
            self.logger.debug ("User %s found" % user)
            try:
                req_user= "%s=%s,%s" % (ldap_attribute, user, ldap_base )
                connexion = Connection(ldap_url, req_user, password)
            except connexion.last_error:
                self.logger.debug("Invalid request")
            else:
                if connexion.bind():
                    self.logger.debug("LDAP bind OK")
                    return True
                else:
                    self.logger.log("Bad password")
        else:
            self.logger.debug("User %s not found" % user)

        self.logger.debug("LDAP bind failed")

        return False
