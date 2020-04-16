# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import talon_one
from talon_one.api.integration_api import IntegrationApi  # noqa: E501
from talon_one.rest import ApiException


class TestIntegrationApi(unittest.TestCase):
    """IntegrationApi unit test stubs"""

    def setUp(self):
        self.api = talon_one.api.integration_api.IntegrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_coupon_reservation(self):
        """Test case for create_coupon_reservation

        Create a new coupon reservation  # noqa: E501
        """
        pass

    def test_create_referral(self):
        """Test case for create_referral

        Create a referral code for an advocate  # noqa: E501
        """
        pass

    def test_delete_coupon_reservation(self):
        """Test case for delete_coupon_reservation

        Delete coupon reservations  # noqa: E501
        """
        pass

    def test_delete_customer_data(self):
        """Test case for delete_customer_data

        Delete the personal data of a customer.  # noqa: E501
        """
        pass

    def test_get_customer_inventory(self):
        """Test case for get_customer_inventory

        Get an inventory of all data associated with a specific customer profile.  # noqa: E501
        """
        pass

    def test_get_reserved_coupons(self):
        """Test case for get_reserved_coupons

        Get all valid reserved coupons  # noqa: E501
        """
        pass

    def test_get_reserved_customers(self):
        """Test case for get_reserved_customers

        Get the users that have this coupon reserved  # noqa: E501
        """
        pass

    def test_track_event(self):
        """Test case for track_event

        Track an Event  # noqa: E501
        """
        pass

    def test_update_customer_profile(self):
        """Test case for update_customer_profile

        Update a Customer Profile  # noqa: E501
        """
        pass

    def test_update_customer_session(self):
        """Test case for update_customer_session

        Update a Customer Session  # noqa: E501
        """
        pass

    def test_update_customer_session_v2(self):
        """Test case for update_customer_session_v2

        Update a Customer Session  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
