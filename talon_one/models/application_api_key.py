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


class ApplicationAPIKey(object):
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
        'title': 'str',
        'expires': 'datetime',
        'platform': 'str',
        'id': 'int',
        'created_by': 'int',
        'account_id': 'int',
        'application_id': 'int',
        'created': 'datetime'
    }

    attribute_map = {
        'title': 'title',
        'expires': 'expires',
        'platform': 'platform',
        'id': 'id',
        'created_by': 'createdBy',
        'account_id': 'accountID',
        'application_id': 'applicationID',
        'created': 'created'
    }

    def __init__(self, title=None, expires=None, platform=None, id=None, created_by=None, account_id=None, application_id=None, created=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationAPIKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._expires = None
        self._platform = None
        self._id = None
        self._created_by = None
        self._account_id = None
        self._application_id = None
        self._created = None
        self.discriminator = None

        self.title = title
        self.expires = expires
        if platform is not None:
            self.platform = platform
        self.id = id
        self.created_by = created_by
        self.account_id = account_id
        self.application_id = application_id
        self.created = created

    @property
    def title(self):
        """Gets the title of this ApplicationAPIKey.  # noqa: E501

        Title for API Key.  # noqa: E501

        :return: The title of this ApplicationAPIKey.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ApplicationAPIKey.

        Title for API Key.  # noqa: E501

        :param title: The title of this ApplicationAPIKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def expires(self):
        """Gets the expires of this ApplicationAPIKey.  # noqa: E501

        The date the API key expired.  # noqa: E501

        :return: The expires of this ApplicationAPIKey.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this ApplicationAPIKey.

        The date the API key expired.  # noqa: E501

        :param expires: The expires of this ApplicationAPIKey.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and expires is None:  # noqa: E501
            raise ValueError("Invalid value for `expires`, must not be `None`")  # noqa: E501

        self._expires = expires

    @property
    def platform(self):
        """Gets the platform of this ApplicationAPIKey.  # noqa: E501

        The third-party platform the API key is valid for. Use `none` for a generic API key to be used from your own integration layer.   # noqa: E501

        :return: The platform of this ApplicationAPIKey.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ApplicationAPIKey.

        The third-party platform the API key is valid for. Use `none` for a generic API key to be used from your own integration layer.   # noqa: E501

        :param platform: The platform of this ApplicationAPIKey.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "segment", "braze", "mparticle", "selligent", "iterable", "customer_engagement", "customer_data", "salesforce"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and platform not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `platform` ({0}), must be one of {1}"  # noqa: E501
                .format(platform, allowed_values)
            )

        self._platform = platform

    @property
    def id(self):
        """Gets the id of this ApplicationAPIKey.  # noqa: E501

        ID of the API Key.  # noqa: E501

        :return: The id of this ApplicationAPIKey.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationAPIKey.

        ID of the API Key.  # noqa: E501

        :param id: The id of this ApplicationAPIKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this ApplicationAPIKey.  # noqa: E501

        ID of user who created.  # noqa: E501

        :return: The created_by of this ApplicationAPIKey.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ApplicationAPIKey.

        ID of user who created.  # noqa: E501

        :param created_by: The created_by of this ApplicationAPIKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def account_id(self):
        """Gets the account_id of this ApplicationAPIKey.  # noqa: E501

        ID of account the key is used for.  # noqa: E501

        :return: The account_id of this ApplicationAPIKey.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ApplicationAPIKey.

        ID of account the key is used for.  # noqa: E501

        :param account_id: The account_id of this ApplicationAPIKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def application_id(self):
        """Gets the application_id of this ApplicationAPIKey.  # noqa: E501

        ID of application the key is used for.  # noqa: E501

        :return: The application_id of this ApplicationAPIKey.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApplicationAPIKey.

        ID of application the key is used for.  # noqa: E501

        :param application_id: The application_id of this ApplicationAPIKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def created(self):
        """Gets the created of this ApplicationAPIKey.  # noqa: E501

        The date the API key was created.  # noqa: E501

        :return: The created of this ApplicationAPIKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ApplicationAPIKey.

        The date the API key was created.  # noqa: E501

        :param created: The created of this ApplicationAPIKey.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

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
        if not isinstance(other, ApplicationAPIKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationAPIKey):
            return True

        return self.to_dict() != other.to_dict()
