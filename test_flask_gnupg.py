from shutil import rmtree
import os
import unittest
import gnupg as _gnupg
from flask import Flask
from flask.ext.gnupg import GPG, fetch_gpg_key, get_keyid

GPG_HOME = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.gnupg')


class FlaskGnuPGTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['GPG_HOME'] = GPG_HOME
        gpg = GPG()
        gpg.init_app(self.app)

    @classmethod
    def tearDownClass(cls):
        if os.path.isdir(GPG_HOME):
            rmtree(GPG_HOME)

    def test_init(self):
        self.assertTrue('gnupg' in self.app.extensions)
        self.assertIsInstance(self.app.extensions['gnupg'], _gnupg.GPG)

    def test_fetch(self):
        with self.app.test_request_context():
            fetch_gpg_key('iscandr@gmail.com', self.app.config['GPG_KEYSERVERS'][0])

    def test_get(self):
        with self.app.test_request_context():
            rv = get_keyid('iscandr@gmail.com')
            self.assertTrue(rv == u'28432835514AA0F6')

if __name__ == '__main__':
    unittest.main()
