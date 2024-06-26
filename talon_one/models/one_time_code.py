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


class OneTimeCode(object):
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
        'user_id': 'int',
        'account_id': 'int',
        'token': 'str',
        'code': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'account_id': 'accountId',
        'token': 'token',
        'code': 'code'
    }

    def __init__(self, user_id=None, account_id=None, token=None, code=None, local_vars_configuration=None):  # noqa: E501
        """OneTimeCode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._account_id = None
        self._token = None
        self._code = None
        self.discriminator = None

        self.user_id = user_id
        self.account_id = account_id
        self.token = token
        if code is not None:
            self.code = code

    @property
    def user_id(self):
        """Gets the user_id of this OneTimeCode.  # noqa: E501

        The ID of the user.  # noqa: E501

        :return: The user_id of this OneTimeCode.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this OneTimeCode.

        The ID of the user.  # noqa: E501

        :param user_id: The user_id of this OneTimeCode.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def account_id(self):
        """Gets the account_id of this OneTimeCode.  # noqa: E501

        The ID of the account.  # noqa: E501

        :return: The account_id of this OneTimeCode.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this OneTimeCode.

        The ID of the account.  # noqa: E501

        :param account_id: The account_id of this OneTimeCode.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def token(self):
        """Gets the token of this OneTimeCode.  # noqa: E501

        The two-factor authentication token created during sign-in. This token is used to ensure that the correct user is trying to sign in with a given one-time security code.  # noqa: E501

        :return: The token of this OneTimeCode.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this OneTimeCode.

        The two-factor authentication token created during sign-in. This token is used to ensure that the correct user is trying to sign in with a given one-time security code.  # noqa: E501

        :param token: The token of this OneTimeCode.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token is None:  # noqa: E501
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def code(self):
        """Gets the code of this OneTimeCode.  # noqa: E501

        The one-time security code used for signing in.  # noqa: E501

        :return: The code of this OneTimeCode.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this OneTimeCode.

        The one-time security code used for signing in.  # noqa: E501

        :param code: The code of this OneTimeCode.  # noqa: E501
        :type: str
        """

        self._code = code

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
        if not isinstance(other, OneTimeCode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneTimeCode):
            return True

        return self.to_dict() != other.to_dict()
