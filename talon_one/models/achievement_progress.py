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


class AchievementProgress(object):
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
        'status': 'str',
        'progress': 'float',
        'start_date': 'datetime',
        'completion_date': 'datetime',
        'end_date': 'datetime'
    }

    attribute_map = {
        'status': 'status',
        'progress': 'progress',
        'start_date': 'startDate',
        'completion_date': 'completionDate',
        'end_date': 'endDate'
    }

    def __init__(self, status=None, progress=None, start_date=None, completion_date=None, end_date=None, local_vars_configuration=None):  # noqa: E501
        """AchievementProgress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._progress = None
        self._start_date = None
        self._completion_date = None
        self._end_date = None
        self.discriminator = None

        self.status = status
        self.progress = progress
        if start_date is not None:
            self.start_date = start_date
        if completion_date is not None:
            self.completion_date = completion_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def status(self):
        """Gets the status of this AchievementProgress.  # noqa: E501

        The status of the achievement.  # noqa: E501

        :return: The status of this AchievementProgress.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AchievementProgress.

        The status of the achievement.  # noqa: E501

        :param status: The status of this AchievementProgress.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["inprogress", "completed", "expired", "not_started"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def progress(self):
        """Gets the progress of this AchievementProgress.  # noqa: E501

        The current progress of the customer in the achievement.  # noqa: E501

        :return: The progress of this AchievementProgress.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this AchievementProgress.

        The current progress of the customer in the achievement.  # noqa: E501

        :param progress: The progress of this AchievementProgress.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and progress is None:  # noqa: E501
            raise ValueError("Invalid value for `progress`, must not be `None`")  # noqa: E501

        self._progress = progress

    @property
    def start_date(self):
        """Gets the start_date of this AchievementProgress.  # noqa: E501

        Timestamp at which the customer started the achievement.  # noqa: E501

        :return: The start_date of this AchievementProgress.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this AchievementProgress.

        Timestamp at which the customer started the achievement.  # noqa: E501

        :param start_date: The start_date of this AchievementProgress.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def completion_date(self):
        """Gets the completion_date of this AchievementProgress.  # noqa: E501

        Timestamp at which point the customer completed the achievement.  # noqa: E501

        :return: The completion_date of this AchievementProgress.  # noqa: E501
        :rtype: datetime
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this AchievementProgress.

        Timestamp at which point the customer completed the achievement.  # noqa: E501

        :param completion_date: The completion_date of this AchievementProgress.  # noqa: E501
        :type: datetime
        """

        self._completion_date = completion_date

    @property
    def end_date(self):
        """Gets the end_date of this AchievementProgress.  # noqa: E501

        Timestamp at which point the achievement ends and resets for the customer.  # noqa: E501

        :return: The end_date of this AchievementProgress.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this AchievementProgress.

        Timestamp at which point the achievement ends and resets for the customer.  # noqa: E501

        :param end_date: The end_date of this AchievementProgress.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

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
        if not isinstance(other, AchievementProgress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AchievementProgress):
            return True

        return self.to_dict() != other.to_dict()
