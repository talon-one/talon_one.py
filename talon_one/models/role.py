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


class Role(object):
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
        'modified': 'datetime',
        'account_id': 'int',
        'campaign_group_id': 'int',
        'name': 'str',
        'description': 'str',
        'members': 'list[int]',
        'acl': 'object'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'modified': 'modified',
        'account_id': 'accountId',
        'campaign_group_id': 'campaignGroupID',
        'name': 'name',
        'description': 'description',
        'members': 'members',
        'acl': 'acl'
    }

    def __init__(self, id=None, created=None, modified=None, account_id=None, campaign_group_id=None, name=None, description=None, members=None, acl=None, local_vars_configuration=None):  # noqa: E501
        """Role - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._modified = None
        self._account_id = None
        self._campaign_group_id = None
        self._name = None
        self._description = None
        self._members = None
        self._acl = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.modified = modified
        self.account_id = account_id
        if campaign_group_id is not None:
            self.campaign_group_id = campaign_group_id
        self.name = name
        if description is not None:
            self.description = description
        if members is not None:
            self.members = members
        self.acl = acl

    @property
    def id(self):
        """Gets the id of this Role.  # noqa: E501

        Internal ID of this entity.  # noqa: E501

        :return: The id of this Role.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Role.

        Internal ID of this entity.  # noqa: E501

        :param id: The id of this Role.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Role.  # noqa: E501

        The time this entity was created.  # noqa: E501

        :return: The created of this Role.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Role.

        The time this entity was created.  # noqa: E501

        :param created: The created of this Role.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this Role.  # noqa: E501

        The time this entity was last modified.  # noqa: E501

        :return: The modified of this Role.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Role.

        The time this entity was last modified.  # noqa: E501

        :param modified: The modified of this Role.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified is None:  # noqa: E501
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def account_id(self):
        """Gets the account_id of this Role.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The account_id of this Role.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Role.

        The ID of the account that owns this entity.  # noqa: E501

        :param account_id: The account_id of this Role.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def campaign_group_id(self):
        """Gets the campaign_group_id of this Role.  # noqa: E501

        The ID of the [Campaign Group](https://docs.talon.one/docs/product/account/account-settings/managing-campaign-groups) this role was created for.   # noqa: E501

        :return: The campaign_group_id of this Role.  # noqa: E501
        :rtype: int
        """
        return self._campaign_group_id

    @campaign_group_id.setter
    def campaign_group_id(self, campaign_group_id):
        """Sets the campaign_group_id of this Role.

        The ID of the [Campaign Group](https://docs.talon.one/docs/product/account/account-settings/managing-campaign-groups) this role was created for.   # noqa: E501

        :param campaign_group_id: The campaign_group_id of this Role.  # noqa: E501
        :type: int
        """

        self._campaign_group_id = campaign_group_id

    @property
    def name(self):
        """Gets the name of this Role.  # noqa: E501

        Name of the role.  # noqa: E501

        :return: The name of this Role.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Role.

        Name of the role.  # noqa: E501

        :param name: The name of this Role.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Role.  # noqa: E501

        Description of the role.  # noqa: E501

        :return: The description of this Role.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Role.

        Description of the role.  # noqa: E501

        :param description: The description of this Role.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def members(self):
        """Gets the members of this Role.  # noqa: E501

        A list of user identifiers assigned to this role.  # noqa: E501

        :return: The members of this Role.  # noqa: E501
        :rtype: list[int]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this Role.

        A list of user identifiers assigned to this role.  # noqa: E501

        :param members: The members of this Role.  # noqa: E501
        :type: list[int]
        """

        self._members = members

    @property
    def acl(self):
        """Gets the acl of this Role.  # noqa: E501

        The `Access Control List` json defining the role of the user. This represents the access control on the user level.  # noqa: E501

        :return: The acl of this Role.  # noqa: E501
        :rtype: object
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this Role.

        The `Access Control List` json defining the role of the user. This represents the access control on the user level.  # noqa: E501

        :param acl: The acl of this Role.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and acl is None:  # noqa: E501
            raise ValueError("Invalid value for `acl`, must not be `None`")  # noqa: E501

        self._acl = acl

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
        if not isinstance(other, Role):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Role):
            return True

        return self.to_dict() != other.to_dict()
