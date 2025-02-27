# coding: utf-8

"""
    Engines API

    Allow clients to fetch Engines Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: 2
    Contact: analytics.api.support@factset.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fds.analyticsapi.engines.configuration import Configuration


class CalculationStatus(object):
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
        'status': 'str',
        'points': 'int',
        'pa': 'dict(str, CalculationUnitStatus)',
        'spar': 'dict(str, CalculationUnitStatus)',
        'vault': 'dict(str, CalculationUnitStatus)'
    }

    attribute_map = {
        'status': 'status',
        'points': 'points',
        'pa': 'pa',
        'spar': 'spar',
        'vault': 'vault'
    }

    def __init__(self, status=None, points=None, pa=None, spar=None, vault=None, local_vars_configuration=None):  # noqa: E501
        """CalculationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._points = None
        self._pa = None
        self._spar = None
        self._vault = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if points is not None:
            self.points = points
        if pa is not None:
            self.pa = pa
        if spar is not None:
            self.spar = spar
        if vault is not None:
            self.vault = vault

    @property
    def status(self):
        """Gets the status of this CalculationStatus.  # noqa: E501


        :return: The status of this CalculationStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CalculationStatus.


        :param status: The status of this CalculationStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["Queued", "Executing", "Completed", "Cancelled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def points(self):
        """Gets the points of this CalculationStatus.  # noqa: E501


        :return: The points of this CalculationStatus.  # noqa: E501
        :rtype: int
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this CalculationStatus.


        :param points: The points of this CalculationStatus.  # noqa: E501
        :type: int
        """

        self._points = points

    @property
    def pa(self):
        """Gets the pa of this CalculationStatus.  # noqa: E501


        :return: The pa of this CalculationStatus.  # noqa: E501
        :rtype: dict(str, CalculationUnitStatus)
        """
        return self._pa

    @pa.setter
    def pa(self, pa):
        """Sets the pa of this CalculationStatus.


        :param pa: The pa of this CalculationStatus.  # noqa: E501
        :type: dict(str, CalculationUnitStatus)
        """

        self._pa = pa

    @property
    def spar(self):
        """Gets the spar of this CalculationStatus.  # noqa: E501


        :return: The spar of this CalculationStatus.  # noqa: E501
        :rtype: dict(str, CalculationUnitStatus)
        """
        return self._spar

    @spar.setter
    def spar(self, spar):
        """Sets the spar of this CalculationStatus.


        :param spar: The spar of this CalculationStatus.  # noqa: E501
        :type: dict(str, CalculationUnitStatus)
        """

        self._spar = spar

    @property
    def vault(self):
        """Gets the vault of this CalculationStatus.  # noqa: E501


        :return: The vault of this CalculationStatus.  # noqa: E501
        :rtype: dict(str, CalculationUnitStatus)
        """
        return self._vault

    @vault.setter
    def vault(self, vault):
        """Sets the vault of this CalculationStatus.


        :param vault: The vault of this CalculationStatus.  # noqa: E501
        :type: dict(str, CalculationUnitStatus)
        """

        self._vault = vault

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
        if not isinstance(other, CalculationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CalculationStatus):
            return True

        return self.to_dict() != other.to_dict()
