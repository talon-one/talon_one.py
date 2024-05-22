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


class OutgoingIntegrationTemplate(object):
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
        'integration_type': 'int',
        'title': 'str',
        'description': 'str',
        'payload': 'str',
        'method': 'str',
        'relative_url': 'str',
        'headers': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'integration_type': 'integrationType',
        'title': 'title',
        'description': 'description',
        'payload': 'payload',
        'method': 'method',
        'relative_url': 'relativeUrl',
        'headers': 'headers'
    }

    def __init__(self, id=None, integration_type=None, title=None, description=None, payload=None, method=None, relative_url=None, headers=None, local_vars_configuration=None):  # noqa: E501
        """OutgoingIntegrationTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._integration_type = None
        self._title = None
        self._description = None
        self._payload = None
        self._method = None
        self._relative_url = None
        self._headers = None
        self.discriminator = None

        self.id = id
        self.integration_type = integration_type
        self.title = title
        self.description = description
        self.payload = payload
        self.method = method
        self.relative_url = relative_url
        self.headers = headers

    @property
    def id(self):
        """Gets the id of this OutgoingIntegrationTemplate.  # noqa: E501

        Unique ID for this entity.  # noqa: E501

        :return: The id of this OutgoingIntegrationTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OutgoingIntegrationTemplate.

        Unique ID for this entity.  # noqa: E501

        :param id: The id of this OutgoingIntegrationTemplate.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def integration_type(self):
        """Gets the integration_type of this OutgoingIntegrationTemplate.  # noqa: E501

        Unique ID of outgoing integration type.  # noqa: E501

        :return: The integration_type of this OutgoingIntegrationTemplate.  # noqa: E501
        :rtype: int
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """Sets the integration_type of this OutgoingIntegrationTemplate.

        Unique ID of outgoing integration type.  # noqa: E501

        :param integration_type: The integration_type of this OutgoingIntegrationTemplate.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and integration_type is None:  # noqa: E501
            raise ValueError("Invalid value for `integration_type`, must not be `None`")  # noqa: E501

        self._integration_type = integration_type

    @property
    def title(self):
        """Gets the title of this OutgoingIntegrationTemplate.  # noqa: E501

        The title of the integration template.  # noqa: E501

        :return: The title of this OutgoingIntegrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this OutgoingIntegrationTemplate.

        The title of the integration template.  # noqa: E501

        :param title: The title of this OutgoingIntegrationTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) > 255):
            raise ValueError("Invalid value for `title`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) < 1):
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this OutgoingIntegrationTemplate.  # noqa: E501

        The description of the specific outgoing integration template.  # noqa: E501

        :return: The description of this OutgoingIntegrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OutgoingIntegrationTemplate.

        The description of the specific outgoing integration template.  # noqa: E501

        :param description: The description of this OutgoingIntegrationTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def payload(self):
        """Gets the payload of this OutgoingIntegrationTemplate.  # noqa: E501

        The API payload (supports templating using parameters) for this integration template.  # noqa: E501

        :return: The payload of this OutgoingIntegrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this OutgoingIntegrationTemplate.

        The API payload (supports templating using parameters) for this integration template.  # noqa: E501

        :param payload: The payload of this OutgoingIntegrationTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payload is None:  # noqa: E501
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        self._payload = payload

    @property
    def method(self):
        """Gets the method of this OutgoingIntegrationTemplate.  # noqa: E501

        API method for this webhook.  # noqa: E501

        :return: The method of this OutgoingIntegrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this OutgoingIntegrationTemplate.

        API method for this webhook.  # noqa: E501

        :param method: The method of this OutgoingIntegrationTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and method is None:  # noqa: E501
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501
        allowed_values = ["POST", "PUT", "GET", "DELETE", "PATCH"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def relative_url(self):
        """Gets the relative_url of this OutgoingIntegrationTemplate.  # noqa: E501

        The relative URL corresponding to each integration template.  # noqa: E501

        :return: The relative_url of this OutgoingIntegrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._relative_url

    @relative_url.setter
    def relative_url(self, relative_url):
        """Sets the relative_url of this OutgoingIntegrationTemplate.

        The relative URL corresponding to each integration template.  # noqa: E501

        :param relative_url: The relative_url of this OutgoingIntegrationTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and relative_url is None:  # noqa: E501
            raise ValueError("Invalid value for `relative_url`, must not be `None`")  # noqa: E501

        self._relative_url = relative_url

    @property
    def headers(self):
        """Gets the headers of this OutgoingIntegrationTemplate.  # noqa: E501

        The list of HTTP headers for this integration template.  # noqa: E501

        :return: The headers of this OutgoingIntegrationTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this OutgoingIntegrationTemplate.

        The list of HTTP headers for this integration template.  # noqa: E501

        :param headers: The headers of this OutgoingIntegrationTemplate.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and headers is None:  # noqa: E501
            raise ValueError("Invalid value for `headers`, must not be `None`")  # noqa: E501

        self._headers = headers

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
        if not isinstance(other, OutgoingIntegrationTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OutgoingIntegrationTemplate):
            return True

        return self.to_dict() != other.to_dict()
