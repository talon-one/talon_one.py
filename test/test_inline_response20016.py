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
from talon_one.models.inline_response20016 import InlineResponse20016  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse20016(unittest.TestCase):
    """InlineResponse20016 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20016
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response20016.InlineResponse20016()  # noqa: E501
        if include_optional :
            return InlineResponse20016(
                total_result_size = 56, 
                data = [
                    talon_one.models.application_event.ApplicationEvent(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        application_id = 56, 
                        profile_id = 56, 
                        session_id = 56, 
                        type = '0', 
                        attributes = talon_one.models.attributes.attributes(), 
                        effects = [
                            None
                            ], 
                        rule_failure_reasons = [
                            talon_one.models.rule_failure_reason.RuleFailureReason(
                                campaign_id = 56, 
                                campaign_name = '0', 
                                ruleset_id = 56, 
                                coupon_id = 56, 
                                coupon_value = '0', 
                                referral_id = 56, 
                                referral_value = '0', 
                                rule_index = 56, 
                                rule_name = '0', 
                                condition_index = 56, 
                                effect_index = 56, 
                                details = '0', )
                            ], )
                    ]
            )
        else :
            return InlineResponse20016(
                total_result_size = 56,
                data = [
                    talon_one.models.application_event.ApplicationEvent(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        application_id = 56, 
                        profile_id = 56, 
                        session_id = 56, 
                        type = '0', 
                        attributes = talon_one.models.attributes.attributes(), 
                        effects = [
                            None
                            ], 
                        rule_failure_reasons = [
                            talon_one.models.rule_failure_reason.RuleFailureReason(
                                campaign_id = 56, 
                                campaign_name = '0', 
                                ruleset_id = 56, 
                                coupon_id = 56, 
                                coupon_value = '0', 
                                referral_id = 56, 
                                referral_value = '0', 
                                rule_index = 56, 
                                rule_name = '0', 
                                condition_index = 56, 
                                effect_index = 56, 
                                details = '0', )
                            ], )
                    ],
        )

    def testInlineResponse20016(self):
        """Test InlineResponse20016"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
