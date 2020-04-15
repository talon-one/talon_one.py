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


class NewEventType(object):
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
        'application_ids': 'list[int]',
        'title': 'str',
        'name': 'str',
        'description': 'str',
        'mime_type': 'str',
        'example_payload': 'str',
        'schema': 'object',
        'handler_language': 'str',
        'handler': 'str',
        'version': 'int'
    }

    attribute_map = {
        'application_ids': 'applicationIds',
        'title': 'title',
        'name': 'name',
        'description': 'description',
        'mime_type': 'mimeType',
        'example_payload': 'examplePayload',
        'schema': 'schema',
        'handler_language': 'handlerLanguage',
        'handler': 'handler',
        'version': 'version'
    }

    def __init__(self, application_ids=None, title=None, name=None, description=None, mime_type=None, example_payload=None, schema=None, handler_language=None, handler=None, version=None, local_vars_configuration=None):  # noqa: E501
        """NewEventType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_ids = None
        self._title = None
        self._name = None
        self._description = None
        self._mime_type = None
        self._example_payload = None
        self._schema = None
        self._handler_language = None
        self._handler = None
        self._version = None
        self.discriminator = None

        self.application_ids = application_ids
        self.title = title
        self.name = name
        self.description = description
        self.mime_type = mime_type
        if example_payload is not None:
            self.example_payload = example_payload
        if schema is not None:
            self.schema = schema
        if handler_language is not None:
            self.handler_language = handler_language
        self.handler = handler
        self.version = version

    @property
    def application_ids(self):
        """Gets the application_ids of this NewEventType.  # noqa: E501

        The IDs of the applications that are related to this entity.  # noqa: E501

        :return: The application_ids of this NewEventType.  # noqa: E501
        :rtype: list[int]
        """
        return self._application_ids

    @application_ids.setter
    def application_ids(self, application_ids):
        """Sets the application_ids of this NewEventType.

        The IDs of the applications that are related to this entity.  # noqa: E501

        :param application_ids: The application_ids of this NewEventType.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and application_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `application_ids`, must not be `None`")  # noqa: E501

        self._application_ids = application_ids

    @property
    def title(self):
        """Gets the title of this NewEventType.  # noqa: E501

        The human-friendly display name for this event type. Use a short, past-tense, description of the event.  # noqa: E501

        :return: The title of this NewEventType.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NewEventType.

        The human-friendly display name for this event type. Use a short, past-tense, description of the event.  # noqa: E501

        :param title: The title of this NewEventType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) < 1):
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def name(self):
        """Gets the name of this NewEventType.  # noqa: E501

        The machine-friendly canonical name for this event type. This will be used in URLs, and cannot be changed after an event type has been created.  # noqa: E501

        :return: The name of this NewEventType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewEventType.

        The machine-friendly canonical name for this event type. This will be used in URLs, and cannot be changed after an event type has been created.  # noqa: E501

        :param name: The name of this NewEventType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this NewEventType.  # noqa: E501

        An explanation of when the event type is triggered. Write this with a campaign manager in mind. For example:  > The \"Payment Accepted\" event is triggered after successful processing of a payment by our payment gateway.   # noqa: E501

        :return: The description of this NewEventType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NewEventType.

        An explanation of when the event type is triggered. Write this with a campaign manager in mind. For example:  > The \"Payment Accepted\" event is triggered after successful processing of a payment by our payment gateway.   # noqa: E501

        :param description: The description of this NewEventType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def mime_type(self):
        """Gets the mime_type of this NewEventType.  # noqa: E501

        This defines how the request payload will be parsed before your handler code is run.  # noqa: E501

        :return: The mime_type of this NewEventType.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this NewEventType.

        This defines how the request payload will be parsed before your handler code is run.  # noqa: E501

        :param mime_type: The mime_type of this NewEventType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mime_type is None:  # noqa: E501
            raise ValueError("Invalid value for `mime_type`, must not be `None`")  # noqa: E501
        allowed_values = ["application/json", "application/x-www-form-urlencoded", "none"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mime_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mime_type` ({0}), must be one of {1}"  # noqa: E501
                .format(mime_type, allowed_values)
            )

        self._mime_type = mime_type

    @property
    def example_payload(self):
        """Gets the example_payload of this NewEventType.  # noqa: E501

        It is often helpful to include an example payload with the event type definition for documentation purposes.  # noqa: E501

        :return: The example_payload of this NewEventType.  # noqa: E501
        :rtype: str
        """
        return self._example_payload

    @example_payload.setter
    def example_payload(self, example_payload):
        """Sets the example_payload of this NewEventType.

        It is often helpful to include an example payload with the event type definition for documentation purposes.  # noqa: E501

        :param example_payload: The example_payload of this NewEventType.  # noqa: E501
        :type: str
        """

        self._example_payload = example_payload

    @property
    def schema(self):
        """Gets the schema of this NewEventType.  # noqa: E501

        It is strongly recommended to define a JSON schema that will be used to perform structural validation of request payloads after parsing.   # noqa: E501

        :return: The schema of this NewEventType.  # noqa: E501
        :rtype: object
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this NewEventType.

        It is strongly recommended to define a JSON schema that will be used to perform structural validation of request payloads after parsing.   # noqa: E501

        :param schema: The schema of this NewEventType.  # noqa: E501
        :type: object
        """

        self._schema = schema

    @property
    def handler_language(self):
        """Gets the handler_language of this NewEventType.  # noqa: E501

        The language of the handler code. Currently only `\"talang\"` is supported.  # noqa: E501

        :return: The handler_language of this NewEventType.  # noqa: E501
        :rtype: str
        """
        return self._handler_language

    @handler_language.setter
    def handler_language(self, handler_language):
        """Sets the handler_language of this NewEventType.

        The language of the handler code. Currently only `\"talang\"` is supported.  # noqa: E501

        :param handler_language: The handler_language of this NewEventType.  # noqa: E501
        :type: str
        """
        allowed_values = ["talang"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and handler_language not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `handler_language` ({0}), must be one of {1}"  # noqa: E501
                .format(handler_language, allowed_values)
            )

        self._handler_language = handler_language

    @property
    def handler(self):
        """Gets the handler of this NewEventType.  # noqa: E501

        Code that will be run after successful parsing & validation of the payload for this event. This code _may_ choose to evaluate campaign rules.   # noqa: E501

        :return: The handler of this NewEventType.  # noqa: E501
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        """Sets the handler of this NewEventType.

        Code that will be run after successful parsing & validation of the payload for this event. This code _may_ choose to evaluate campaign rules.   # noqa: E501

        :param handler: The handler of this NewEventType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and handler is None:  # noqa: E501
            raise ValueError("Invalid value for `handler`, must not be `None`")  # noqa: E501

        self._handler = handler

    @property
    def version(self):
        """Gets the version of this NewEventType.  # noqa: E501

        The version of this event type. When updating an existing event type this must be **exactly** `currentVersion + 1`.   # noqa: E501

        :return: The version of this NewEventType.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NewEventType.

        The version of this event type. When updating an existing event type this must be **exactly** `currentVersion + 1`.   # noqa: E501

        :param version: The version of this NewEventType.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, NewEventType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewEventType):
            return True

        return self.to_dict() != other.to_dict()
