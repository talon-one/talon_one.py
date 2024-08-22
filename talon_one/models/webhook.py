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


class Webhook(object):
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
        'application_ids': 'list[int]',
        'title': 'str',
        'description': 'str',
        'verb': 'str',
        'url': 'str',
        'headers': 'list[str]',
        'payload': 'str',
        'params': 'list[TemplateArgDef]',
        'enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'modified': 'modified',
        'application_ids': 'applicationIds',
        'title': 'title',
        'description': 'description',
        'verb': 'verb',
        'url': 'url',
        'headers': 'headers',
        'payload': 'payload',
        'params': 'params',
        'enabled': 'enabled'
    }

    def __init__(self, id=None, created=None, modified=None, application_ids=None, title=None, description=None, verb=None, url=None, headers=None, payload=None, params=None, enabled=None, local_vars_configuration=None):  # noqa: E501
        """Webhook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._modified = None
        self._application_ids = None
        self._title = None
        self._description = None
        self._verb = None
        self._url = None
        self._headers = None
        self._payload = None
        self._params = None
        self._enabled = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.modified = modified
        self.application_ids = application_ids
        self.title = title
        if description is not None:
            self.description = description
        self.verb = verb
        self.url = url
        self.headers = headers
        if payload is not None:
            self.payload = payload
        self.params = params
        self.enabled = enabled

    @property
    def id(self):
        """Gets the id of this Webhook.  # noqa: E501

        Internal ID of this entity.  # noqa: E501

        :return: The id of this Webhook.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Webhook.

        Internal ID of this entity.  # noqa: E501

        :param id: The id of this Webhook.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Webhook.  # noqa: E501

        The time this entity was created.  # noqa: E501

        :return: The created of this Webhook.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Webhook.

        The time this entity was created.  # noqa: E501

        :param created: The created of this Webhook.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this Webhook.  # noqa: E501

        The time this entity was last modified.  # noqa: E501

        :return: The modified of this Webhook.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Webhook.

        The time this entity was last modified.  # noqa: E501

        :param modified: The modified of this Webhook.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified is None:  # noqa: E501
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def application_ids(self):
        """Gets the application_ids of this Webhook.  # noqa: E501

        The IDs of the Applications that are related to this entity. The IDs of the Applications that are related to this entity.  # noqa: E501

        :return: The application_ids of this Webhook.  # noqa: E501
        :rtype: list[int]
        """
        return self._application_ids

    @application_ids.setter
    def application_ids(self, application_ids):
        """Sets the application_ids of this Webhook.

        The IDs of the Applications that are related to this entity. The IDs of the Applications that are related to this entity.  # noqa: E501

        :param application_ids: The application_ids of this Webhook.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and application_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `application_ids`, must not be `None`")  # noqa: E501

        self._application_ids = application_ids

    @property
    def title(self):
        """Gets the title of this Webhook.  # noqa: E501

        Name or title for this webhook.  # noqa: E501

        :return: The title of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Webhook.

        Name or title for this webhook.  # noqa: E501

        :param title: The title of this Webhook.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and not re.search(r'^[A-Za-z][A-Za-z0-9_.!~*\'() -]*$', title)):  # noqa: E501
            raise ValueError(r"Invalid value for `title`, must be a follow pattern or equal to `/^[A-Za-z][A-Za-z0-9_.!~*'() -]*$/`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this Webhook.  # noqa: E501

        A description of the webhook.  # noqa: E501

        :return: The description of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Webhook.

        A description of the webhook.  # noqa: E501

        :param description: The description of this Webhook.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def verb(self):
        """Gets the verb of this Webhook.  # noqa: E501

        API method for this webhook.  # noqa: E501

        :return: The verb of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """Sets the verb of this Webhook.

        API method for this webhook.  # noqa: E501

        :param verb: The verb of this Webhook.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and verb is None:  # noqa: E501
            raise ValueError("Invalid value for `verb`, must not be `None`")  # noqa: E501
        allowed_values = ["POST", "PUT", "GET", "DELETE", "PATCH"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and verb not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `verb` ({0}), must be one of {1}"  # noqa: E501
                .format(verb, allowed_values)
            )

        self._verb = verb

    @property
    def url(self):
        """Gets the url of this Webhook.  # noqa: E501

        API URL (supports templating using parameters) for this webhook.  # noqa: E501

        :return: The url of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Webhook.

        API URL (supports templating using parameters) for this webhook.  # noqa: E501

        :param url: The url of this Webhook.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def headers(self):
        """Gets the headers of this Webhook.  # noqa: E501

        List of API HTTP headers for this webhook.  # noqa: E501

        :return: The headers of this Webhook.  # noqa: E501
        :rtype: list[str]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this Webhook.

        List of API HTTP headers for this webhook.  # noqa: E501

        :param headers: The headers of this Webhook.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and headers is None:  # noqa: E501
            raise ValueError("Invalid value for `headers`, must not be `None`")  # noqa: E501

        self._headers = headers

    @property
    def payload(self):
        """Gets the payload of this Webhook.  # noqa: E501

        API payload (supports templating using parameters) for this webhook.  # noqa: E501

        :return: The payload of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this Webhook.

        API payload (supports templating using parameters) for this webhook.  # noqa: E501

        :param payload: The payload of this Webhook.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def params(self):
        """Gets the params of this Webhook.  # noqa: E501

        Array of template argument definitions.  # noqa: E501

        :return: The params of this Webhook.  # noqa: E501
        :rtype: list[TemplateArgDef]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this Webhook.

        Array of template argument definitions.  # noqa: E501

        :param params: The params of this Webhook.  # noqa: E501
        :type: list[TemplateArgDef]
        """
        if self.local_vars_configuration.client_side_validation and params is None:  # noqa: E501
            raise ValueError("Invalid value for `params`, must not be `None`")  # noqa: E501

        self._params = params

    @property
    def enabled(self):
        """Gets the enabled of this Webhook.  # noqa: E501

        Enables or disables webhook from showing in the Rule Builder.  # noqa: E501

        :return: The enabled of this Webhook.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Webhook.

        Enables or disables webhook from showing in the Rule Builder.  # noqa: E501

        :param enabled: The enabled of this Webhook.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

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
        if not isinstance(other, Webhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Webhook):
            return True

        return self.to_dict() != other.to_dict()
