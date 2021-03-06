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


class NewReferral(object):
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
        'campaign_id': 'int',
        'advocate_profile_integration_id': 'str',
        'friend_profile_integration_id': 'str',
        'start_date': 'datetime',
        'expiry_date': 'datetime'
    }

    attribute_map = {
        'campaign_id': 'campaignId',
        'advocate_profile_integration_id': 'advocateProfileIntegrationId',
        'friend_profile_integration_id': 'friendProfileIntegrationId',
        'start_date': 'startDate',
        'expiry_date': 'expiryDate'
    }

    def __init__(self, campaign_id=None, advocate_profile_integration_id=None, friend_profile_integration_id=None, start_date=None, expiry_date=None, local_vars_configuration=None):  # noqa: E501
        """NewReferral - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._campaign_id = None
        self._advocate_profile_integration_id = None
        self._friend_profile_integration_id = None
        self._start_date = None
        self._expiry_date = None
        self.discriminator = None

        self.campaign_id = campaign_id
        self.advocate_profile_integration_id = advocate_profile_integration_id
        if friend_profile_integration_id is not None:
            self.friend_profile_integration_id = friend_profile_integration_id
        if start_date is not None:
            self.start_date = start_date
        if expiry_date is not None:
            self.expiry_date = expiry_date

    @property
    def campaign_id(self):
        """Gets the campaign_id of this NewReferral.  # noqa: E501

        ID of the campaign from which the referral received the referral code.  # noqa: E501

        :return: The campaign_id of this NewReferral.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this NewReferral.

        ID of the campaign from which the referral received the referral code.  # noqa: E501

        :param campaign_id: The campaign_id of this NewReferral.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and campaign_id is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")  # noqa: E501

        self._campaign_id = campaign_id

    @property
    def advocate_profile_integration_id(self):
        """Gets the advocate_profile_integration_id of this NewReferral.  # noqa: E501

        The Integration Id of the Advocate's Profile  # noqa: E501

        :return: The advocate_profile_integration_id of this NewReferral.  # noqa: E501
        :rtype: str
        """
        return self._advocate_profile_integration_id

    @advocate_profile_integration_id.setter
    def advocate_profile_integration_id(self, advocate_profile_integration_id):
        """Sets the advocate_profile_integration_id of this NewReferral.

        The Integration Id of the Advocate's Profile  # noqa: E501

        :param advocate_profile_integration_id: The advocate_profile_integration_id of this NewReferral.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and advocate_profile_integration_id is None:  # noqa: E501
            raise ValueError("Invalid value for `advocate_profile_integration_id`, must not be `None`")  # noqa: E501

        self._advocate_profile_integration_id = advocate_profile_integration_id

    @property
    def friend_profile_integration_id(self):
        """Gets the friend_profile_integration_id of this NewReferral.  # noqa: E501

        An optional Integration ID of the Friend's Profile  # noqa: E501

        :return: The friend_profile_integration_id of this NewReferral.  # noqa: E501
        :rtype: str
        """
        return self._friend_profile_integration_id

    @friend_profile_integration_id.setter
    def friend_profile_integration_id(self, friend_profile_integration_id):
        """Sets the friend_profile_integration_id of this NewReferral.

        An optional Integration ID of the Friend's Profile  # noqa: E501

        :param friend_profile_integration_id: The friend_profile_integration_id of this NewReferral.  # noqa: E501
        :type: str
        """

        self._friend_profile_integration_id = friend_profile_integration_id

    @property
    def start_date(self):
        """Gets the start_date of this NewReferral.  # noqa: E501

        Timestamp at which point the referral code becomes valid.  # noqa: E501

        :return: The start_date of this NewReferral.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this NewReferral.

        Timestamp at which point the referral code becomes valid.  # noqa: E501

        :param start_date: The start_date of this NewReferral.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this NewReferral.  # noqa: E501

        Expiry date of the referral code. Referral never expires if this is omitted, zero, or negative.  # noqa: E501

        :return: The expiry_date of this NewReferral.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this NewReferral.

        Expiry date of the referral code. Referral never expires if this is omitted, zero, or negative.  # noqa: E501

        :param expiry_date: The expiry_date of this NewReferral.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

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
        if not isinstance(other, NewReferral):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewReferral):
            return True

        return self.to_dict() != other.to_dict()
