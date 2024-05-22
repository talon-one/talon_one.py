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


class Attribute(object):
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
        'entity': 'str',
        'event_type': 'str',
        'name': 'str',
        'title': 'str',
        'type': 'str',
        'description': 'str',
        'suggestions': 'list[str]',
        'has_allowed_list': 'bool',
        'restricted_by_suggestions': 'bool',
        'editable': 'bool',
        'subscribed_applications_ids': 'list[int]',
        'subscribed_catalogs_ids': 'list[int]',
        'allowed_subscriptions': 'list[str]',
        'event_type_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'account_id': 'accountId',
        'entity': 'entity',
        'event_type': 'eventType',
        'name': 'name',
        'title': 'title',
        'type': 'type',
        'description': 'description',
        'suggestions': 'suggestions',
        'has_allowed_list': 'hasAllowedList',
        'restricted_by_suggestions': 'restrictedBySuggestions',
        'editable': 'editable',
        'subscribed_applications_ids': 'subscribedApplicationsIds',
        'subscribed_catalogs_ids': 'subscribedCatalogsIds',
        'allowed_subscriptions': 'allowedSubscriptions',
        'event_type_id': 'eventTypeId'
    }

    def __init__(self, id=None, created=None, account_id=None, entity=None, event_type=None, name=None, title=None, type=None, description=None, suggestions=None, has_allowed_list=False, restricted_by_suggestions=False, editable=None, subscribed_applications_ids=None, subscribed_catalogs_ids=None, allowed_subscriptions=None, event_type_id=None, local_vars_configuration=None):  # noqa: E501
        """Attribute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._account_id = None
        self._entity = None
        self._event_type = None
        self._name = None
        self._title = None
        self._type = None
        self._description = None
        self._suggestions = None
        self._has_allowed_list = None
        self._restricted_by_suggestions = None
        self._editable = None
        self._subscribed_applications_ids = None
        self._subscribed_catalogs_ids = None
        self._allowed_subscriptions = None
        self._event_type_id = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.account_id = account_id
        self.entity = entity
        if event_type is not None:
            self.event_type = event_type
        self.name = name
        self.title = title
        self.type = type
        self.description = description
        self.suggestions = suggestions
        if has_allowed_list is not None:
            self.has_allowed_list = has_allowed_list
        if restricted_by_suggestions is not None:
            self.restricted_by_suggestions = restricted_by_suggestions
        self.editable = editable
        if subscribed_applications_ids is not None:
            self.subscribed_applications_ids = subscribed_applications_ids
        if subscribed_catalogs_ids is not None:
            self.subscribed_catalogs_ids = subscribed_catalogs_ids
        if allowed_subscriptions is not None:
            self.allowed_subscriptions = allowed_subscriptions
        if event_type_id is not None:
            self.event_type_id = event_type_id

    @property
    def id(self):
        """Gets the id of this Attribute.  # noqa: E501

        Internal ID of this entity.  # noqa: E501

        :return: The id of this Attribute.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Attribute.

        Internal ID of this entity.  # noqa: E501

        :param id: The id of this Attribute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Attribute.  # noqa: E501

        The time this entity was created.  # noqa: E501

        :return: The created of this Attribute.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Attribute.

        The time this entity was created.  # noqa: E501

        :param created: The created of this Attribute.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def account_id(self):
        """Gets the account_id of this Attribute.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The account_id of this Attribute.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Attribute.

        The ID of the account that owns this entity.  # noqa: E501

        :param account_id: The account_id of this Attribute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def entity(self):
        """Gets the entity of this Attribute.  # noqa: E501

        The name of the entity that can have this attribute. When creating or updating the entities of a given type, you can include an `attributes` object with keys corresponding to the `name` of the custom attributes for that type.  # noqa: E501

        :return: The entity of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this Attribute.

        The name of the entity that can have this attribute. When creating or updating the entities of a given type, you can include an `attributes` object with keys corresponding to the `name` of the custom attributes for that type.  # noqa: E501

        :param entity: The entity of this Attribute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and entity is None:  # noqa: E501
            raise ValueError("Invalid value for `entity`, must not be `None`")  # noqa: E501
        allowed_values = ["Account", "Application", "Campaign", "CustomerProfile", "CustomerSession", "CartItem", "Coupon", "Event", "Giveaway", "Referral", "Store"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and entity not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `entity` ({0}), must be one of {1}"  # noqa: E501
                .format(entity, allowed_values)
            )

        self._entity = entity

    @property
    def event_type(self):
        """Gets the event_type of this Attribute.  # noqa: E501


        :return: The event_type of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Attribute.


        :param event_type: The event_type of this Attribute.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def name(self):
        """Gets the name of this Attribute.  # noqa: E501

        The attribute name that will be used in API requests and Talang. E.g. if `name == \"region\"` then you would set the region attribute by including an `attributes.region` property in your request payload.  # noqa: E501

        :return: The name of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Attribute.

        The attribute name that will be used in API requests and Talang. E.g. if `name == \"region\"` then you would set the region attribute by including an `attributes.region` property in your request payload.  # noqa: E501

        :param name: The name of this Attribute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[A-Za-z]\w*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z]\w*$/`")  # noqa: E501

        self._name = name

    @property
    def title(self):
        """Gets the title of this Attribute.  # noqa: E501

        The human-readable name for the attribute that will be shown in the Campaign Manager. Like `name`, the combination of entity and title must also be unique.  # noqa: E501

        :return: The title of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Attribute.

        The human-readable name for the attribute that will be shown in the Campaign Manager. Like `name`, the combination of entity and title must also be unique.  # noqa: E501

        :param title: The title of this Attribute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and not re.search(r'^[A-Za-z][A-Za-z0-9_.!~*\'() -]*$', title)):  # noqa: E501
            raise ValueError(r"Invalid value for `title`, must be a follow pattern or equal to `/^[A-Za-z][A-Za-z0-9_.!~*'() -]*$/`")  # noqa: E501

        self._title = title

    @property
    def type(self):
        """Gets the type of this Attribute.  # noqa: E501

        The data type of the attribute, a `time` attribute must be sent as a string that conforms to the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp format.  # noqa: E501

        :return: The type of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Attribute.

        The data type of the attribute, a `time` attribute must be sent as a string that conforms to the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp format.  # noqa: E501

        :param type: The type of this Attribute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["string", "number", "boolean", "time", "(list string)", "(list number)", "(list time)", "location", "(list location)"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def description(self):
        """Gets the description of this Attribute.  # noqa: E501

        A description of this attribute.  # noqa: E501

        :return: The description of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Attribute.

        A description of this attribute.  # noqa: E501

        :param description: The description of this Attribute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def suggestions(self):
        """Gets the suggestions of this Attribute.  # noqa: E501

        A list of suggestions for the attribute.  # noqa: E501

        :return: The suggestions of this Attribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._suggestions

    @suggestions.setter
    def suggestions(self, suggestions):
        """Sets the suggestions of this Attribute.

        A list of suggestions for the attribute.  # noqa: E501

        :param suggestions: The suggestions of this Attribute.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and suggestions is None:  # noqa: E501
            raise ValueError("Invalid value for `suggestions`, must not be `None`")  # noqa: E501

        self._suggestions = suggestions

    @property
    def has_allowed_list(self):
        """Gets the has_allowed_list of this Attribute.  # noqa: E501

        Whether or not this attribute has an allowed list of values associated with it.  # noqa: E501

        :return: The has_allowed_list of this Attribute.  # noqa: E501
        :rtype: bool
        """
        return self._has_allowed_list

    @has_allowed_list.setter
    def has_allowed_list(self, has_allowed_list):
        """Sets the has_allowed_list of this Attribute.

        Whether or not this attribute has an allowed list of values associated with it.  # noqa: E501

        :param has_allowed_list: The has_allowed_list of this Attribute.  # noqa: E501
        :type: bool
        """

        self._has_allowed_list = has_allowed_list

    @property
    def restricted_by_suggestions(self):
        """Gets the restricted_by_suggestions of this Attribute.  # noqa: E501

        Whether or not this attribute's value is restricted by suggestions (`suggestions` property) or by an allowed list of value (`hasAllowedList` property).   # noqa: E501

        :return: The restricted_by_suggestions of this Attribute.  # noqa: E501
        :rtype: bool
        """
        return self._restricted_by_suggestions

    @restricted_by_suggestions.setter
    def restricted_by_suggestions(self, restricted_by_suggestions):
        """Sets the restricted_by_suggestions of this Attribute.

        Whether or not this attribute's value is restricted by suggestions (`suggestions` property) or by an allowed list of value (`hasAllowedList` property).   # noqa: E501

        :param restricted_by_suggestions: The restricted_by_suggestions of this Attribute.  # noqa: E501
        :type: bool
        """

        self._restricted_by_suggestions = restricted_by_suggestions

    @property
    def editable(self):
        """Gets the editable of this Attribute.  # noqa: E501

        Whether or not this attribute can be edited.  # noqa: E501

        :return: The editable of this Attribute.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this Attribute.

        Whether or not this attribute can be edited.  # noqa: E501

        :param editable: The editable of this Attribute.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and editable is None:  # noqa: E501
            raise ValueError("Invalid value for `editable`, must not be `None`")  # noqa: E501

        self._editable = editable

    @property
    def subscribed_applications_ids(self):
        """Gets the subscribed_applications_ids of this Attribute.  # noqa: E501

        A list of the IDs of the applications where this attribute is available.  # noqa: E501

        :return: The subscribed_applications_ids of this Attribute.  # noqa: E501
        :rtype: list[int]
        """
        return self._subscribed_applications_ids

    @subscribed_applications_ids.setter
    def subscribed_applications_ids(self, subscribed_applications_ids):
        """Sets the subscribed_applications_ids of this Attribute.

        A list of the IDs of the applications where this attribute is available.  # noqa: E501

        :param subscribed_applications_ids: The subscribed_applications_ids of this Attribute.  # noqa: E501
        :type: list[int]
        """

        self._subscribed_applications_ids = subscribed_applications_ids

    @property
    def subscribed_catalogs_ids(self):
        """Gets the subscribed_catalogs_ids of this Attribute.  # noqa: E501

        A list of the IDs of the catalogs where this attribute is available.  # noqa: E501

        :return: The subscribed_catalogs_ids of this Attribute.  # noqa: E501
        :rtype: list[int]
        """
        return self._subscribed_catalogs_ids

    @subscribed_catalogs_ids.setter
    def subscribed_catalogs_ids(self, subscribed_catalogs_ids):
        """Sets the subscribed_catalogs_ids of this Attribute.

        A list of the IDs of the catalogs where this attribute is available.  # noqa: E501

        :param subscribed_catalogs_ids: The subscribed_catalogs_ids of this Attribute.  # noqa: E501
        :type: list[int]
        """

        self._subscribed_catalogs_ids = subscribed_catalogs_ids

    @property
    def allowed_subscriptions(self):
        """Gets the allowed_subscriptions of this Attribute.  # noqa: E501

        A list of allowed subscription types for this attribute.  **Note:** This only applies to attributes associated with the `CartItem` entity.   # noqa: E501

        :return: The allowed_subscriptions of this Attribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_subscriptions

    @allowed_subscriptions.setter
    def allowed_subscriptions(self, allowed_subscriptions):
        """Sets the allowed_subscriptions of this Attribute.

        A list of allowed subscription types for this attribute.  **Note:** This only applies to attributes associated with the `CartItem` entity.   # noqa: E501

        :param allowed_subscriptions: The allowed_subscriptions of this Attribute.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["application", "catalog"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(allowed_subscriptions).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `allowed_subscriptions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(allowed_subscriptions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._allowed_subscriptions = allowed_subscriptions

    @property
    def event_type_id(self):
        """Gets the event_type_id of this Attribute.  # noqa: E501


        :return: The event_type_id of this Attribute.  # noqa: E501
        :rtype: int
        """
        return self._event_type_id

    @event_type_id.setter
    def event_type_id(self, event_type_id):
        """Sets the event_type_id of this Attribute.


        :param event_type_id: The event_type_id of this Attribute.  # noqa: E501
        :type: int
        """

        self._event_type_id = event_type_id

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
        if not isinstance(other, Attribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Attribute):
            return True

        return self.to_dict() != other.to_dict()
