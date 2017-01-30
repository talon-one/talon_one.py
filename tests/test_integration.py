import mock
import unittest

from talon_one import integration

class TestIntegrationApi(unittest.TestCase):
    def setUp(self):
        self.client = integration.Client("http://localhost:9000", 1, "c0a9cc9bd05d62ed")

    def tearDown(self):
        self.client = None

    def test_update_customer_profile(self):
        data = {
            "advocateId": "",
            "attributes": {
                "Name": "Foobar1"
            }
        }
        integration_id = "cust1"
        print self.client.update_customer_profile(integration_id, data)


if __name__ == '__main__':
    unittest.main()
