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


class ApplicationCampaignStats(object):
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
        'draft': 'int',
        'disabled': 'int',
        'scheduled': 'int',
        'running': 'int',
        'expired': 'int',
        'archived': 'int'
    }

    attribute_map = {
        'draft': 'draft',
        'disabled': 'disabled',
        'scheduled': 'scheduled',
        'running': 'running',
        'expired': 'expired',
        'archived': 'archived'
    }

    def __init__(self, draft=None, disabled=None, scheduled=None, running=None, expired=None, archived=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationCampaignStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._draft = None
        self._disabled = None
        self._scheduled = None
        self._running = None
        self._expired = None
        self._archived = None
        self.discriminator = None

        self.draft = draft
        self.disabled = disabled
        self.scheduled = scheduled
        self.running = running
        self.expired = expired
        self.archived = archived

    @property
    def draft(self):
        """Gets the draft of this ApplicationCampaignStats.  # noqa: E501

        Number of draft campaigns.  # noqa: E501

        :return: The draft of this ApplicationCampaignStats.  # noqa: E501
        :rtype: int
        """
        return self._draft

    @draft.setter
    def draft(self, draft):
        """Sets the draft of this ApplicationCampaignStats.

        Number of draft campaigns.  # noqa: E501

        :param draft: The draft of this ApplicationCampaignStats.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and draft is None:  # noqa: E501
            raise ValueError("Invalid value for `draft`, must not be `None`")  # noqa: E501

        self._draft = draft

    @property
    def disabled(self):
        """Gets the disabled of this ApplicationCampaignStats.  # noqa: E501

        Number of disabled campaigns.  # noqa: E501

        :return: The disabled of this ApplicationCampaignStats.  # noqa: E501
        :rtype: int
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this ApplicationCampaignStats.

        Number of disabled campaigns.  # noqa: E501

        :param disabled: The disabled of this ApplicationCampaignStats.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and disabled is None:  # noqa: E501
            raise ValueError("Invalid value for `disabled`, must not be `None`")  # noqa: E501

        self._disabled = disabled

    @property
    def scheduled(self):
        """Gets the scheduled of this ApplicationCampaignStats.  # noqa: E501

        Number of scheduled campaigns.  # noqa: E501

        :return: The scheduled of this ApplicationCampaignStats.  # noqa: E501
        :rtype: int
        """
        return self._scheduled

    @scheduled.setter
    def scheduled(self, scheduled):
        """Sets the scheduled of this ApplicationCampaignStats.

        Number of scheduled campaigns.  # noqa: E501

        :param scheduled: The scheduled of this ApplicationCampaignStats.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and scheduled is None:  # noqa: E501
            raise ValueError("Invalid value for `scheduled`, must not be `None`")  # noqa: E501

        self._scheduled = scheduled

    @property
    def running(self):
        """Gets the running of this ApplicationCampaignStats.  # noqa: E501

        Number of running campaigns.  # noqa: E501

        :return: The running of this ApplicationCampaignStats.  # noqa: E501
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this ApplicationCampaignStats.

        Number of running campaigns.  # noqa: E501

        :param running: The running of this ApplicationCampaignStats.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and running is None:  # noqa: E501
            raise ValueError("Invalid value for `running`, must not be `None`")  # noqa: E501

        self._running = running

    @property
    def expired(self):
        """Gets the expired of this ApplicationCampaignStats.  # noqa: E501

        Number of expired campaigns.  # noqa: E501

        :return: The expired of this ApplicationCampaignStats.  # noqa: E501
        :rtype: int
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this ApplicationCampaignStats.

        Number of expired campaigns.  # noqa: E501

        :param expired: The expired of this ApplicationCampaignStats.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and expired is None:  # noqa: E501
            raise ValueError("Invalid value for `expired`, must not be `None`")  # noqa: E501

        self._expired = expired

    @property
    def archived(self):
        """Gets the archived of this ApplicationCampaignStats.  # noqa: E501

        Number of archived campaigns.  # noqa: E501

        :return: The archived of this ApplicationCampaignStats.  # noqa: E501
        :rtype: int
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this ApplicationCampaignStats.

        Number of archived campaigns.  # noqa: E501

        :param archived: The archived of this ApplicationCampaignStats.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and archived is None:  # noqa: E501
            raise ValueError("Invalid value for `archived`, must not be `None`")  # noqa: E501

        self._archived = archived

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
        if not isinstance(other, ApplicationCampaignStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationCampaignStats):
            return True

        return self.to_dict() != other.to_dict()
