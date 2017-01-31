import mock
import unittest

from talon_one import management

class TestManagementApi(unittest.TestCase):
    def setUp(self):
        self.client = management.Client("http://localhost:9000", "demo@talon.one", "demo1234")
        self.assertTrue(self.client.login())

    def tearDown(self):
        self.assertTrue(self.client.logout())

    def test_applications(self):
        apps = self.client.list_applications()

        # remove all apps
        exists = False
        for app in apps["data"]:
            if app["name"] == "TestApp1":
                self.client.delete("/v1/applications/%d" % app["id"])

        new_app = self.client.create_application("TestApp1", "c0a9cc9bd05d62ed")

        print dir(new_app)

if __name__ == '__main__':
    unittest.main()
