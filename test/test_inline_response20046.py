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
from talon_one.models.inline_response20046 import InlineResponse20046  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse20046(unittest.TestCase):
    """InlineResponse20046 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20046
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response20046.InlineResponse20046()  # noqa: E501
        if include_optional :
            return InlineResponse20046(
                total_result_size = 1, 
                data = [
                    talon_one.models.role_v2.RoleV2(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        modified = '2021-09-12T10:12:42Z', 
                        account_id = 3886, 
                        name = 'Campaign and campaign access group manager', 
                        description = 'Allows you to create and edit campaigns for specific Applications, delete specific campaign access groups, and view loyalty programs.', 
                        permissions = talon_one.models.role_v2_permissions.RoleV2Permissions(
                            permission_sets = [{name=Application permission set, logicalOperations=[getApplicationOperations, editApplicationOperations]}, {name=Campaign manager permission set, logicalOperations=[getCampaignOperations, createCampaignOperations, updateCampaignOperations]}, {name=Campaign read-only permission set, logicalOperations=[getCampaignOperations]}, {name=Loyalty program read-only permission set, logicalOperations=[getLoyaltyProgramOperations]}, {name=Campaign access group manager permission set, logicalOperations=[getCampaignAccessGroupOperations, updateCampaignAccessGroupOperations, deleteCampaignAccessGroupOperations]}], 
                            roles = talon_one.models.role_v2_roles_group.RoleV2RolesGroup(
                                applications = {1={application=Application permission set}, 3={campaign=Campaign manager permission set}, 4={draftCampaign=Campaign read-only permission set}, 5={tools=Tools permission set}}, 
                                loyalty_programs = {10=Loyalty program manager permission set}, 
                                campaign_access_groups = {5=Campaign access group manager permission set}, ), ), 
                        members = [10, 12], )
                    ]
            )
        else :
            return InlineResponse20046(
                total_result_size = 1,
                data = [
                    talon_one.models.role_v2.RoleV2(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        modified = '2021-09-12T10:12:42Z', 
                        account_id = 3886, 
                        name = 'Campaign and campaign access group manager', 
                        description = 'Allows you to create and edit campaigns for specific Applications, delete specific campaign access groups, and view loyalty programs.', 
                        permissions = talon_one.models.role_v2_permissions.RoleV2Permissions(
                            permission_sets = [{name=Application permission set, logicalOperations=[getApplicationOperations, editApplicationOperations]}, {name=Campaign manager permission set, logicalOperations=[getCampaignOperations, createCampaignOperations, updateCampaignOperations]}, {name=Campaign read-only permission set, logicalOperations=[getCampaignOperations]}, {name=Loyalty program read-only permission set, logicalOperations=[getLoyaltyProgramOperations]}, {name=Campaign access group manager permission set, logicalOperations=[getCampaignAccessGroupOperations, updateCampaignAccessGroupOperations, deleteCampaignAccessGroupOperations]}], 
                            roles = talon_one.models.role_v2_roles_group.RoleV2RolesGroup(
                                applications = {1={application=Application permission set}, 3={campaign=Campaign manager permission set}, 4={draftCampaign=Campaign read-only permission set}, 5={tools=Tools permission set}}, 
                                loyalty_programs = {10=Loyalty program manager permission set}, 
                                campaign_access_groups = {5=Campaign access group manager permission set}, ), ), 
                        members = [10, 12], )
                    ],
        )

    def testInlineResponse20046(self):
        """Test InlineResponse20046"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
