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


class LoyaltyProgramEntity(object):
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
        'program_id': 'int',
        'program_name': 'str',
        'program_title': 'str'
    }

    attribute_map = {
        'program_id': 'programID',
        'program_name': 'programName',
        'program_title': 'programTitle'
    }

    def __init__(self, program_id=None, program_name=None, program_title=None, local_vars_configuration=None):  # noqa: E501
        """LoyaltyProgramEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._program_id = None
        self._program_name = None
        self._program_title = None
        self.discriminator = None

        self.program_id = program_id
        if program_name is not None:
            self.program_name = program_name
        if program_title is not None:
            self.program_title = program_title

    @property
    def program_id(self):
        """Gets the program_id of this LoyaltyProgramEntity.  # noqa: E501

        The ID of the loyalty program that owns this entity.  # noqa: E501

        :return: The program_id of this LoyaltyProgramEntity.  # noqa: E501
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this LoyaltyProgramEntity.

        The ID of the loyalty program that owns this entity.  # noqa: E501

        :param program_id: The program_id of this LoyaltyProgramEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and program_id is None:  # noqa: E501
            raise ValueError("Invalid value for `program_id`, must not be `None`")  # noqa: E501

        self._program_id = program_id

    @property
    def program_name(self):
        """Gets the program_name of this LoyaltyProgramEntity.  # noqa: E501

        The integration name of the loyalty program that owns this entity.  # noqa: E501

        :return: The program_name of this LoyaltyProgramEntity.  # noqa: E501
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name):
        """Sets the program_name of this LoyaltyProgramEntity.

        The integration name of the loyalty program that owns this entity.  # noqa: E501

        :param program_name: The program_name of this LoyaltyProgramEntity.  # noqa: E501
        :type: str
        """

        self._program_name = program_name

    @property
    def program_title(self):
        """Gets the program_title of this LoyaltyProgramEntity.  # noqa: E501

        The Campaign Manager-displayed name of the loyalty program that owns this entity.  # noqa: E501

        :return: The program_title of this LoyaltyProgramEntity.  # noqa: E501
        :rtype: str
        """
        return self._program_title

    @program_title.setter
    def program_title(self, program_title):
        """Sets the program_title of this LoyaltyProgramEntity.

        The Campaign Manager-displayed name of the loyalty program that owns this entity.  # noqa: E501

        :param program_title: The program_title of this LoyaltyProgramEntity.  # noqa: E501
        :type: str
        """

        self._program_title = program_title

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
        if not isinstance(other, LoyaltyProgramEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoyaltyProgramEntity):
            return True

        return self.to_dict() != other.to_dict()
