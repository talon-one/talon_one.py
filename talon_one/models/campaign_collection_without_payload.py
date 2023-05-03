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


class CampaignCollectionWithoutPayload(object):
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
        'account_id': 'int',
        'modified': 'datetime',
        'description': 'str',
        'name': 'str',
        'modified_by': 'int',
        'created_by': 'int',
        'application_id': 'int',
        'campaign_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'account_id': 'accountId',
        'modified': 'modified',
        'description': 'description',
        'name': 'name',
        'modified_by': 'modifiedBy',
        'created_by': 'createdBy',
        'application_id': 'applicationId',
        'campaign_id': 'campaignId'
    }

    def __init__(self, id=None, created=None, account_id=None, modified=None, description=None, name=None, modified_by=None, created_by=None, application_id=None, campaign_id=None, local_vars_configuration=None):  # noqa: E501
        """CampaignCollectionWithoutPayload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._account_id = None
        self._modified = None
        self._description = None
        self._name = None
        self._modified_by = None
        self._created_by = None
        self._application_id = None
        self._campaign_id = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.account_id = account_id
        self.modified = modified
        if description is not None:
            self.description = description
        self.name = name
        if modified_by is not None:
            self.modified_by = modified_by
        self.created_by = created_by
        if application_id is not None:
            self.application_id = application_id
        if campaign_id is not None:
            self.campaign_id = campaign_id

    @property
    def id(self):
        """Gets the id of this CampaignCollectionWithoutPayload.  # noqa: E501

        Internal ID of this entity.  # noqa: E501

        :return: The id of this CampaignCollectionWithoutPayload.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CampaignCollectionWithoutPayload.

        Internal ID of this entity.  # noqa: E501

        :param id: The id of this CampaignCollectionWithoutPayload.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this CampaignCollectionWithoutPayload.  # noqa: E501

        The time this entity was created.  # noqa: E501

        :return: The created of this CampaignCollectionWithoutPayload.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CampaignCollectionWithoutPayload.

        The time this entity was created.  # noqa: E501

        :param created: The created of this CampaignCollectionWithoutPayload.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def account_id(self):
        """Gets the account_id of this CampaignCollectionWithoutPayload.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The account_id of this CampaignCollectionWithoutPayload.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CampaignCollectionWithoutPayload.

        The ID of the account that owns this entity.  # noqa: E501

        :param account_id: The account_id of this CampaignCollectionWithoutPayload.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def modified(self):
        """Gets the modified of this CampaignCollectionWithoutPayload.  # noqa: E501

        The time this entity was last modified.  # noqa: E501

        :return: The modified of this CampaignCollectionWithoutPayload.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this CampaignCollectionWithoutPayload.

        The time this entity was last modified.  # noqa: E501

        :param modified: The modified of this CampaignCollectionWithoutPayload.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified is None:  # noqa: E501
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def description(self):
        """Gets the description of this CampaignCollectionWithoutPayload.  # noqa: E501

        A short description of the purpose of this collection.  # noqa: E501

        :return: The description of this CampaignCollectionWithoutPayload.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CampaignCollectionWithoutPayload.

        A short description of the purpose of this collection.  # noqa: E501

        :param description: The description of this CampaignCollectionWithoutPayload.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this CampaignCollectionWithoutPayload.  # noqa: E501

        The name of this collection.  # noqa: E501

        :return: The name of this CampaignCollectionWithoutPayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CampaignCollectionWithoutPayload.

        The name of this collection.  # noqa: E501

        :param name: The name of this CampaignCollectionWithoutPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[^[:cntrl:]\s][^[:cntrl:]]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[^[:cntrl:]\s][^[:cntrl:]]*$/`")  # noqa: E501

        self._name = name

    @property
    def modified_by(self):
        """Gets the modified_by of this CampaignCollectionWithoutPayload.  # noqa: E501

        ID of the user who last updated this effect if available.  # noqa: E501

        :return: The modified_by of this CampaignCollectionWithoutPayload.  # noqa: E501
        :rtype: int
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this CampaignCollectionWithoutPayload.

        ID of the user who last updated this effect if available.  # noqa: E501

        :param modified_by: The modified_by of this CampaignCollectionWithoutPayload.  # noqa: E501
        :type: int
        """

        self._modified_by = modified_by

    @property
    def created_by(self):
        """Gets the created_by of this CampaignCollectionWithoutPayload.  # noqa: E501

        ID of the user who created this effect.  # noqa: E501

        :return: The created_by of this CampaignCollectionWithoutPayload.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CampaignCollectionWithoutPayload.

        ID of the user who created this effect.  # noqa: E501

        :param created_by: The created_by of this CampaignCollectionWithoutPayload.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def application_id(self):
        """Gets the application_id of this CampaignCollectionWithoutPayload.  # noqa: E501

        The ID of the Application that owns this entity.  # noqa: E501

        :return: The application_id of this CampaignCollectionWithoutPayload.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this CampaignCollectionWithoutPayload.

        The ID of the Application that owns this entity.  # noqa: E501

        :param application_id: The application_id of this CampaignCollectionWithoutPayload.  # noqa: E501
        :type: int
        """

        self._application_id = application_id

    @property
    def campaign_id(self):
        """Gets the campaign_id of this CampaignCollectionWithoutPayload.  # noqa: E501

        The ID of the campaign that owns this entity.  # noqa: E501

        :return: The campaign_id of this CampaignCollectionWithoutPayload.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this CampaignCollectionWithoutPayload.

        The ID of the campaign that owns this entity.  # noqa: E501

        :param campaign_id: The campaign_id of this CampaignCollectionWithoutPayload.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

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
        if not isinstance(other, CampaignCollectionWithoutPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignCollectionWithoutPayload):
            return True

        return self.to_dict() != other.to_dict()
