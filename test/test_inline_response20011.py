# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import talon_one
from talon_one.models.inline_response20011 import InlineResponse20011  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse20011(unittest.TestCase):
    """InlineResponse20011 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20011
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response20011.InlineResponse20011()  # noqa: E501
        if include_optional :
            return InlineResponse20011(
                total_result_size = 56, 
                has_more = True, 
                data = [
                    talon_one.models.application_customer.ApplicationCustomer(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        integration_id = '0', 
                        attributes = talon_one.models.attributes.attributes(), 
                        account_id = 56, 
                        closed_sessions = 56, 
                        total_sales = 1.337, 
                        loyalty_memberships = [
                            talon_one.models.loyalty_membership.LoyaltyMembership(
                                joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                loyalty_program_id = 56, )
                            ], 
                        audience_memberships = [
                            talon_one.models.audience_membership.AudienceMembership(
                                id = 56, 
                                name = '0', )
                            ], 
                        last_activity = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else :
            return InlineResponse20011(
                data = [
                    talon_one.models.application_customer.ApplicationCustomer(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        integration_id = '0', 
                        attributes = talon_one.models.attributes.attributes(), 
                        account_id = 56, 
                        closed_sessions = 56, 
                        total_sales = 1.337, 
                        loyalty_memberships = [
                            talon_one.models.loyalty_membership.LoyaltyMembership(
                                joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                loyalty_program_id = 56, )
                            ], 
                        audience_memberships = [
                            talon_one.models.audience_membership.AudienceMembership(
                                id = 56, 
                                name = '0', )
                            ], 
                        last_activity = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )

    def testInlineResponse20011(self):
        """Test InlineResponse20011"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
