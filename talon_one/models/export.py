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


class Export(object):
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
        'user_id': 'int',
        'entity': 'str',
        'filter': 'object'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'account_id': 'accountId',
        'user_id': 'userId',
        'entity': 'entity',
        'filter': 'filter'
    }

    def __init__(self, id=None, created=None, account_id=None, user_id=None, entity=None, filter=None, local_vars_configuration=None):  # noqa: E501
        """Export - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._account_id = None
        self._user_id = None
        self._entity = None
        self._filter = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.account_id = account_id
        self.user_id = user_id
        self.entity = entity
        self.filter = filter

    @property
    def id(self):
        """Gets the id of this Export.  # noqa: E501

        Unique ID for this entity.  # noqa: E501

        :return: The id of this Export.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Export.

        Unique ID for this entity.  # noqa: E501

        :param id: The id of this Export.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Export.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this Export.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Export.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this Export.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def account_id(self):
        """Gets the account_id of this Export.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The account_id of this Export.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Export.

        The ID of the account that owns this entity.  # noqa: E501

        :param account_id: The account_id of this Export.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def user_id(self):
        """Gets the user_id of this Export.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The user_id of this Export.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Export.

        The ID of the account that owns this entity.  # noqa: E501

        :param user_id: The user_id of this Export.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def entity(self):
        """Gets the entity of this Export.  # noqa: E501

        The name of the entity that was exported.  # noqa: E501

        :return: The entity of this Export.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this Export.

        The name of the entity that was exported.  # noqa: E501

        :param entity: The entity of this Export.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and entity is None:  # noqa: E501
            raise ValueError("Invalid value for `entity`, must not be `None`")  # noqa: E501
        allowed_values = ["Coupon", "Effect", "CustomerSession", "LoyaltyLedger", "LoyaltyLedgerLog"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and entity not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `entity` ({0}), must be one of {1}"  # noqa: E501
                .format(entity, allowed_values)
            )

        self._entity = entity

    @property
    def filter(self):
        """Gets the filter of this Export.  # noqa: E501

        Map of keys and values that were used to filter the exported rows  # noqa: E501

        :return: The filter of this Export.  # noqa: E501
        :rtype: object
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this Export.

        Map of keys and values that were used to filter the exported rows  # noqa: E501

        :param filter: The filter of this Export.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and filter is None:  # noqa: E501
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501

        self._filter = filter

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
        if not isinstance(other, Export):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Export):
            return True

        return self.to_dict() != other.to_dict()
