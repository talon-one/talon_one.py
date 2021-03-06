# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class AccountAdditionalCost(object):
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
        'account_id': 'int',
        'name': 'str',
        'title': 'str',
        'description': 'str',
        'subscribed_applications_ids': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'account_id': 'accountId',
        'name': 'name',
        'title': 'title',
        'description': 'description',
        'subscribed_applications_ids': 'subscribedApplicationsIds'
    }

    def __init__(self, id=None, created=None, account_id=None, name=None, title=None, description=None, subscribed_applications_ids=None, local_vars_configuration=None):  # noqa: E501
        """AccountAdditionalCost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._account_id = None
        self._name = None
        self._title = None
        self._description = None
        self._subscribed_applications_ids = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.account_id = account_id
        self.name = name
        self.title = title
        self.description = description
        if subscribed_applications_ids is not None:
            self.subscribed_applications_ids = subscribed_applications_ids

    @property
    def id(self):
        """Gets the id of this AccountAdditionalCost.  # noqa: E501

        Unique ID for this entity.  # noqa: E501

        :return: The id of this AccountAdditionalCost.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountAdditionalCost.

        Unique ID for this entity.  # noqa: E501

        :param id: The id of this AccountAdditionalCost.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this AccountAdditionalCost.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this AccountAdditionalCost.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AccountAdditionalCost.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this AccountAdditionalCost.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def account_id(self):
        """Gets the account_id of this AccountAdditionalCost.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The account_id of this AccountAdditionalCost.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountAdditionalCost.

        The ID of the account that owns this entity.  # noqa: E501

        :param account_id: The account_id of this AccountAdditionalCost.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this AccountAdditionalCost.  # noqa: E501

        The additional cost name that will be used in API requests and Talang. E.g. if `name == \"shipping\"` then you would set the shipping additional cost by including an `additionalCosts.shipping` property in your request payload.  # noqa: E501

        :return: The name of this AccountAdditionalCost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountAdditionalCost.

        The additional cost name that will be used in API requests and Talang. E.g. if `name == \"shipping\"` then you would set the shipping additional cost by including an `additionalCosts.shipping` property in your request payload.  # noqa: E501

        :param name: The name of this AccountAdditionalCost.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def title(self):
        """Gets the title of this AccountAdditionalCost.  # noqa: E501

        The human-readable name for the additional cost that will be shown in the Campaign Manager. Like `name`, the combination of entity and title must also be unique.  # noqa: E501

        :return: The title of this AccountAdditionalCost.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AccountAdditionalCost.

        The human-readable name for the additional cost that will be shown in the Campaign Manager. Like `name`, the combination of entity and title must also be unique.  # noqa: E501

        :param title: The title of this AccountAdditionalCost.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this AccountAdditionalCost.  # noqa: E501

        A description of this additional cost.  # noqa: E501

        :return: The description of this AccountAdditionalCost.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccountAdditionalCost.

        A description of this additional cost.  # noqa: E501

        :param description: The description of this AccountAdditionalCost.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def subscribed_applications_ids(self):
        """Gets the subscribed_applications_ids of this AccountAdditionalCost.  # noqa: E501

        A list of the IDs of the applications that are subscribed to this additional cost  # noqa: E501

        :return: The subscribed_applications_ids of this AccountAdditionalCost.  # noqa: E501
        :rtype: list[int]
        """
        return self._subscribed_applications_ids

    @subscribed_applications_ids.setter
    def subscribed_applications_ids(self, subscribed_applications_ids):
        """Sets the subscribed_applications_ids of this AccountAdditionalCost.

        A list of the IDs of the applications that are subscribed to this additional cost  # noqa: E501

        :param subscribed_applications_ids: The subscribed_applications_ids of this AccountAdditionalCost.  # noqa: E501
        :type: list[int]
        """

        self._subscribed_applications_ids = subscribed_applications_ids

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
        if not isinstance(other, AccountAdditionalCost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountAdditionalCost):
            return True

        return self.to_dict() != other.to_dict()
