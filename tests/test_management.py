import mock
import unittest

from talon_one import management

class TestManagementApi(unittest.TestCase):
    def setUp(self):
        self.client = management.Client("http://localhost:9000", "demo@talon.one", "demo1234")

    def tearDown(self):
        self.client = None

    def test_user_login(self):
        print self.client.login()

if __name__ == '__main__':
    unittest.main()
