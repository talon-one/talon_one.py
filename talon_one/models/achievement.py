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


class Achievement(object):
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
        'id': 'int',
        'created': 'datetime',
        'name': 'str',
        'title': 'str',
        'description': 'str',
        'target': 'float',
        'period': 'str',
        'period_end_override': 'TimePoint',
        'campaign_id': 'int',
        'user_id': 'int',
        'created_by': 'str',
        'has_progress': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'name': 'name',
        'title': 'title',
        'description': 'description',
        'target': 'target',
        'period': 'period',
        'period_end_override': 'periodEndOverride',
        'campaign_id': 'campaignId',
        'user_id': 'userId',
        'created_by': 'createdBy',
        'has_progress': 'hasProgress'
    }

    def __init__(self, id=None, created=None, name=None, title=None, description=None, target=None, period=None, period_end_override=None, campaign_id=None, user_id=None, created_by=None, has_progress=None, local_vars_configuration=None):  # noqa: E501
        """Achievement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._name = None
        self._title = None
        self._description = None
        self._target = None
        self._period = None
        self._period_end_override = None
        self._campaign_id = None
        self._user_id = None
        self._created_by = None
        self._has_progress = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.name = name
        self.title = title
        self.description = description
        self.target = target
        self.period = period
        if period_end_override is not None:
            self.period_end_override = period_end_override
        self.campaign_id = campaign_id
        self.user_id = user_id
        self.created_by = created_by
        if has_progress is not None:
            self.has_progress = has_progress

    @property
    def id(self):
        """Gets the id of this Achievement.  # noqa: E501

        Internal ID of this entity.  # noqa: E501

        :return: The id of this Achievement.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Achievement.

        Internal ID of this entity.  # noqa: E501

        :param id: The id of this Achievement.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Achievement.  # noqa: E501

        The time this entity was created.  # noqa: E501

        :return: The created of this Achievement.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Achievement.

        The time this entity was created.  # noqa: E501

        :param created: The created of this Achievement.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def name(self):
        """Gets the name of this Achievement.  # noqa: E501

        The internal name of the achievement used in API requests.  **Note**: The name should start with a letter. This cannot be changed after the achievement has been created.   # noqa: E501

        :return: The name of this Achievement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Achievement.

        The internal name of the achievement used in API requests.  **Note**: The name should start with a letter. This cannot be changed after the achievement has been created.   # noqa: E501

        :param name: The name of this Achievement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 1000):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[a-zA-Z]\w+$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z]\w+$/`")  # noqa: E501

        self._name = name

    @property
    def title(self):
        """Gets the title of this Achievement.  # noqa: E501

        The display name for the achievement in the Campaign Manager.  # noqa: E501

        :return: The title of this Achievement.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Achievement.

        The display name for the achievement in the Campaign Manager.  # noqa: E501

        :param title: The title of this Achievement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this Achievement.  # noqa: E501

        A description of the achievement.  # noqa: E501

        :return: The description of this Achievement.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Achievement.

        A description of the achievement.  # noqa: E501

        :param description: The description of this Achievement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def target(self):
        """Gets the target of this Achievement.  # noqa: E501

        The required number of actions or the transactional milestone to complete the achievement.  # noqa: E501

        :return: The target of this Achievement.  # noqa: E501
        :rtype: float
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this Achievement.

        The required number of actions or the transactional milestone to complete the achievement.  # noqa: E501

        :param target: The target of this Achievement.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and target is None:  # noqa: E501
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

    @property
    def period(self):
        """Gets the period of this Achievement.  # noqa: E501

        The relative duration after which the achievement ends and resets for a particular customer profile.  **Note**: The `period` does not start when the achievement is created.  The period is a **positive real number** followed by one letter indicating the time unit.  Examples: `30s`, `40m`, `1h`, `5D`, `7W`, `10M`, `15Y`.  Available units:  - `s`: seconds - `m`: minutes - `h`: hours - `D`: days - `W`: weeks - `M`: months - `Y`: years  You can also round certain units down to the beginning of period and up to the end of period.: - `_D` for rounding down days only. Signifies the start of the day. Example: `30D_D` - `_U` for rounding up days, weeks, months and years. Signifies the end of the day, week, month or year. Example: `23W_U`  **Note**: You can either use the round down and round up option or set an absolute period.   # noqa: E501

        :return: The period of this Achievement.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Achievement.

        The relative duration after which the achievement ends and resets for a particular customer profile.  **Note**: The `period` does not start when the achievement is created.  The period is a **positive real number** followed by one letter indicating the time unit.  Examples: `30s`, `40m`, `1h`, `5D`, `7W`, `10M`, `15Y`.  Available units:  - `s`: seconds - `m`: minutes - `h`: hours - `D`: days - `W`: weeks - `M`: months - `Y`: years  You can also round certain units down to the beginning of period and up to the end of period.: - `_D` for rounding down days only. Signifies the start of the day. Example: `30D_D` - `_U` for rounding up days, weeks, months and years. Signifies the end of the day, week, month or year. Example: `23W_U`  **Note**: You can either use the round down and round up option or set an absolute period.   # noqa: E501

        :param period: The period of this Achievement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and period is None:  # noqa: E501
            raise ValueError("Invalid value for `period`, must not be `None`")  # noqa: E501

        self._period = period

    @property
    def period_end_override(self):
        """Gets the period_end_override of this Achievement.  # noqa: E501


        :return: The period_end_override of this Achievement.  # noqa: E501
        :rtype: TimePoint
        """
        return self._period_end_override

    @period_end_override.setter
    def period_end_override(self, period_end_override):
        """Sets the period_end_override of this Achievement.


        :param period_end_override: The period_end_override of this Achievement.  # noqa: E501
        :type: TimePoint
        """

        self._period_end_override = period_end_override

    @property
    def campaign_id(self):
        """Gets the campaign_id of this Achievement.  # noqa: E501

        ID of the campaign, to which the achievement belongs to  # noqa: E501

        :return: The campaign_id of this Achievement.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this Achievement.

        ID of the campaign, to which the achievement belongs to  # noqa: E501

        :param campaign_id: The campaign_id of this Achievement.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and campaign_id is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")  # noqa: E501

        self._campaign_id = campaign_id

    @property
    def user_id(self):
        """Gets the user_id of this Achievement.  # noqa: E501

        ID of the user that created this achievement.  # noqa: E501

        :return: The user_id of this Achievement.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Achievement.

        ID of the user that created this achievement.  # noqa: E501

        :param user_id: The user_id of this Achievement.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def created_by(self):
        """Gets the created_by of this Achievement.  # noqa: E501

        Name of the user that created the achievement.  **Note**: This is not available if the user has been deleted.   # noqa: E501

        :return: The created_by of this Achievement.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Achievement.

        Name of the user that created the achievement.  **Note**: This is not available if the user has been deleted.   # noqa: E501

        :param created_by: The created_by of this Achievement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def has_progress(self):
        """Gets the has_progress of this Achievement.  # noqa: E501

        Indicates if a customer has made progress in the achievement.  # noqa: E501

        :return: The has_progress of this Achievement.  # noqa: E501
        :rtype: bool
        """
        return self._has_progress

    @has_progress.setter
    def has_progress(self, has_progress):
        """Sets the has_progress of this Achievement.

        Indicates if a customer has made progress in the achievement.  # noqa: E501

        :param has_progress: The has_progress of this Achievement.  # noqa: E501
        :type: bool
        """

        self._has_progress = has_progress

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
        if not isinstance(other, Achievement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Achievement):
            return True

        return self.to_dict() != other.to_dict()
