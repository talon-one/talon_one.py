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


class WebhookActivationLogEntry(object):
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
        'integration_request_uuid': 'str',
        'webhook_id': 'int',
        'application_id': 'int',
        'campaign_id': 'int',
        'created': 'datetime'
    }

    attribute_map = {
        'integration_request_uuid': 'integrationRequestUuid',
        'webhook_id': 'webhookId',
        'application_id': 'applicationId',
        'campaign_id': 'campaignId',
        'created': 'created'
    }

    def __init__(self, integration_request_uuid=None, webhook_id=None, application_id=None, campaign_id=None, created=None, local_vars_configuration=None):  # noqa: E501
        """WebhookActivationLogEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._integration_request_uuid = None
        self._webhook_id = None
        self._application_id = None
        self._campaign_id = None
        self._created = None
        self.discriminator = None

        self.integration_request_uuid = integration_request_uuid
        self.webhook_id = webhook_id
        self.application_id = application_id
        self.campaign_id = campaign_id
        self.created = created

    @property
    def integration_request_uuid(self):
        """Gets the integration_request_uuid of this WebhookActivationLogEntry.  # noqa: E501

        UUID reference of the integration request that triggered the effect with the webhook  # noqa: E501

        :return: The integration_request_uuid of this WebhookActivationLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._integration_request_uuid

    @integration_request_uuid.setter
    def integration_request_uuid(self, integration_request_uuid):
        """Sets the integration_request_uuid of this WebhookActivationLogEntry.

        UUID reference of the integration request that triggered the effect with the webhook  # noqa: E501

        :param integration_request_uuid: The integration_request_uuid of this WebhookActivationLogEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and integration_request_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `integration_request_uuid`, must not be `None`")  # noqa: E501

        self._integration_request_uuid = integration_request_uuid

    @property
    def webhook_id(self):
        """Gets the webhook_id of this WebhookActivationLogEntry.  # noqa: E501

        ID of the webhook that triggered the request  # noqa: E501

        :return: The webhook_id of this WebhookActivationLogEntry.  # noqa: E501
        :rtype: int
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this WebhookActivationLogEntry.

        ID of the webhook that triggered the request  # noqa: E501

        :param webhook_id: The webhook_id of this WebhookActivationLogEntry.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and webhook_id is None:  # noqa: E501
            raise ValueError("Invalid value for `webhook_id`, must not be `None`")  # noqa: E501

        self._webhook_id = webhook_id

    @property
    def application_id(self):
        """Gets the application_id of this WebhookActivationLogEntry.  # noqa: E501

        ID of the application that triggered the webhook  # noqa: E501

        :return: The application_id of this WebhookActivationLogEntry.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this WebhookActivationLogEntry.

        ID of the application that triggered the webhook  # noqa: E501

        :param application_id: The application_id of this WebhookActivationLogEntry.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def campaign_id(self):
        """Gets the campaign_id of this WebhookActivationLogEntry.  # noqa: E501

        ID of the campaign that triggered the webhook  # noqa: E501

        :return: The campaign_id of this WebhookActivationLogEntry.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this WebhookActivationLogEntry.

        ID of the campaign that triggered the webhook  # noqa: E501

        :param campaign_id: The campaign_id of this WebhookActivationLogEntry.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and campaign_id is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")  # noqa: E501

        self._campaign_id = campaign_id

    @property
    def created(self):
        """Gets the created of this WebhookActivationLogEntry.  # noqa: E501

        Timestamp of request  # noqa: E501

        :return: The created of this WebhookActivationLogEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this WebhookActivationLogEntry.

        Timestamp of request  # noqa: E501

        :param created: The created of this WebhookActivationLogEntry.  # noqa: E501
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
        if not isinstance(other, WebhookActivationLogEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookActivationLogEntry):
            return True

        return self.to_dict() != other.to_dict()
