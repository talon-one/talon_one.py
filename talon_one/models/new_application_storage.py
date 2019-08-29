# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NewApplicationStorage(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'datatype': 'object',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'datatype': 'datatype',
        'description': 'description'
    }

    def __init__(self, name=None, datatype=None, description=None):  # noqa: E501
        """NewApplicationStorage - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._datatype = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.datatype = datatype
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this NewApplicationStorage.  # noqa: E501

        Identifier for the information to be saved, e.g. \"Loyalty points for SKU\".  # noqa: E501

        :return: The name of this NewApplicationStorage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewApplicationStorage.

        Identifier for the information to be saved, e.g. \"Loyalty points for SKU\".  # noqa: E501

        :param name: The name of this NewApplicationStorage.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def datatype(self):
        """Gets the datatype of this NewApplicationStorage.  # noqa: E501

        A JSON Schema describing the information to be saved in the storage  # noqa: E501

        :return: The datatype of this NewApplicationStorage.  # noqa: E501
        :rtype: object
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this NewApplicationStorage.

        A JSON Schema describing the information to be saved in the storage  # noqa: E501

        :param datatype: The datatype of this NewApplicationStorage.  # noqa: E501
        :type: object
        """
        if datatype is None:
            raise ValueError("Invalid value for `datatype`, must not be `None`")  # noqa: E501

        self._datatype = datatype

    @property
    def description(self):
        """Gets the description of this NewApplicationStorage.  # noqa: E501

        Description of the application store  # noqa: E501

        :return: The description of this NewApplicationStorage.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NewApplicationStorage.

        Description of the application store  # noqa: E501

        :param description: The description of this NewApplicationStorage.  # noqa: E501
        :type: str
        """

        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(NewApplicationStorage, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewApplicationStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
