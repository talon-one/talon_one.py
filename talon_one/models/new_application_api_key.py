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


class NewApplicationAPIKey(object):
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
        'created_by': 'int',
        'title': 'str',
        'account_id': 'int',
        'application_id': 'int',
        'created': 'datetime',
        'expires': 'datetime',
        'key': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'title': 'title',
        'account_id': 'accountID',
        'application_id': 'applicationID',
        'created': 'created',
        'expires': 'expires',
        'key': 'key'
    }

    def __init__(self, id=None, created_by=None, title=None, account_id=None, application_id=None, created=None, expires=None, key=None, local_vars_configuration=None):  # noqa: E501
        """NewApplicationAPIKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_by = None
        self._title = None
        self._account_id = None
        self._application_id = None
        self._created = None
        self._expires = None
        self._key = None
        self.discriminator = None

        self.id = id
        self.created_by = created_by
        self.title = title
        self.account_id = account_id
        self.application_id = application_id
        self.created = created
        self.expires = expires
        self.key = key

    @property
    def id(self):
        """Gets the id of this NewApplicationAPIKey.  # noqa: E501

        ID of the API Key  # noqa: E501

        :return: The id of this NewApplicationAPIKey.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NewApplicationAPIKey.

        ID of the API Key  # noqa: E501

        :param id: The id of this NewApplicationAPIKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this NewApplicationAPIKey.  # noqa: E501

        ID of user who created  # noqa: E501

        :return: The created_by of this NewApplicationAPIKey.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this NewApplicationAPIKey.

        ID of user who created  # noqa: E501

        :param created_by: The created_by of this NewApplicationAPIKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def title(self):
        """Gets the title of this NewApplicationAPIKey.  # noqa: E501

        Title for API Key  # noqa: E501

        :return: The title of this NewApplicationAPIKey.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NewApplicationAPIKey.

        Title for API Key  # noqa: E501

        :param title: The title of this NewApplicationAPIKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def account_id(self):
        """Gets the account_id of this NewApplicationAPIKey.  # noqa: E501

        ID of account the key is used for  # noqa: E501

        :return: The account_id of this NewApplicationAPIKey.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this NewApplicationAPIKey.

        ID of account the key is used for  # noqa: E501

        :param account_id: The account_id of this NewApplicationAPIKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def application_id(self):
        """Gets the application_id of this NewApplicationAPIKey.  # noqa: E501

        ID of application the key is used for  # noqa: E501

        :return: The application_id of this NewApplicationAPIKey.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this NewApplicationAPIKey.

        ID of application the key is used for  # noqa: E501

        :param application_id: The application_id of this NewApplicationAPIKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def created(self):
        """Gets the created of this NewApplicationAPIKey.  # noqa: E501

        The date the API key was created  # noqa: E501

        :return: The created of this NewApplicationAPIKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NewApplicationAPIKey.

        The date the API key was created  # noqa: E501

        :param created: The created of this NewApplicationAPIKey.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def expires(self):
        """Gets the expires of this NewApplicationAPIKey.  # noqa: E501

        The date the API key expired  # noqa: E501

        :return: The expires of this NewApplicationAPIKey.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this NewApplicationAPIKey.

        The date the API key expired  # noqa: E501

        :param expires: The expires of this NewApplicationAPIKey.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and expires is None:  # noqa: E501
            raise ValueError("Invalid value for `expires`, must not be `None`")  # noqa: E501

        self._expires = expires

    @property
    def key(self):
        """Gets the key of this NewApplicationAPIKey.  # noqa: E501

        Raw API Key  # noqa: E501

        :return: The key of this NewApplicationAPIKey.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this NewApplicationAPIKey.

        Raw API Key  # noqa: E501

        :param key: The key of this NewApplicationAPIKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

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
        if not isinstance(other, NewApplicationAPIKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewApplicationAPIKey):
            return True

        return self.to_dict() != other.to_dict()
