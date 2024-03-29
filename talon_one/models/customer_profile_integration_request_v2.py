# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you access the Campaign Manager at `https://yourbaseurl.talon.one/`, the URL for the [updateCustomerSessionV2](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint is `https://yourbaseurl.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class CustomerProfileIntegrationRequestV2(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'attributes': 'object',
        'evaluable_campaign_ids': 'list[int]',
        'audiences_changes': 'ProfileAudiencesChanges',
        'response_content': 'list[str]'
    }

    attribute_map = {
        'attributes': 'attributes',
        'evaluable_campaign_ids': 'evaluableCampaignIds',
        'audiences_changes': 'audiencesChanges',
        'response_content': 'responseContent'
    }

    def __init__(self, attributes=None, evaluable_campaign_ids=None, audiences_changes=None, response_content=None, local_vars_configuration=None):  # noqa: E501
        """CustomerProfileIntegrationRequestV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attributes = None
        self._evaluable_campaign_ids = None
        self._audiences_changes = None
        self._response_content = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if evaluable_campaign_ids is not None:
            self.evaluable_campaign_ids = evaluable_campaign_ids
        if audiences_changes is not None:
            self.audiences_changes = audiences_changes
        if response_content is not None:
            self.response_content = response_content

    @property
    def attributes(self):
        """Gets the attributes of this CustomerProfileIntegrationRequestV2.  # noqa: E501

        Arbitrary properties associated with this item.  # noqa: E501

        :return: The attributes of this CustomerProfileIntegrationRequestV2.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CustomerProfileIntegrationRequestV2.

        Arbitrary properties associated with this item.  # noqa: E501

        :param attributes: The attributes of this CustomerProfileIntegrationRequestV2.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def evaluable_campaign_ids(self):
        """Gets the evaluable_campaign_ids of this CustomerProfileIntegrationRequestV2.  # noqa: E501

        When using the `dry` query parameter, use this property to list the campaign to be evaluated by the Rule Engine.  These campaigns will be evaluated, even if they are disabled, allowing you to test specific campaigns before activating them.   # noqa: E501

        :return: The evaluable_campaign_ids of this CustomerProfileIntegrationRequestV2.  # noqa: E501
        :rtype: list[int]
        """
        return self._evaluable_campaign_ids

    @evaluable_campaign_ids.setter
    def evaluable_campaign_ids(self, evaluable_campaign_ids):
        """Sets the evaluable_campaign_ids of this CustomerProfileIntegrationRequestV2.

        When using the `dry` query parameter, use this property to list the campaign to be evaluated by the Rule Engine.  These campaigns will be evaluated, even if they are disabled, allowing you to test specific campaigns before activating them.   # noqa: E501

        :param evaluable_campaign_ids: The evaluable_campaign_ids of this CustomerProfileIntegrationRequestV2.  # noqa: E501
        :type: list[int]
        """

        self._evaluable_campaign_ids = evaluable_campaign_ids

    @property
    def audiences_changes(self):
        """Gets the audiences_changes of this CustomerProfileIntegrationRequestV2.  # noqa: E501


        :return: The audiences_changes of this CustomerProfileIntegrationRequestV2.  # noqa: E501
        :rtype: ProfileAudiencesChanges
        """
        return self._audiences_changes

    @audiences_changes.setter
    def audiences_changes(self, audiences_changes):
        """Sets the audiences_changes of this CustomerProfileIntegrationRequestV2.


        :param audiences_changes: The audiences_changes of this CustomerProfileIntegrationRequestV2.  # noqa: E501
        :type: ProfileAudiencesChanges
        """

        self._audiences_changes = audiences_changes

    @property
    def response_content(self):
        """Gets the response_content of this CustomerProfileIntegrationRequestV2.  # noqa: E501

        Extends the response with the chosen data entities. Use this property to get as much data as you need in one _Update customer profile_ request instead of sending extra requests to other endpoints.   # noqa: E501

        :return: The response_content of this CustomerProfileIntegrationRequestV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._response_content

    @response_content.setter
    def response_content(self, response_content):
        """Sets the response_content of this CustomerProfileIntegrationRequestV2.

        Extends the response with the chosen data entities. Use this property to get as much data as you need in one _Update customer profile_ request instead of sending extra requests to other endpoints.   # noqa: E501

        :param response_content: The response_content of this CustomerProfileIntegrationRequestV2.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["customerProfile", "triggeredCampaigns", "loyalty", "event", "awardedGiveaways", "ruleFailureReasons"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(response_content).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `response_content` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(response_content) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._response_content = response_content

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomerProfileIntegrationRequestV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerProfileIntegrationRequestV2):
            return True

        return self.to_dict() != other.to_dict()
