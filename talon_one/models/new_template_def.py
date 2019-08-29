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

from talon_one.models.template_arg_def import TemplateArgDef  # noqa: F401,E501


class NewTemplateDef(object):
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
        'title': 'str',
        'description': 'str',
        'help': 'str',
        'category': 'str',
        'expr': 'list[object]',
        'args': 'list[TemplateArgDef]',
        'expose': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'help': 'help',
        'category': 'category',
        'expr': 'expr',
        'args': 'args',
        'expose': 'expose'
    }

    def __init__(self, title=None, description=None, help=None, category=None, expr=None, args=None, expose=False):  # noqa: E501
        """NewTemplateDef - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._description = None
        self._help = None
        self._category = None
        self._expr = None
        self._args = None
        self._expose = None
        self.discriminator = None

        self.title = title
        if description is not None:
            self.description = description
        if help is not None:
            self.help = help
        self.category = category
        self.expr = expr
        self.args = args
        if expose is not None:
            self.expose = expose

    @property
    def title(self):
        """Gets the title of this NewTemplateDef.  # noqa: E501

        Campaigner-friendly name for the template that will be shown in the rule editor.  # noqa: E501

        :return: The title of this NewTemplateDef.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NewTemplateDef.

        Campaigner-friendly name for the template that will be shown in the rule editor.  # noqa: E501

        :param title: The title of this NewTemplateDef.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if title is not None and len(title) < 1:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this NewTemplateDef.  # noqa: E501

        A short description of the template that will be shown in the rule editor.  # noqa: E501

        :return: The description of this NewTemplateDef.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NewTemplateDef.

        A short description of the template that will be shown in the rule editor.  # noqa: E501

        :param description: The description of this NewTemplateDef.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def help(self):
        """Gets the help of this NewTemplateDef.  # noqa: E501

        Extended help text for the template.  # noqa: E501

        :return: The help of this NewTemplateDef.  # noqa: E501
        :rtype: str
        """
        return self._help

    @help.setter
    def help(self, help):
        """Sets the help of this NewTemplateDef.

        Extended help text for the template.  # noqa: E501

        :param help: The help of this NewTemplateDef.  # noqa: E501
        :type: str
        """

        self._help = help

    @property
    def category(self):
        """Gets the category of this NewTemplateDef.  # noqa: E501

        Used for grouping templates in the rule editor sidebar.  # noqa: E501

        :return: The category of this NewTemplateDef.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this NewTemplateDef.

        Used for grouping templates in the rule editor sidebar.  # noqa: E501

        :param category: The category of this NewTemplateDef.  # noqa: E501
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501
        if category is not None and len(category) < 1:
            raise ValueError("Invalid value for `category`, length must be greater than or equal to `1`")  # noqa: E501

        self._category = category

    @property
    def expr(self):
        """Gets the expr of this NewTemplateDef.  # noqa: E501

        A Talang expression that contains variable bindings referring to args.  # noqa: E501

        :return: The expr of this NewTemplateDef.  # noqa: E501
        :rtype: list[object]
        """
        return self._expr

    @expr.setter
    def expr(self, expr):
        """Sets the expr of this NewTemplateDef.

        A Talang expression that contains variable bindings referring to args.  # noqa: E501

        :param expr: The expr of this NewTemplateDef.  # noqa: E501
        :type: list[object]
        """
        if expr is None:
            raise ValueError("Invalid value for `expr`, must not be `None`")  # noqa: E501

        self._expr = expr

    @property
    def args(self):
        """Gets the args of this NewTemplateDef.  # noqa: E501

        An array of argument definitions.  # noqa: E501

        :return: The args of this NewTemplateDef.  # noqa: E501
        :rtype: list[TemplateArgDef]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this NewTemplateDef.

        An array of argument definitions.  # noqa: E501

        :param args: The args of this NewTemplateDef.  # noqa: E501
        :type: list[TemplateArgDef]
        """
        if args is None:
            raise ValueError("Invalid value for `args`, must not be `None`")  # noqa: E501

        self._args = args

    @property
    def expose(self):
        """Gets the expose of this NewTemplateDef.  # noqa: E501

        A flag to control exposure in Rule Builder.  # noqa: E501

        :return: The expose of this NewTemplateDef.  # noqa: E501
        :rtype: bool
        """
        return self._expose

    @expose.setter
    def expose(self, expose):
        """Sets the expose of this NewTemplateDef.

        A flag to control exposure in Rule Builder.  # noqa: E501

        :param expose: The expose of this NewTemplateDef.  # noqa: E501
        :type: bool
        """

        self._expose = expose

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
        if issubclass(NewTemplateDef, dict):
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
        if not isinstance(other, NewTemplateDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
