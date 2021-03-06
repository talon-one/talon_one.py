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
from talon_one.models.campaign_set import CampaignSet  # noqa: E501
from talon_one.rest import ApiException

class TestCampaignSet(unittest.TestCase):
    """CampaignSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CampaignSet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.campaign_set.CampaignSet()  # noqa: E501
        if include_optional :
            return CampaignSet(
                id = 56, 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                application_id = 56, 
                version = 1, 
                set = talon_one.models.campaign_set_branch_node.CampaignSetBranchNode(
                    type = 'SET', 
                    name = '0', 
                    operator = 'ALL', 
                    elements = [
                        talon_one.models.campaign_set_node.CampaignSetNode(
                            type = '0', )
                        ], )
            )
        else :
            return CampaignSet(
                id = 56,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                application_id = 56,
                version = 1,
                set = talon_one.models.campaign_set_branch_node.CampaignSetBranchNode(
                    type = 'SET', 
                    name = '0', 
                    operator = 'ALL', 
                    elements = [
                        talon_one.models.campaign_set_node.CampaignSetNode(
                            type = '0', )
                        ], ),
        )

    def testCampaignSet(self):
        """Test CampaignSet"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
