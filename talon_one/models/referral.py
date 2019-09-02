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


class Referral(object):
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
        'id': 'int',
        'created': 'datetime',
        'campaign_id': 'int',
        'advocate_profile_integration_id': 'str',
        'friend_profile_integration_id': 'str',
        'start_date': 'datetime',
        'expiry_date': 'datetime',
        'code': 'str',
        'usage_counter': 'int',
        'usage_limit': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'campaign_id': 'campaignId',
        'advocate_profile_integration_id': 'advocateProfileIntegrationId',
        'friend_profile_integration_id': 'friendProfileIntegrationId',
        'start_date': 'startDate',
        'expiry_date': 'expiryDate',
        'code': 'code',
        'usage_counter': 'usageCounter',
        'usage_limit': 'usageLimit'
    }

    def __init__(self, id=None, created=None, campaign_id=None, advocate_profile_integration_id=None, friend_profile_integration_id=None, start_date=None, expiry_date=None, code=None, usage_counter=None, usage_limit=None):  # noqa: E501
        """Referral - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created = None
        self._campaign_id = None
        self._advocate_profile_integration_id = None
        self._friend_profile_integration_id = None
        self._start_date = None
        self._expiry_date = None
        self._code = None
        self._usage_counter = None
        self._usage_limit = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.campaign_id = campaign_id
        self.advocate_profile_integration_id = advocate_profile_integration_id
        if friend_profile_integration_id is not None:
            self.friend_profile_integration_id = friend_profile_integration_id
        if start_date is not None:
            self.start_date = start_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        self.code = code
        self.usage_counter = usage_counter
        self.usage_limit = usage_limit

    @property
    def id(self):
        """Gets the id of this Referral.  # noqa: E501

        Unique ID for this entity.  # noqa: E501

        :return: The id of this Referral.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Referral.

        Unique ID for this entity.  # noqa: E501

        :param id: The id of this Referral.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Referral.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this Referral.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Referral.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this Referral.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def campaign_id(self):
        """Gets the campaign_id of this Referral.  # noqa: E501

        ID of the campaign from which the referral received the referral code.  # noqa: E501

        :return: The campaign_id of this Referral.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this Referral.

        ID of the campaign from which the referral received the referral code.  # noqa: E501

        :param campaign_id: The campaign_id of this Referral.  # noqa: E501
        :type: int
        """
        if campaign_id is None:
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")  # noqa: E501

        self._campaign_id = campaign_id

    @property
    def advocate_profile_integration_id(self):
        """Gets the advocate_profile_integration_id of this Referral.  # noqa: E501

        The Integration Id of the Advocate's Profile  # noqa: E501

        :return: The advocate_profile_integration_id of this Referral.  # noqa: E501
        :rtype: str
        """
        return self._advocate_profile_integration_id

    @advocate_profile_integration_id.setter
    def advocate_profile_integration_id(self, advocate_profile_integration_id):
        """Sets the advocate_profile_integration_id of this Referral.

        The Integration Id of the Advocate's Profile  # noqa: E501

        :param advocate_profile_integration_id: The advocate_profile_integration_id of this Referral.  # noqa: E501
        :type: str
        """
        if advocate_profile_integration_id is None:
            raise ValueError("Invalid value for `advocate_profile_integration_id`, must not be `None`")  # noqa: E501

        self._advocate_profile_integration_id = advocate_profile_integration_id

    @property
    def friend_profile_integration_id(self):
        """Gets the friend_profile_integration_id of this Referral.  # noqa: E501

        An optional Integration ID of the Friend's Profile  # noqa: E501

        :return: The friend_profile_integration_id of this Referral.  # noqa: E501
        :rtype: str
        """
        return self._friend_profile_integration_id

    @friend_profile_integration_id.setter
    def friend_profile_integration_id(self, friend_profile_integration_id):
        """Sets the friend_profile_integration_id of this Referral.

        An optional Integration ID of the Friend's Profile  # noqa: E501

        :param friend_profile_integration_id: The friend_profile_integration_id of this Referral.  # noqa: E501
        :type: str
        """

        self._friend_profile_integration_id = friend_profile_integration_id

    @property
    def start_date(self):
        """Gets the start_date of this Referral.  # noqa: E501

        Timestamp at which point the referral code becomes valid.  # noqa: E501

        :return: The start_date of this Referral.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Referral.

        Timestamp at which point the referral code becomes valid.  # noqa: E501

        :param start_date: The start_date of this Referral.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this Referral.  # noqa: E501

        Expiry date of the referral code. Referral never expires if this is omitted, zero, or negative.  # noqa: E501

        :return: The expiry_date of this Referral.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this Referral.

        Expiry date of the referral code. Referral never expires if this is omitted, zero, or negative.  # noqa: E501

        :param expiry_date: The expiry_date of this Referral.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

    @property
    def code(self):
        """Gets the code of this Referral.  # noqa: E501

        The actual referral code.  # noqa: E501

        :return: The code of this Referral.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Referral.

        The actual referral code.  # noqa: E501

        :param code: The code of this Referral.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if code is not None and len(code) < 4:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `4`")  # noqa: E501

        self._code = code

    @property
    def usage_counter(self):
        """Gets the usage_counter of this Referral.  # noqa: E501

        The number of times this referral code has been successfully used.  # noqa: E501

        :return: The usage_counter of this Referral.  # noqa: E501
        :rtype: int
        """
        return self._usage_counter

    @usage_counter.setter
    def usage_counter(self, usage_counter):
        """Sets the usage_counter of this Referral.

        The number of times this referral code has been successfully used.  # noqa: E501

        :param usage_counter: The usage_counter of this Referral.  # noqa: E501
        :type: int
        """
        if usage_counter is None:
            raise ValueError("Invalid value for `usage_counter`, must not be `None`")  # noqa: E501

        self._usage_counter = usage_counter

    @property
    def usage_limit(self):
        """Gets the usage_limit of this Referral.  # noqa: E501

        The number of times a referral code can be used. This can be set to 0 for no limit, but any campaign usage limits will still apply.   # noqa: E501

        :return: The usage_limit of this Referral.  # noqa: E501
        :rtype: int
        """
        return self._usage_limit

    @usage_limit.setter
    def usage_limit(self, usage_limit):
        """Sets the usage_limit of this Referral.

        The number of times a referral code can be used. This can be set to 0 for no limit, but any campaign usage limits will still apply.   # noqa: E501

        :param usage_limit: The usage_limit of this Referral.  # noqa: E501
        :type: int
        """
        if usage_limit is None:
            raise ValueError("Invalid value for `usage_limit`, must not be `None`")  # noqa: E501
        if usage_limit is not None and usage_limit < 0:  # noqa: E501
            raise ValueError("Invalid value for `usage_limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._usage_limit = usage_limit

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
        if issubclass(Referral, dict):
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
        if not isinstance(other, Referral):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other