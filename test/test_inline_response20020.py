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
from talon_one.models.inline_response20020 import InlineResponse20020  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse20020(unittest.TestCase):
    """InlineResponse20020 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20020
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response20020.InlineResponse20020()  # noqa: E501
        if include_optional :
            return InlineResponse20020(
                total_result_size = 56, 
                data = [
                    talon_one.models.attribute.Attribute(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        account_id = 56, 
                        entity = 'Account', 
                        event_type = '0', 
                        name = '0', 
                        title = '0', 
                        type = 'string', 
                        description = '0', 
                        suggestions = [
                            '0'
                            ], 
                        editable = True, 
                        subscribed_applications_ids = [
                            56
                            ], )
                    ]
            )
        else :
            return InlineResponse20020(
                total_result_size = 56,
                data = [
                    talon_one.models.attribute.Attribute(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        account_id = 56, 
                        entity = 'Account', 
                        event_type = '0', 
                        name = '0', 
                        title = '0', 
                        type = 'string', 
                        description = '0', 
                        suggestions = [
                            '0'
                            ], 
                        editable = True, 
                        subscribed_applications_ids = [
                            56
                            ], )
                    ],
        )

    def testInlineResponse20020(self):
        """Test InlineResponse20020"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
