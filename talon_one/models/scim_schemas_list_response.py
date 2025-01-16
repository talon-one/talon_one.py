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


class ScimSchemasListResponse(object):
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
        'resources': 'list[ScimSchemaResource]',
        'schemas': 'list[str]',
        'total_results': 'int'
    }

    attribute_map = {
        'resources': 'Resources',
        'schemas': 'schemas',
        'total_results': 'totalResults'
    }

    def __init__(self, resources=None, schemas=None, total_results=None, local_vars_configuration=None):  # noqa: E501
        """ScimSchemasListResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._resources = None
        self._schemas = None
        self._total_results = None
        self.discriminator = None

        self.resources = resources
        if schemas is not None:
            self.schemas = schemas
        if total_results is not None:
            self.total_results = total_results

    @property
    def resources(self):
        """Gets the resources of this ScimSchemasListResponse.  # noqa: E501


        :return: The resources of this ScimSchemasListResponse.  # noqa: E501
        :rtype: list[ScimSchemaResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ScimSchemasListResponse.


        :param resources: The resources of this ScimSchemasListResponse.  # noqa: E501
        :type: list[ScimSchemaResource]
        """
        if self.local_vars_configuration.client_side_validation and resources is None:  # noqa: E501
            raise ValueError("Invalid value for `resources`, must not be `None`")  # noqa: E501

        self._resources = resources

    @property
    def schemas(self):
        """Gets the schemas of this ScimSchemasListResponse.  # noqa: E501

        SCIM schema for the given resource.  # noqa: E501

        :return: The schemas of this ScimSchemasListResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this ScimSchemasListResponse.

        SCIM schema for the given resource.  # noqa: E501

        :param schemas: The schemas of this ScimSchemasListResponse.  # noqa: E501
        :type: list[str]
        """

        self._schemas = schemas

    @property
    def total_results(self):
        """Gets the total_results of this ScimSchemasListResponse.  # noqa: E501

        Number of total results in the response.  # noqa: E501

        :return: The total_results of this ScimSchemasListResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this ScimSchemasListResponse.

        Number of total results in the response.  # noqa: E501

        :param total_results: The total_results of this ScimSchemasListResponse.  # noqa: E501
        :type: int
        """

        self._total_results = total_results

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
        if not isinstance(other, ScimSchemasListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScimSchemasListResponse):
            return True

        return self.to_dict() != other.to_dict()
