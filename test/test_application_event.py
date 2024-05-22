# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you access the Campaign Manager at `https://yourbaseurl.talon.one/`, the URL for the [updateCustomerSessionV2](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint is `https://yourbaseurl.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import talon_one
from talon_one.models.application_event import ApplicationEvent  # noqa: E501
from talon_one.rest import ApiException

class TestApplicationEvent(unittest.TestCase):
    """ApplicationEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.application_event.ApplicationEvent()  # noqa: E501
        if include_optional :
            return ApplicationEvent(
                id = 6, 
                created = '2020-06-10T09:05:27.993483Z', 
                application_id = 322, 
                profile_id = 138, 
                store_id = 56, 
                store_integration_id = 'STORE-001', 
                session_id = 56, 
                type = '0', 
                attributes = None, 
                effects = [
                    talon_one.models.effect.Effect(
                        campaign_id = 244, 
                        ruleset_id = 73, 
                        rule_index = 2, 
                        rule_name = 'Give 20% discount', 
                        effect_type = 'rejectCoupon', 
                        triggered_by_coupon = 4928, 
                        triggered_for_catalog_item = 786, 
                        condition_index = 786, 
                        props = talon_one.models.effect_props.EffectProps(), )
                    ], 
                rule_failure_reasons = [
                    talon_one.models.rule_failure_reason.RuleFailureReason(
                        campaign_id = 56, 
                        campaign_name = '0', 
                        ruleset_id = 56, 
                        coupon_id = 4928, 
                        coupon_value = '0', 
                        referral_id = 56, 
                        referral_value = '0', 
                        rule_index = 56, 
                        rule_name = '0', 
                        condition_index = 56, 
                        effect_index = 56, 
                        details = '0', )
                    ]
            )
        else :
            return ApplicationEvent(
                id = 6,
                created = '2020-06-10T09:05:27.993483Z',
                application_id = 322,
                type = '0',
                attributes = None,
                effects = [
                    talon_one.models.effect.Effect(
                        campaign_id = 244, 
                        ruleset_id = 73, 
                        rule_index = 2, 
                        rule_name = 'Give 20% discount', 
                        effect_type = 'rejectCoupon', 
                        triggered_by_coupon = 4928, 
                        triggered_for_catalog_item = 786, 
                        condition_index = 786, 
                        props = talon_one.models.effect_props.EffectProps(), )
                    ],
        )

    def testApplicationEvent(self):
        """Test ApplicationEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
