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


class CustomerProfileAudienceRequestItem(object):
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
        'action': 'str',
        'profile_integration_id': 'str',
        'audience_id': 'int'
    }

    attribute_map = {
        'action': 'action',
        'profile_integration_id': 'profileIntegrationId',
        'audience_id': 'audienceId'
    }

    def __init__(self, action=None, profile_integration_id=None, audience_id=None, local_vars_configuration=None):  # noqa: E501
        """CustomerProfileAudienceRequestItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._profile_integration_id = None
        self._audience_id = None
        self.discriminator = None

        self.action = action
        self.profile_integration_id = profile_integration_id
        self.audience_id = audience_id

    @property
    def action(self):
        """Gets the action of this CustomerProfileAudienceRequestItem.  # noqa: E501

        Defines the action to perform: - `add`: Adds the customer profile to the audience. - `delete`: Removes the customer profile from the audience.   # noqa: E501

        :return: The action of this CustomerProfileAudienceRequestItem.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CustomerProfileAudienceRequestItem.

        Defines the action to perform: - `add`: Adds the customer profile to the audience. - `delete`: Removes the customer profile from the audience.   # noqa: E501

        :param action: The action of this CustomerProfileAudienceRequestItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["add", "delete"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def profile_integration_id(self):
        """Gets the profile_integration_id of this CustomerProfileAudienceRequestItem.  # noqa: E501

        The ID of this customer profile in the third-party integration.  # noqa: E501

        :return: The profile_integration_id of this CustomerProfileAudienceRequestItem.  # noqa: E501
        :rtype: str
        """
        return self._profile_integration_id

    @profile_integration_id.setter
    def profile_integration_id(self, profile_integration_id):
        """Sets the profile_integration_id of this CustomerProfileAudienceRequestItem.

        The ID of this customer profile in the third-party integration.  # noqa: E501

        :param profile_integration_id: The profile_integration_id of this CustomerProfileAudienceRequestItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and profile_integration_id is None:  # noqa: E501
            raise ValueError("Invalid value for `profile_integration_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                profile_integration_id is not None and len(profile_integration_id) > 1000):
            raise ValueError("Invalid value for `profile_integration_id`, length must be less than or equal to `1000`")  # noqa: E501

        self._profile_integration_id = profile_integration_id

    @property
    def audience_id(self):
        """Gets the audience_id of this CustomerProfileAudienceRequestItem.  # noqa: E501

        The ID of the audience. You get it via the `id` property when [creating an audience](#operation/createAudienceV2).  # noqa: E501

        :return: The audience_id of this CustomerProfileAudienceRequestItem.  # noqa: E501
        :rtype: int
        """
        return self._audience_id

    @audience_id.setter
    def audience_id(self, audience_id):
        """Sets the audience_id of this CustomerProfileAudienceRequestItem.

        The ID of the audience. You get it via the `id` property when [creating an audience](#operation/createAudienceV2).  # noqa: E501

        :param audience_id: The audience_id of this CustomerProfileAudienceRequestItem.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and audience_id is None:  # noqa: E501
            raise ValueError("Invalid value for `audience_id`, must not be `None`")  # noqa: E501

        self._audience_id = audience_id

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
        if not isinstance(other, CustomerProfileAudienceRequestItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerProfileAudienceRequestItem):
            return True

        return self.to_dict() != other.to_dict()
