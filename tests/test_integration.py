import unittest
from talon_one import exceptions
from talon_one import management
from talon_one import integration
from sys import version as pyversion

class TestIntegrationApi(unittest.TestCase):
    # global integration ids
    profile_id = "profile1"
    session_id = "profile1Session1"

    def setUp(self):
        try:
            self.integration_client = integration.Client()
            self.management_client = management.Client()

            self.management_client.login()

            # bootstrap application and campaign with simple rules
            self.app = self.management_client.create_application(
                name = "Python SDK Test App" + pyversion[0:3],
                api_key = "fefecafedeadbeef"
            )

            # setup runs for every test so we have to update application id
            self.integration_client.set_app_id(self.app["id"])
            self.integration_client.set_app_key(self.app["key"])

            self.campaign = self.management_client.post(
                "/v1/applications/{}/campaigns".format(self.app["id"]),
                {
                    "name": "Test Campaign",
                    "state": "disabled",
                    "limits": [
                        {
                            "action": "redeemReferral",
                            "entities": [
                                "Referral"
                            ],
                            "limit": 7.50
                        }],
                    "referralSettings": {
                        "couponPattern": "996732pucn",
                        "validCharacters": [
                            "a-z",
                            "0-9"
                        ]
                    },
                    "tags": ["Spring"],
                    "features": ["referrals"]
                })

            self.ruleset = self.management_client.post(
                "/v1/applications/{}/campaigns/{}/rulesets".format(self.app["id"], self.campaign["id"]),
                {"rules": [{
                    "title": "Free money for all!",
                    "condition": ["and", True],
                    "effects": [
                        ["setDiscount", "Free money", 45.55]
                    ]
                }]})

            self.campaign["activeRulesetId"] = self.ruleset["id"]
            self.campaign["state"] = "enabled"

            self.campaign = self.management_client.put(
                "/v1/applications/{}/campaigns/{}".format(self.app["id"], self.campaign["id"]),
                self.campaign)

            attr = {"entity": 'Event',
                    "eventType": 'Homepage',
                    "title": 'Homepage Page Url',
                    "name": 'URL',
                    "type": 'string',
                    "description": '',
                    "tags": [],
                    "editable": True
            }
            self.attr = self.management_client.post("v1/attributes", attr)

        except exceptions.TalonOneAPIError as te:
            print(te)

    def tearDown(self):
        self.integration_client = None
        if hasattr(self, "app"):
            self.management_client.delete_application(self.app["id"])
        if hasattr(self, "attr"):
            self.management_client.delete("/v1/attributes/{}".format(self.attr["id"]))

    def test_update_customer_profile(self):
        data = {"advocateId": "",
                "attributes": {
                    "Name": "Foobar1"
                }
        }
        response = self.integration_client.update_customer_profile(self.profile_id, data)

        self.assertEqual(self.__class__.profile_id, response["profile"]["integrationId"])
        self.assertEqual("Foobar1", response["profile"]["attributes"]["Name"])

    def test_create_referral_code(self):
        data = {"advocateProfileIntegrationId": self.__class__.profile_id,
                "campaignId": self.campaign["id"],
                "expiryDate": "2017-08-17T16:08:52.018206901+02:00",
                "startDate": "2017-02-28T16:08:52.018206901+01:00"}
        response = self.integration_client.create_referral_code(data)

        self.assertTrue(response["code"] != "")
        self.assertEqual(self.__class__.profile_id, response["advocateProfileIntegrationId"])

    def test_update_customer_session(self):
        data = {
            "cartItems": [
                {
                    "category": "food",
                    "height": 5.95,
                    "length": 5.99,
                    "name": "spatula",
                    "price": 26.8,
                    "quantity": 55,
                    "sku": "sxhj387plb",
                    "weight": 6.85,
                    "width": 5.7
                }
            ],
            "coupon": "6tu30966ay",
            "profileId": self.__class__.profile_id,
            "referral": "996732pucn",
            "state": "open",
            "total": 38.46
        }
        response = self.integration_client.update_customer_session(self.__class__.session_id, data)

        self.assertEqual(self.__class__.profile_id, response["profile"]["integrationId"])
        self.assertEqual("open", response["session"]["state"])
        self.assertEqual("setDiscount", response["event"]["effects"][0][3][0])
        self.assertEqual("rejectCoupon", response["event"]["effects"][1][3][0])
        self.assertEqual("rejectReferral", response["event"]["effects"][2][3][0])

    def test_close_customer_session(self):
        response = self.integration_client.close_customer_session(self.__class__.session_id)
        self.assertEqual(1, response["profile"]["closedSessions"])
        self.assertEqual(True, response["session"]["firstSession"])
        self.assertEqual("closed", response["session"]["state"])

    def test_track_event(self):
        self.integration_client.set_debug(False)

        response = self.integration_client.track_event(self.__class__.profile_id, self.__class__.session_id,
                                                       "Homepage", {"URL": "http://example.com"})

        self.assertEqual("Homepage", response["event"]["type"])
        self.assertEqual("http://example.com", response["event"]["attributes"]["URL"])

        # usage of unknown event type raises an error
        with self.assertRaises(exceptions.TalonOneAPIError):
            self.integration_client.track_event(self.__class__.profile_id, self.__class__.session_id,
                                                "Page", {"URL": "http://example.com"})

if __name__ == "__main__":
    unittest.main()
