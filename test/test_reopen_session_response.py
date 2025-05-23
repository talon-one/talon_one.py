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
from talon_one.models.reopen_session_response import ReopenSessionResponse  # noqa: E501
from talon_one.rest import ApiException

class TestReopenSessionResponse(unittest.TestCase):
    """ReopenSessionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReopenSessionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.reopen_session_response.ReopenSessionResponse()  # noqa: E501
        if include_optional :
            return ReopenSessionResponse(
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
                        evaluation_group_id = 3, 
                        evaluation_group_mode = 'stackable', 
                        campaign_revision_id = 1, 
                        campaign_revision_version_id = 5, 
                        props = talon_one.models.props.props(), )
                    ]
            )
        else :
            return ReopenSessionResponse(
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
                        evaluation_group_id = 3, 
                        evaluation_group_mode = 'stackable', 
                        campaign_revision_id = 1, 
                        campaign_revision_version_id = 5, 
                        props = talon_one.models.props.props(), )
                    ],
        )

    def testReopenSessionResponse(self):
        """Test ReopenSessionResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
