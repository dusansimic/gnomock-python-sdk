# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.4.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class SplunkValues(object):
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
        'event': 'str',
        'index': 'str',
        'source': 'str',
        'sourcetype': 'str',
        'time': 'float'
    }

    attribute_map = {
        'event': 'event',
        'index': 'index',
        'source': 'source',
        'sourcetype': 'sourcetype',
        'time': 'time'
    }

    def __init__(self, event=None, index=None, source=None, sourcetype=None, time=None, local_vars_configuration=None):  # noqa: E501
        """SplunkValues - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event = None
        self._index = None
        self._source = None
        self._sourcetype = None
        self._time = None
        self.discriminator = None

        self.event = event
        self.index = index
        self.source = source
        self.sourcetype = sourcetype
        self.time = time

    @property
    def event(self):
        """Gets the event of this SplunkValues.  # noqa: E501


        :return: The event of this SplunkValues.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this SplunkValues.


        :param event: The event of this SplunkValues.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and event is None:  # noqa: E501
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def index(self):
        """Gets the index of this SplunkValues.  # noqa: E501


        :return: The index of this SplunkValues.  # noqa: E501
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this SplunkValues.


        :param index: The index of this SplunkValues.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and index is None:  # noqa: E501
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def source(self):
        """Gets the source of this SplunkValues.  # noqa: E501


        :return: The source of this SplunkValues.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SplunkValues.


        :param source: The source of this SplunkValues.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def sourcetype(self):
        """Gets the sourcetype of this SplunkValues.  # noqa: E501


        :return: The sourcetype of this SplunkValues.  # noqa: E501
        :rtype: str
        """
        return self._sourcetype

    @sourcetype.setter
    def sourcetype(self, sourcetype):
        """Sets the sourcetype of this SplunkValues.


        :param sourcetype: The sourcetype of this SplunkValues.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sourcetype is None:  # noqa: E501
            raise ValueError("Invalid value for `sourcetype`, must not be `None`")  # noqa: E501

        self._sourcetype = sourcetype

    @property
    def time(self):
        """Gets the time of this SplunkValues.  # noqa: E501

        timestamp in seconds (or milli-, micro- or nanoseconds)  # noqa: E501

        :return: The time of this SplunkValues.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SplunkValues.

        timestamp in seconds (or milli-, micro- or nanoseconds)  # noqa: E501

        :param time: The time of this SplunkValues.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and time is None:  # noqa: E501
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

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
        if not isinstance(other, SplunkValues):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SplunkValues):
            return True

        return self.to_dict() != other.to_dict()
