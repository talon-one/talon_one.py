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


class IntegrationEntity(object):
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
        'integration_id': 'str',
        'created': 'datetime'
    }

    attribute_map = {
        'integration_id': 'integrationId',
        'created': 'created'
    }

    def __init__(self, integration_id=None, created=None, local_vars_configuration=None):  # noqa: E501
        """IntegrationEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._integration_id = None
        self._created = None
        self.discriminator = None

        self.integration_id = integration_id
        self.created = created

    @property
    def integration_id(self):
        """Gets the integration_id of this IntegrationEntity.  # noqa: E501

        The integration ID for this entity sent to and used in the Talon.One system.  # noqa: E501

        :return: The integration_id of this IntegrationEntity.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this IntegrationEntity.

        The integration ID for this entity sent to and used in the Talon.One system.  # noqa: E501

        :param integration_id: The integration_id of this IntegrationEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and integration_id is None:  # noqa: E501
            raise ValueError("Invalid value for `integration_id`, must not be `None`")  # noqa: E501

        self._integration_id = integration_id

    @property
    def created(self):
        """Gets the created of this IntegrationEntity.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this IntegrationEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this IntegrationEntity.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this IntegrationEntity.  # noqa: E501
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
        if not isinstance(other, IntegrationEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegrationEntity):
            return True

        return self.to_dict() != other.to_dict()
