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


class User(object):
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
        'modified': 'datetime',
        'email': 'str',
        'account_id': 'int',
        'invite_token': 'str',
        'state': 'str',
        'name': 'str',
        'policy': 'str',
        'release_update': 'bool',
        'latest_feature': 'str',
        'roles': 'list[int]',
        'application_notification_subscriptions': 'object',
        'auth_method': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'modified': 'modified',
        'email': 'email',
        'account_id': 'accountId',
        'invite_token': 'inviteToken',
        'state': 'state',
        'name': 'name',
        'policy': 'policy',
        'release_update': 'releaseUpdate',
        'latest_feature': 'latestFeature',
        'roles': 'roles',
        'application_notification_subscriptions': 'applicationNotificationSubscriptions',
        'auth_method': 'authMethod'
    }

    def __init__(self, id=None, created=None, modified=None, email=None, account_id=None, invite_token=None, state=None, name=None, policy=None, release_update=None, latest_feature=None, roles=None, application_notification_subscriptions=None, auth_method=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created = None
        self._modified = None
        self._email = None
        self._account_id = None
        self._invite_token = None
        self._state = None
        self._name = None
        self._policy = None
        self._release_update = None
        self._latest_feature = None
        self._roles = None
        self._application_notification_subscriptions = None
        self._auth_method = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.modified = modified
        self.email = email
        self.account_id = account_id
        self.invite_token = invite_token
        self.state = state
        self.name = name
        self.policy = policy
        self.release_update = release_update
        if latest_feature is not None:
            self.latest_feature = latest_feature
        if roles is not None:
            self.roles = roles
        if application_notification_subscriptions is not None:
            self.application_notification_subscriptions = application_notification_subscriptions
        if auth_method is not None:
            self.auth_method = auth_method

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501

        Unique ID for this entity.  # noqa: E501

        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        Unique ID for this entity.  # noqa: E501

        :param id: The id of this User.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this User.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this User.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this User.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this User.  # noqa: E501

        The exact moment this entity was last modified.  # noqa: E501

        :return: The modified of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this User.

        The exact moment this entity was last modified.  # noqa: E501

        :param modified: The modified of this User.  # noqa: E501
        :type: datetime
        """
        if modified is None:
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        The email address associated with your account.  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        The email address associated with your account.  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def account_id(self):
        """Gets the account_id of this User.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The account_id of this User.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this User.

        The ID of the account that owns this entity.  # noqa: E501

        :param account_id: The account_id of this User.  # noqa: E501
        :type: int
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def invite_token(self):
        """Gets the invite_token of this User.  # noqa: E501

        Invite token, empty if the user as already accepted their invite.  # noqa: E501

        :return: The invite_token of this User.  # noqa: E501
        :rtype: str
        """
        return self._invite_token

    @invite_token.setter
    def invite_token(self, invite_token):
        """Sets the invite_token of this User.

        Invite token, empty if the user as already accepted their invite.  # noqa: E501

        :param invite_token: The invite_token of this User.  # noqa: E501
        :type: str
        """
        if invite_token is None:
            raise ValueError("Invalid value for `invite_token`, must not be `None`")  # noqa: E501

        self._invite_token = invite_token

    @property
    def state(self):
        """Gets the state of this User.  # noqa: E501

        Current user state.  # noqa: E501

        :return: The state of this User.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this User.

        Current user state.  # noqa: E501

        :param state: The state of this User.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["invited", "active", "deactivated"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501

        Full name  # noqa: E501

        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.

        Full name  # noqa: E501

        :param name: The name of this User.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def policy(self):
        """Gets the policy of this User.  # noqa: E501

        A blob of ACL JSON  # noqa: E501

        :return: The policy of this User.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this User.

        A blob of ACL JSON  # noqa: E501

        :param policy: The policy of this User.  # noqa: E501
        :type: str
        """
        if policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    @property
    def release_update(self):
        """Gets the release_update of this User.  # noqa: E501

        Update the user via email  # noqa: E501

        :return: The release_update of this User.  # noqa: E501
        :rtype: bool
        """
        return self._release_update

    @release_update.setter
    def release_update(self, release_update):
        """Sets the release_update of this User.

        Update the user via email  # noqa: E501

        :param release_update: The release_update of this User.  # noqa: E501
        :type: bool
        """
        if release_update is None:
            raise ValueError("Invalid value for `release_update`, must not be `None`")  # noqa: E501

        self._release_update = release_update

    @property
    def latest_feature(self):
        """Gets the latest_feature of this User.  # noqa: E501

        Latest feature the user has been notified.  # noqa: E501

        :return: The latest_feature of this User.  # noqa: E501
        :rtype: str
        """
        return self._latest_feature

    @latest_feature.setter
    def latest_feature(self, latest_feature):
        """Sets the latest_feature of this User.

        Latest feature the user has been notified.  # noqa: E501

        :param latest_feature: The latest_feature of this User.  # noqa: E501
        :type: str
        """

        self._latest_feature = latest_feature

    @property
    def roles(self):
        """Gets the roles of this User.  # noqa: E501

        Contains a list of all roles a user is a memeber of  # noqa: E501

        :return: The roles of this User.  # noqa: E501
        :rtype: list[int]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this User.

        Contains a list of all roles a user is a memeber of  # noqa: E501

        :param roles: The roles of this User.  # noqa: E501
        :type: list[int]
        """

        self._roles = roles

    @property
    def application_notification_subscriptions(self):
        """Gets the application_notification_subscriptions of this User.  # noqa: E501


        :return: The application_notification_subscriptions of this User.  # noqa: E501
        :rtype: object
        """
        return self._application_notification_subscriptions

    @application_notification_subscriptions.setter
    def application_notification_subscriptions(self, application_notification_subscriptions):
        """Sets the application_notification_subscriptions of this User.


        :param application_notification_subscriptions: The application_notification_subscriptions of this User.  # noqa: E501
        :type: object
        """

        self._application_notification_subscriptions = application_notification_subscriptions

    @property
    def auth_method(self):
        """Gets the auth_method of this User.  # noqa: E501

        The Authentication method for this user  # noqa: E501

        :return: The auth_method of this User.  # noqa: E501
        :rtype: str
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Sets the auth_method of this User.

        The Authentication method for this user  # noqa: E501

        :param auth_method: The auth_method of this User.  # noqa: E501
        :type: str
        """

        self._auth_method = auth_method

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
