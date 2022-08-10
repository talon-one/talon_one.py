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


class ModelReturn(object):
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
        'application_id': 'int',
        'account_id': 'int',
        'returned_cart_items': 'list[ReturnedCartItem]',
        'event_id': 'int',
        'session_id': 'int',
        'session_integration_id': 'str',
        'profile_id': 'int',
        'profile_integration_id': 'str',
        'created_by': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'application_id': 'applicationId',
        'account_id': 'accountId',
        'returned_cart_items': 'returnedCartItems',
        'event_id': 'eventId',
        'session_id': 'sessionId',
        'session_integration_id': 'sessionIntegrationId',
        'profile_id': 'profileId',
        'profile_integration_id': 'profileIntegrationId',
        'created_by': 'createdBy'
    }

    def __init__(self, id=None, created=None, application_id=None, account_id=None, returned_cart_items=None, event_id=None, session_id=None, session_integration_id=None, profile_id=None, profile_integration_id=None, created_by=None, local_vars_configuration=None):  # noqa: E501
        """ModelReturn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._application_id = None
        self._account_id = None
        self._returned_cart_items = None
        self._event_id = None
        self._session_id = None
        self._session_integration_id = None
        self._profile_id = None
        self._profile_integration_id = None
        self._created_by = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.application_id = application_id
        self.account_id = account_id
        self.returned_cart_items = returned_cart_items
        self.event_id = event_id
        self.session_id = session_id
        self.session_integration_id = session_integration_id
        if profile_id is not None:
            self.profile_id = profile_id
        if profile_integration_id is not None:
            self.profile_integration_id = profile_integration_id
        if created_by is not None:
            self.created_by = created_by

    @property
    def id(self):
        """Gets the id of this ModelReturn.  # noqa: E501

        Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints.  # noqa: E501

        :return: The id of this ModelReturn.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelReturn.

        Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints.  # noqa: E501

        :param id: The id of this ModelReturn.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this ModelReturn.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this ModelReturn.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ModelReturn.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this ModelReturn.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def application_id(self):
        """Gets the application_id of this ModelReturn.  # noqa: E501

        The ID of the application that owns this entity.  # noqa: E501

        :return: The application_id of this ModelReturn.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ModelReturn.

        The ID of the application that owns this entity.  # noqa: E501

        :param application_id: The application_id of this ModelReturn.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def account_id(self):
        """Gets the account_id of this ModelReturn.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The account_id of this ModelReturn.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ModelReturn.

        The ID of the account that owns this entity.  # noqa: E501

        :param account_id: The account_id of this ModelReturn.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def returned_cart_items(self):
        """Gets the returned_cart_items of this ModelReturn.  # noqa: E501

        List of cart items to be returned.  # noqa: E501

        :return: The returned_cart_items of this ModelReturn.  # noqa: E501
        :rtype: list[ReturnedCartItem]
        """
        return self._returned_cart_items

    @returned_cart_items.setter
    def returned_cart_items(self, returned_cart_items):
        """Sets the returned_cart_items of this ModelReturn.

        List of cart items to be returned.  # noqa: E501

        :param returned_cart_items: The returned_cart_items of this ModelReturn.  # noqa: E501
        :type: list[ReturnedCartItem]
        """
        if self.local_vars_configuration.client_side_validation and returned_cart_items is None:  # noqa: E501
            raise ValueError("Invalid value for `returned_cart_items`, must not be `None`")  # noqa: E501

        self._returned_cart_items = returned_cart_items

    @property
    def event_id(self):
        """Gets the event_id of this ModelReturn.  # noqa: E501

        The event ID of that was generated for this return.  # noqa: E501

        :return: The event_id of this ModelReturn.  # noqa: E501
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this ModelReturn.

        The event ID of that was generated for this return.  # noqa: E501

        :param event_id: The event_id of this ModelReturn.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and event_id is None:  # noqa: E501
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501

        self._event_id = event_id

    @property
    def session_id(self):
        """Gets the session_id of this ModelReturn.  # noqa: E501

        The internal ID of the session this return was requested on.  # noqa: E501

        :return: The session_id of this ModelReturn.  # noqa: E501
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this ModelReturn.

        The internal ID of the session this return was requested on.  # noqa: E501

        :param session_id: The session_id of this ModelReturn.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and session_id is None:  # noqa: E501
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

    @property
    def session_integration_id(self):
        """Gets the session_integration_id of this ModelReturn.  # noqa: E501

        The integration ID of the session this return was requested on.  # noqa: E501

        :return: The session_integration_id of this ModelReturn.  # noqa: E501
        :rtype: str
        """
        return self._session_integration_id

    @session_integration_id.setter
    def session_integration_id(self, session_integration_id):
        """Sets the session_integration_id of this ModelReturn.

        The integration ID of the session this return was requested on.  # noqa: E501

        :param session_integration_id: The session_integration_id of this ModelReturn.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and session_integration_id is None:  # noqa: E501
            raise ValueError("Invalid value for `session_integration_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                session_integration_id is not None and len(session_integration_id) > 1000):
            raise ValueError("Invalid value for `session_integration_id`, length must be less than or equal to `1000`")  # noqa: E501

        self._session_integration_id = session_integration_id

    @property
    def profile_id(self):
        """Gets the profile_id of this ModelReturn.  # noqa: E501

        The internal ID of the profile this return was requested on.  # noqa: E501

        :return: The profile_id of this ModelReturn.  # noqa: E501
        :rtype: int
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this ModelReturn.

        The internal ID of the profile this return was requested on.  # noqa: E501

        :param profile_id: The profile_id of this ModelReturn.  # noqa: E501
        :type: int
        """

        self._profile_id = profile_id

    @property
    def profile_integration_id(self):
        """Gets the profile_integration_id of this ModelReturn.  # noqa: E501

        The integration ID of the profile this return was requested on.  # noqa: E501

        :return: The profile_integration_id of this ModelReturn.  # noqa: E501
        :rtype: str
        """
        return self._profile_integration_id

    @profile_integration_id.setter
    def profile_integration_id(self, profile_integration_id):
        """Sets the profile_integration_id of this ModelReturn.

        The integration ID of the profile this return was requested on.  # noqa: E501

        :param profile_integration_id: The profile_integration_id of this ModelReturn.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                profile_integration_id is not None and len(profile_integration_id) > 1000):
            raise ValueError("Invalid value for `profile_integration_id`, length must be less than or equal to `1000`")  # noqa: E501

        self._profile_integration_id = profile_integration_id

    @property
    def created_by(self):
        """Gets the created_by of this ModelReturn.  # noqa: E501

        ID of the user who requested this return.  # noqa: E501

        :return: The created_by of this ModelReturn.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ModelReturn.

        ID of the user who requested this return.  # noqa: E501

        :param created_by: The created_by of this ModelReturn.  # noqa: E501
        :type: int
        """

        self._created_by = created_by

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
        if not isinstance(other, ModelReturn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelReturn):
            return True

        return self.to_dict() != other.to_dict()
