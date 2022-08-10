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


class NewSamlConnection(object):
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
        'x509certificate': 'str',
        'account_id': 'int',
        'name': 'str',
        'enabled': 'bool',
        'issuer': 'str',
        'sign_on_url': 'str',
        'sign_out_url': 'str',
        'metadata_url': 'str',
        'audience_uri': 'str'
    }

    attribute_map = {
        'x509certificate': 'x509certificate',
        'account_id': 'accountId',
        'name': 'name',
        'enabled': 'enabled',
        'issuer': 'issuer',
        'sign_on_url': 'signOnURL',
        'sign_out_url': 'signOutURL',
        'metadata_url': 'metadataURL',
        'audience_uri': 'audienceURI'
    }

    def __init__(self, x509certificate=None, account_id=None, name=None, enabled=None, issuer=None, sign_on_url=None, sign_out_url=None, metadata_url=None, audience_uri=None, local_vars_configuration=None):  # noqa: E501
        """NewSamlConnection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._x509certificate = None
        self._account_id = None
        self._name = None
        self._enabled = None
        self._issuer = None
        self._sign_on_url = None
        self._sign_out_url = None
        self._metadata_url = None
        self._audience_uri = None
        self.discriminator = None

        self.x509certificate = x509certificate
        self.account_id = account_id
        self.name = name
        self.enabled = enabled
        self.issuer = issuer
        self.sign_on_url = sign_on_url
        if sign_out_url is not None:
            self.sign_out_url = sign_out_url
        if metadata_url is not None:
            self.metadata_url = metadata_url
        if audience_uri is not None:
            self.audience_uri = audience_uri

    @property
    def x509certificate(self):
        """Gets the x509certificate of this NewSamlConnection.  # noqa: E501

        X.509 Certificate.  # noqa: E501

        :return: The x509certificate of this NewSamlConnection.  # noqa: E501
        :rtype: str
        """
        return self._x509certificate

    @x509certificate.setter
    def x509certificate(self, x509certificate):
        """Sets the x509certificate of this NewSamlConnection.

        X.509 Certificate.  # noqa: E501

        :param x509certificate: The x509certificate of this NewSamlConnection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and x509certificate is None:  # noqa: E501
            raise ValueError("Invalid value for `x509certificate`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                x509certificate is not None and len(x509certificate) < 1):
            raise ValueError("Invalid value for `x509certificate`, length must be greater than or equal to `1`")  # noqa: E501

        self._x509certificate = x509certificate

    @property
    def account_id(self):
        """Gets the account_id of this NewSamlConnection.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The account_id of this NewSamlConnection.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this NewSamlConnection.

        The ID of the account that owns this entity.  # noqa: E501

        :param account_id: The account_id of this NewSamlConnection.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this NewSamlConnection.  # noqa: E501

        ID of the SAML service.  # noqa: E501

        :return: The name of this NewSamlConnection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewSamlConnection.

        ID of the SAML service.  # noqa: E501

        :param name: The name of this NewSamlConnection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this NewSamlConnection.  # noqa: E501

        Determines if this SAML connection active.  # noqa: E501

        :return: The enabled of this NewSamlConnection.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NewSamlConnection.

        Determines if this SAML connection active.  # noqa: E501

        :param enabled: The enabled of this NewSamlConnection.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def issuer(self):
        """Gets the issuer of this NewSamlConnection.  # noqa: E501

        Identity Provider Entity ID.  # noqa: E501

        :return: The issuer of this NewSamlConnection.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this NewSamlConnection.

        Identity Provider Entity ID.  # noqa: E501

        :param issuer: The issuer of this NewSamlConnection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and issuer is None:  # noqa: E501
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                issuer is not None and len(issuer) < 1):
            raise ValueError("Invalid value for `issuer`, length must be greater than or equal to `1`")  # noqa: E501

        self._issuer = issuer

    @property
    def sign_on_url(self):
        """Gets the sign_on_url of this NewSamlConnection.  # noqa: E501

        Single Sign-On URL.  # noqa: E501

        :return: The sign_on_url of this NewSamlConnection.  # noqa: E501
        :rtype: str
        """
        return self._sign_on_url

    @sign_on_url.setter
    def sign_on_url(self, sign_on_url):
        """Sets the sign_on_url of this NewSamlConnection.

        Single Sign-On URL.  # noqa: E501

        :param sign_on_url: The sign_on_url of this NewSamlConnection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sign_on_url is None:  # noqa: E501
            raise ValueError("Invalid value for `sign_on_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sign_on_url is not None and len(sign_on_url) < 1):
            raise ValueError("Invalid value for `sign_on_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._sign_on_url = sign_on_url

    @property
    def sign_out_url(self):
        """Gets the sign_out_url of this NewSamlConnection.  # noqa: E501

        Single Sign-Out URL.  # noqa: E501

        :return: The sign_out_url of this NewSamlConnection.  # noqa: E501
        :rtype: str
        """
        return self._sign_out_url

    @sign_out_url.setter
    def sign_out_url(self, sign_out_url):
        """Sets the sign_out_url of this NewSamlConnection.

        Single Sign-Out URL.  # noqa: E501

        :param sign_out_url: The sign_out_url of this NewSamlConnection.  # noqa: E501
        :type: str
        """

        self._sign_out_url = sign_out_url

    @property
    def metadata_url(self):
        """Gets the metadata_url of this NewSamlConnection.  # noqa: E501

        Metadata URL.  # noqa: E501

        :return: The metadata_url of this NewSamlConnection.  # noqa: E501
        :rtype: str
        """
        return self._metadata_url

    @metadata_url.setter
    def metadata_url(self, metadata_url):
        """Sets the metadata_url of this NewSamlConnection.

        Metadata URL.  # noqa: E501

        :param metadata_url: The metadata_url of this NewSamlConnection.  # noqa: E501
        :type: str
        """

        self._metadata_url = metadata_url

    @property
    def audience_uri(self):
        """Gets the audience_uri of this NewSamlConnection.  # noqa: E501

        The application-defined unique identifier that is the intended audience of the SAML assertion. This is most often the SP Entity ID of your application. When not specified, the ACS URL will be used.   # noqa: E501

        :return: The audience_uri of this NewSamlConnection.  # noqa: E501
        :rtype: str
        """
        return self._audience_uri

    @audience_uri.setter
    def audience_uri(self, audience_uri):
        """Sets the audience_uri of this NewSamlConnection.

        The application-defined unique identifier that is the intended audience of the SAML assertion. This is most often the SP Entity ID of your application. When not specified, the ACS URL will be used.   # noqa: E501

        :param audience_uri: The audience_uri of this NewSamlConnection.  # noqa: E501
        :type: str
        """

        self._audience_uri = audience_uri

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
        if not isinstance(other, NewSamlConnection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewSamlConnection):
            return True

        return self.to_dict() != other.to_dict()
