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
from talon_one.models.environment import Environment  # noqa: E501
from talon_one.rest import ApiException

class TestEnvironment(unittest.TestCase):
    """Environment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Environment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.environment.Environment()  # noqa: E501
        if include_optional :
            return Environment(
                id = 6, 
                created = '2020-06-10T09:05:27.993483Z', 
                application_id = 322, 
                slots = [
                    talon_one.models.slot_def.SlotDef(
                        name = '0', 
                        type = '0', 
                        title = '0', 
                        description = '0', 
                        help = '0', 
                        writable = True, )
                    ], 
                functions = [
                    talon_one.models.function_def.FunctionDef(
                        name = '0', 
                        type = '0', 
                        description = '0', 
                        help = '0', 
                        args = [
                            talon_one.models.func_arg_def.FuncArgDef(
                                type = 'string', 
                                description = '0', )
                            ], )
                    ], 
                templates = [
                    talon_one.models.template_def.TemplateDef(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        application_id = 322, 
                        title = '0', 
                        description = '0', 
                        help = '0', 
                        category = '0', 
                        expr = [
                            None
                            ], 
                        args = [
                            talon_one.models.template_arg_def.TemplateArgDef(
                                type = 'string', 
                                description = '0', 
                                title = '0', 
                                ui = talon_one.models.ui.ui(), 
                                picklist_id = 56, 
                                restricted_by_picklist = True, )
                            ], 
                        expose = True, 
                        name = '0', )
                    ], 
                variables = '0', 
                giveaways_pools = [
                    talon_one.models.giveaways_pool.GiveawaysPool(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        account_id = 3886, 
                        name = 'My giveaway pool', 
                        description = 'Generic pool', 
                        subscribed_applications_ids = [2, 4], 
                        sandbox = True, 
                        modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by = 56, 
                        modified_by = 56, )
                    ], 
                loyalty_programs = [
                    talon_one.models.loyalty_program.LoyaltyProgram(
                        id = 56, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        title = 'Point collection', 
                        description = 'Customers collect 10 points per 1$ spent', 
                        subscribed_applications = [132, 97], 
                        default_validity = '2W_U', 
                        default_pending = 'immediate', 
                        allow_subledger = False, 
                        users_per_card_limit = 111, 
                        sandbox = True, 
                        program_join_policy = 'not_join', 
                        tiers_expiration_policy = 'tier_start_date', 
                        tiers_start_date = '2021-09-12T10:12:42Z', 
                        tiers_expire_in = '27W_U', 
                        tiers_downgrade_policy = 'one_down', 
                        card_code_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                            valid_characters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                            coupon_pattern = 'SUMMER-####-####', ), 
                        account_id = 1, 
                        name = 'my_program', 
                        tiers = [{name=Gold, minPoints=300, id=3, created=2021-06-10T09:05:27.993483Z, programID=139}, {name=Silver, minPoints=200, id=2, created=2021-06-10T09:04:59.355258Z, programId=139}, {name=Bronze, minPoints=100, id=1, created=2021-06-10T09:04:39.355258Z, programId=139}], 
                        timezone = 'Europe/Berlin', 
                        card_based = True, 
                        can_update_tiers = True, 
                        can_update_join_policy = True, 
                        can_update_tier_expiration_policy = True, 
                        can_upgrade_to_advanced_tiers = True, )
                    ], 
                achievements = [
                    talon_one.models.achievement.Achievement(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        name = 'Order50Discount', 
                        title = '50% off on 50th purchase.', 
                        description = '50% off for every 50th purchase in a year.', 
                        target = 50.0, 
                        period = '1Y', 
                        period_end_override = {month=11, dayOfMonth=23, hour=23, minute=59, second=59}, 
                        campaign_id = 1, 
                        user_id = 1234, 
                        created_by = 'John Doe', 
                        has_progress = True, )
                    ], 
                attributes = [
                    talon_one.models.attribute.Attribute(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        account_id = 3886, 
                        entity = 'Event', 
                        event_type = 'pageViewed', 
                        name = 'pageViewed', 
                        title = 'Page view event', 
                        type = 'string', 
                        description = 'Event triggered when a customer displays a page.', 
                        suggestions = [
                            '0'
                            ], 
                        has_allowed_list = False, 
                        restricted_by_suggestions = False, 
                        editable = True, 
                        subscribed_applications_ids = [1, 4, 9], 
                        subscribed_catalogs_ids = [2, 5], 
                        allowed_subscriptions = [application, catalog], 
                        event_type_id = 22, )
                    ], 
                additional_costs = [
                    talon_one.models.account_additional_cost.AccountAdditionalCost(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        account_id = 3886, 
                        name = 'shippingFee', 
                        title = 'Shipping fee', 
                        description = 'A shipping fee', 
                        subscribed_applications_ids = [3, 13], 
                        type = 'session', )
                    ], 
                audiences = [
                    talon_one.models.audience.Audience(
                        account_id = 3886, 
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        name = 'Travel audience', 
                        sandbox = True, 
                        description = 'Travel audience 18-27', 
                        integration = 'mparticle', 
                        integration_id = '382370BKDB946', 
                        created_in3rd_party = False, 
                        last_update = '2022-04-26T11:02:38Z', )
                    ], 
                collections = [
                    talon_one.models.collection.Collection(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        account_id = 3886, 
                        modified = '2021-09-12T10:12:42Z', 
                        description = 'My collection of SKUs', 
                        subscribed_applications_ids = [1, 2, 3], 
                        name = 'My collection', 
                        modified_by = 48, 
                        created_by = 134, 
                        application_id = 1, 
                        campaign_id = 7, 
                        payload = [KTL-WH-ET-1, KTL-BL-ET-1], )
                    ]
            )
        else :
            return Environment(
                id = 6,
                created = '2020-06-10T09:05:27.993483Z',
                application_id = 322,
                slots = [
                    talon_one.models.slot_def.SlotDef(
                        name = '0', 
                        type = '0', 
                        title = '0', 
                        description = '0', 
                        help = '0', 
                        writable = True, )
                    ],
                functions = [
                    talon_one.models.function_def.FunctionDef(
                        name = '0', 
                        type = '0', 
                        description = '0', 
                        help = '0', 
                        args = [
                            talon_one.models.func_arg_def.FuncArgDef(
                                type = 'string', 
                                description = '0', )
                            ], )
                    ],
                templates = [
                    talon_one.models.template_def.TemplateDef(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        application_id = 322, 
                        title = '0', 
                        description = '0', 
                        help = '0', 
                        category = '0', 
                        expr = [
                            None
                            ], 
                        args = [
                            talon_one.models.template_arg_def.TemplateArgDef(
                                type = 'string', 
                                description = '0', 
                                title = '0', 
                                ui = talon_one.models.ui.ui(), 
                                picklist_id = 56, 
                                restricted_by_picklist = True, )
                            ], 
                        expose = True, 
                        name = '0', )
                    ],
                variables = '0',
        )

    def testEnvironment(self):
        """Test Environment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
