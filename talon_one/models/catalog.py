# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerSession](https://docs.talon.one/integration-api/#operation/updateCustomerSessionV2) endpoint is `https://mycompany.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class Catalog(object):
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
        'modified': 'datetime',
        'name': 'str',
        'description': 'str',
        'subscribed_applications_ids': 'list[int]',
        'version': 'int',
        'created_by': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'account_id': 'accountId',
        'modified': 'modified',
        'name': 'name',
        'description': 'description',
        'subscribed_applications_ids': 'subscribedApplicationsIds',
        'version': 'version',
        'created_by': 'createdBy'
    }

    def __init__(self, id=None, created=None, account_id=None, modified=None, name=None, description=None, subscribed_applications_ids=None, version=None, created_by=None, local_vars_configuration=None):  # noqa: E501
        """Catalog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._account_id = None
        self._modified = None
        self._name = None
        self._description = None
        self._subscribed_applications_ids = None
        self._version = None
        self._created_by = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.account_id = account_id
        self.modified = modified
        self.name = name
        self.description = description
        if subscribed_applications_ids is not None:
            self.subscribed_applications_ids = subscribed_applications_ids
        self.version = version
        self.created_by = created_by

    @property
    def id(self):
        """Gets the id of this Catalog.  # noqa: E501

        Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints.  # noqa: E501

        :return: The id of this Catalog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Catalog.

        Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints.  # noqa: E501

        :param id: The id of this Catalog.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Catalog.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this Catalog.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Catalog.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this Catalog.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def account_id(self):
        """Gets the account_id of this Catalog.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The account_id of this Catalog.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Catalog.

        The ID of the account that owns this entity.  # noqa: E501

        :param account_id: The account_id of this Catalog.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def modified(self):
        """Gets the modified of this Catalog.  # noqa: E501

        The exact moment this entity was last modified.  # noqa: E501

        :return: The modified of this Catalog.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Catalog.

        The exact moment this entity was last modified.  # noqa: E501

        :param modified: The modified of this Catalog.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified is None:  # noqa: E501
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this Catalog.  # noqa: E501

        The cart item catalog name.  # noqa: E501

        :return: The name of this Catalog.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Catalog.

        The cart item catalog name.  # noqa: E501

        :param name: The name of this Catalog.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Catalog.  # noqa: E501

        A description of this cart item catalog.  # noqa: E501

        :return: The description of this Catalog.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Catalog.

        A description of this cart item catalog.  # noqa: E501

        :param description: The description of this Catalog.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def subscribed_applications_ids(self):
        """Gets the subscribed_applications_ids of this Catalog.  # noqa: E501

        A list of the IDs of the applications that are subscribed to this catalog.  # noqa: E501

        :return: The subscribed_applications_ids of this Catalog.  # noqa: E501
        :rtype: list[int]
        """
        return self._subscribed_applications_ids

    @subscribed_applications_ids.setter
    def subscribed_applications_ids(self, subscribed_applications_ids):
        """Sets the subscribed_applications_ids of this Catalog.

        A list of the IDs of the applications that are subscribed to this catalog.  # noqa: E501

        :param subscribed_applications_ids: The subscribed_applications_ids of this Catalog.  # noqa: E501
        :type: list[int]
        """

        self._subscribed_applications_ids = subscribed_applications_ids

    @property
    def version(self):
        """Gets the version of this Catalog.  # noqa: E501

        The current version of this catalog.  # noqa: E501

        :return: The version of this Catalog.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Catalog.

        The current version of this catalog.  # noqa: E501

        :param version: The version of this Catalog.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def created_by(self):
        """Gets the created_by of this Catalog.  # noqa: E501

        The ID of user who created this catalog.  # noqa: E501

        :return: The created_by of this Catalog.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Catalog.

        The ID of user who created this catalog.  # noqa: E501

        :param created_by: The created_by of this Catalog.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

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
        if not isinstance(other, Catalog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Catalog):
            return True

        return self.to_dict() != other.to_dict()
