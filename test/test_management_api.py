# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import talon_one
from talon_one.api.management_api import ManagementApi  # noqa: E501
from talon_one.rest import ApiException


class TestManagementApi(unittest.TestCase):
    """ManagementApi unit test stubs"""

    def setUp(self):
        self.api = talon_one.api.management_api.ManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_loyalty_points(self):
        """Test case for add_loyalty_points

        Add points in a certain loyalty program for the specified customer  # noqa: E501
        """
        pass

    def test_copy_campaign_to_applications(self):
        """Test case for copy_campaign_to_applications

        Copy the campaign into every specified application  # noqa: E501
        """
        pass

    def test_create_campaign(self):
        """Test case for create_campaign

        Create a Campaign  # noqa: E501
        """
        pass

    def test_create_coupons(self):
        """Test case for create_coupons

        Create Coupons  # noqa: E501
        """
        pass

    def test_create_password_recovery_email(self):
        """Test case for create_password_recovery_email

        Request a password reset  # noqa: E501
        """
        pass

    def test_create_ruleset(self):
        """Test case for create_ruleset

        Create a Ruleset  # noqa: E501
        """
        pass

    def test_create_session(self):
        """Test case for create_session

        Create a Session  # noqa: E501
        """
        pass

    def test_delete_campaign(self):
        """Test case for delete_campaign

        Delete a Campaign  # noqa: E501
        """
        pass

    def test_delete_coupon(self):
        """Test case for delete_coupon

        Delete one Coupon  # noqa: E501
        """
        pass

    def test_delete_coupons(self):
        """Test case for delete_coupons

        Delete Coupons  # noqa: E501
        """
        pass

    def test_delete_referral(self):
        """Test case for delete_referral

        Delete one Referral  # noqa: E501
        """
        pass

    def test_delete_ruleset(self):
        """Test case for delete_ruleset

        Delete a Ruleset  # noqa: E501
        """
        pass

    def test_get_access_logs(self):
        """Test case for get_access_logs

        Get access logs for application  # noqa: E501
        """
        pass

    def test_get_access_logs_without_total_count(self):
        """Test case for get_access_logs_without_total_count

        Get access logs for application  # noqa: E501
        """
        pass

    def test_get_account(self):
        """Test case for get_account

        Get Account Details  # noqa: E501
        """
        pass

    def test_get_account_analytics(self):
        """Test case for get_account_analytics

        Get Account Analytics  # noqa: E501
        """
        pass

    def test_get_account_limits(self):
        """Test case for get_account_limits

        Get Account Limits  # noqa: E501
        """
        pass

    def test_get_all_access_logs(self):
        """Test case for get_all_access_logs

        Get all access logs  # noqa: E501
        """
        pass

    def test_get_all_roles(self):
        """Test case for get_all_roles

        Get all roles.  # noqa: E501
        """
        pass

    def test_get_application(self):
        """Test case for get_application

        Get Application  # noqa: E501
        """
        pass

    def test_get_application_api_health(self):
        """Test case for get_application_api_health

        Get report of health of application API  # noqa: E501
        """
        pass

    def test_get_application_customer(self):
        """Test case for get_application_customer

        Get Application Customer  # noqa: E501
        """
        pass

    def test_get_application_customers(self):
        """Test case for get_application_customers

        List Application Customers  # noqa: E501
        """
        pass

    def test_get_application_customers_by_attributes(self):
        """Test case for get_application_customers_by_attributes

        Get a list of the customer profiles that match the given attributes  # noqa: E501
        """
        pass

    def test_get_application_event_types(self):
        """Test case for get_application_event_types

        List Applications Event Types  # noqa: E501
        """
        pass

    def test_get_application_events(self):
        """Test case for get_application_events

        List Applications Events  # noqa: E501
        """
        pass

    def test_get_application_events_without_total_count(self):
        """Test case for get_application_events_without_total_count

        List Applications Events  # noqa: E501
        """
        pass

    def test_get_application_session(self):
        """Test case for get_application_session

        Get Application Session  # noqa: E501
        """
        pass

    def test_get_application_sessions(self):
        """Test case for get_application_sessions

        List Application Sessions  # noqa: E501
        """
        pass

    def test_get_applications(self):
        """Test case for get_applications

        List Applications  # noqa: E501
        """
        pass

    def test_get_attribute(self):
        """Test case for get_attribute

        Get a custom attribute  # noqa: E501
        """
        pass

    def test_get_campaign(self):
        """Test case for get_campaign

        Get a Campaign  # noqa: E501
        """
        pass

    def test_get_campaign_analytics(self):
        """Test case for get_campaign_analytics

        Get analytics of campaigns  # noqa: E501
        """
        pass

    def test_get_campaign_by_attributes(self):
        """Test case for get_campaign_by_attributes

        Get a list of all campaigns that match the given attributes  # noqa: E501
        """
        pass

    def test_get_campaign_set(self):
        """Test case for get_campaign_set

        List CampaignSet  # noqa: E501
        """
        pass

    def test_get_campaigns(self):
        """Test case for get_campaigns

        List your Campaigns  # noqa: E501
        """
        pass

    def test_get_changes(self):
        """Test case for get_changes

        Get audit log for an account  # noqa: E501
        """
        pass

    def test_get_coupons(self):
        """Test case for get_coupons

        List Coupons  # noqa: E501
        """
        pass

    def test_get_coupons_by_attributes(self):
        """Test case for get_coupons_by_attributes

        Get a list of the coupons that match the given attributes  # noqa: E501
        """
        pass

    def test_get_coupons_by_attributes_application_wide(self):
        """Test case for get_coupons_by_attributes_application_wide

        Get a list of the coupons that match the given attributes in all active campaigns of an application  # noqa: E501
        """
        pass

    def test_get_coupons_without_total_count(self):
        """Test case for get_coupons_without_total_count

        List Coupons  # noqa: E501
        """
        pass

    def test_get_customer_activity_report(self):
        """Test case for get_customer_activity_report

        Get Activity Report for Single Customer  # noqa: E501
        """
        pass

    def test_get_customer_activity_reports(self):
        """Test case for get_customer_activity_reports

        Get Activity Reports for Application Customers  # noqa: E501
        """
        pass

    def test_get_customer_activity_reports_without_total_count(self):
        """Test case for get_customer_activity_reports_without_total_count

        Get Activity Reports for Application Customers  # noqa: E501
        """
        pass

    def test_get_customer_analytics(self):
        """Test case for get_customer_analytics

        Get Analytics Report for a Customer  # noqa: E501
        """
        pass

    def test_get_customer_profile(self):
        """Test case for get_customer_profile

        Get Customer Profile  # noqa: E501
        """
        pass

    def test_get_customer_profiles(self):
        """Test case for get_customer_profiles

        List Customer Profiles  # noqa: E501
        """
        pass

    def test_get_customers_by_attributes(self):
        """Test case for get_customers_by_attributes

        Get a list of the customer profiles that match the given attributes  # noqa: E501
        """
        pass

    def test_get_event_types(self):
        """Test case for get_event_types

        List Event Types  # noqa: E501
        """
        pass

    def test_get_exports(self):
        """Test case for get_exports

        Get Exports  # noqa: E501
        """
        pass

    def test_get_imports(self):
        """Test case for get_imports

        Get Imports  # noqa: E501
        """
        pass

    def test_get_loyalty_points(self):
        """Test case for get_loyalty_points

        get the Loyalty Ledger for this integrationID  # noqa: E501
        """
        pass

    def test_get_loyalty_program(self):
        """Test case for get_loyalty_program

        Get a loyalty program  # noqa: E501
        """
        pass

    def test_get_loyalty_programs(self):
        """Test case for get_loyalty_programs

        List all loyalty Programs  # noqa: E501
        """
        pass

    def test_get_referrals(self):
        """Test case for get_referrals

        List Referrals  # noqa: E501
        """
        pass

    def test_get_referrals_without_total_count(self):
        """Test case for get_referrals_without_total_count

        List Referrals  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        Get information for the specified role.  # noqa: E501
        """
        pass

    def test_get_ruleset(self):
        """Test case for get_ruleset

        Get a Ruleset  # noqa: E501
        """
        pass

    def test_get_rulesets(self):
        """Test case for get_rulesets

        List Campaign Rulesets  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get a single User  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        List Users in your account  # noqa: E501
        """
        pass

    def test_get_webhook(self):
        """Test case for get_webhook

        Get Webhook  # noqa: E501
        """
        pass

    def test_get_webhook_activation_logs(self):
        """Test case for get_webhook_activation_logs

        List Webhook activation Log Entries  # noqa: E501
        """
        pass

    def test_get_webhook_logs(self):
        """Test case for get_webhook_logs

        List Webhook Log Entries  # noqa: E501
        """
        pass

    def test_get_webhooks(self):
        """Test case for get_webhooks

        List Webhooks  # noqa: E501
        """
        pass

    def test_refresh_analytics(self):
        """Test case for refresh_analytics

        Trigger refresh on stale analytics.  # noqa: E501
        """
        pass

    def test_remove_loyalty_points(self):
        """Test case for remove_loyalty_points

        Deduct points in a certain loyalty program for the specified customer  # noqa: E501
        """
        pass

    def test_reset_password(self):
        """Test case for reset_password

        Reset password  # noqa: E501
        """
        pass

    def test_search_coupons_advanced(self):
        """Test case for search_coupons_advanced

        Get a list of the coupons that match the given attributes  # noqa: E501
        """
        pass

    def test_search_coupons_advanced_application_wide(self):
        """Test case for search_coupons_advanced_application_wide

        Get a list of the coupons that match the given attributes in all active campaigns of an application  # noqa: E501
        """
        pass

    def test_search_coupons_advanced_application_wide_without_total_count(self):
        """Test case for search_coupons_advanced_application_wide_without_total_count

        Get a list of the coupons that match the given attributes in all active campaigns of an application  # noqa: E501
        """
        pass

    def test_search_coupons_advanced_without_total_count(self):
        """Test case for search_coupons_advanced_without_total_count

        Get a list of the coupons that match the given attributes  # noqa: E501
        """
        pass

    def test_set_account_limits(self):
        """Test case for set_account_limits

        Set account limits  # noqa: E501
        """
        pass

    def test_update_campaign(self):
        """Test case for update_campaign

        Update a Campaign  # noqa: E501
        """
        pass

    def test_update_campaign_set(self):
        """Test case for update_campaign_set

        Update a Campaign Set  # noqa: E501
        """
        pass

    def test_update_coupon(self):
        """Test case for update_coupon

        Update a Coupon  # noqa: E501
        """
        pass

    def test_update_coupon_batch(self):
        """Test case for update_coupon_batch

        Update a Batch of Coupons  # noqa: E501
        """
        pass

    def test_update_ruleset(self):
        """Test case for update_ruleset

        Update a Ruleset  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()