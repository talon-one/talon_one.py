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
from talon_one.models.application_campaign_analytics import ApplicationCampaignAnalytics  # noqa: E501
from talon_one.rest import ApiException

class TestApplicationCampaignAnalytics(unittest.TestCase):
    """ApplicationCampaignAnalytics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationCampaignAnalytics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.application_campaign_analytics.ApplicationCampaignAnalytics()  # noqa: E501
        if include_optional :
            return ApplicationCampaignAnalytics(
                start_time = '2024-02-01T00:00Z', 
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                campaign_id = 1, 
                campaign_name = 'Summer promotions', 
                campaign_tags = [summer], 
                campaign_state = 'running', 
                total_revenue = talon_one.models.analytics_data_point_with_trend_and_influenced_rate.AnalyticsDataPointWithTrendAndInfluencedRate(
                    value = 12.0, 
                    influenced_rate = 12.0, 
                    trend = 3.25, ), 
                sessions_count = talon_one.models.analytics_data_point_with_trend_and_influenced_rate.AnalyticsDataPointWithTrendAndInfluencedRate(
                    value = 12.0, 
                    influenced_rate = 12.0, 
                    trend = 3.25, ), 
                avg_items_per_session = talon_one.models.analytics_data_point_with_trend_and_uplift.AnalyticsDataPointWithTrendAndUplift(
                    value = 12.0, 
                    uplift = 3.25, 
                    trend = 3.25, ), 
                avg_session_value = talon_one.models.analytics_data_point_with_trend_and_uplift.AnalyticsDataPointWithTrendAndUplift(
                    value = 12.0, 
                    uplift = 3.25, 
                    trend = 3.25, ), 
                total_discounts = talon_one.models.analytics_data_point_with_trend.AnalyticsDataPointWithTrend(
                    value = 12.0, 
                    trend = 3.25, ), 
                coupons_count = talon_one.models.analytics_data_point_with_trend.AnalyticsDataPointWithTrend(
                    value = 12.0, 
                    trend = 3.25, )
            )
        else :
            return ApplicationCampaignAnalytics(
                start_time = '2024-02-01T00:00Z',
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                campaign_id = 1,
                campaign_name = 'Summer promotions',
                campaign_tags = [summer],
                campaign_state = 'running',
        )

    def testApplicationCampaignAnalytics(self):
        """Test ApplicationCampaignAnalytics"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
