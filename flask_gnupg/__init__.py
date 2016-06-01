from flask import current_app
import gnupg as _gnupg
import re


class GPG(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('GPG_BINARY', '/usr/local/bin/gpg')
        app.config.setdefault('GPG_KEYSERVERS', ['pgp.mit.edu'])
        app.config.setdefault('GPG_VERBOSE', True)
        app.config.setdefault(
            'GPG_OPTIONS',
            ['--batch', '--no-tty', '--yes', '--keyserver-options',
             'no-honor-keyserver-url,timeout=5'])

        gpg = _gnupg.GPG(
            gpgbinary=app.config['GPG_BINARY'],
            gnupghome=app.config['GPG_HOME'],
            verbose=app.config['GPG_VERBOSE'],
            options=app.config['GPG_OPTIONS'])

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['gnupg'] = gpg

    @property
    def gnupg(self):
        return current_app.extensions.get('gnupg')


def fetch_gpg_key(email=None, ks=None):
    """Fetch GPG keys from keyserver and save them in the local keychain

    :param email: Email address
    :param ks: KeyServer
    """
    gpg = current_app.extensions.get('gnupg', None)
    if gpg is None:
        raise RuntimeError('Flask-GnuPG not found in curent application: {}'.
                           format(current_app))
    if get_keyid(email) is None:
        keys = gpg.search_keys(email, ks)
        if keys:
            for key in keys:
                gpg.recv_keys(ks, key['keyid'])


def get_keyid(email=None):
    """Get keyid from local keychain

    :param email: Email address
    """
    gpg = current_app.extensions.get('gnupg', None)
    if gpg is None:
        raise RuntimeError('Flask-GnuPG not found in curent application: {}'.
                           format(current_app))
    for pub_key in gpg.list_keys():
        for uid in pub_key['uids']:
            match = re.match(r"^.*<(.*)>.*$", uid)
            if match and match.group(1).lower() == email.lower():
                return pub_key['keyid']
    return None
