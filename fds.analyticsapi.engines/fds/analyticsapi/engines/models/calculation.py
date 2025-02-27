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


class Calculation(object):
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
        'pa': 'dict(str, PACalculationParameters)',
        'spar': 'dict(str, SPARCalculationParameters)',
        'vault': 'dict(str, VaultCalculationParameters)'
    }

    attribute_map = {
        'pa': 'pa',
        'spar': 'spar',
        'vault': 'vault'
    }

    def __init__(self, pa=None, spar=None, vault=None, local_vars_configuration=None):  # noqa: E501
        """Calculation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pa = None
        self._spar = None
        self._vault = None
        self.discriminator = None

        if pa is not None:
            self.pa = pa
        if spar is not None:
            self.spar = spar
        if vault is not None:
            self.vault = vault

    @property
    def pa(self):
        """Gets the pa of this Calculation.  # noqa: E501


        :return: The pa of this Calculation.  # noqa: E501
        :rtype: dict(str, PACalculationParameters)
        """
        return self._pa

    @pa.setter
    def pa(self, pa):
        """Sets the pa of this Calculation.


        :param pa: The pa of this Calculation.  # noqa: E501
        :type: dict(str, PACalculationParameters)
        """

        self._pa = pa

    @property
    def spar(self):
        """Gets the spar of this Calculation.  # noqa: E501


        :return: The spar of this Calculation.  # noqa: E501
        :rtype: dict(str, SPARCalculationParameters)
        """
        return self._spar

    @spar.setter
    def spar(self, spar):
        """Sets the spar of this Calculation.


        :param spar: The spar of this Calculation.  # noqa: E501
        :type: dict(str, SPARCalculationParameters)
        """

        self._spar = spar

    @property
    def vault(self):
        """Gets the vault of this Calculation.  # noqa: E501


        :return: The vault of this Calculation.  # noqa: E501
        :rtype: dict(str, VaultCalculationParameters)
        """
        return self._vault

    @vault.setter
    def vault(self, vault):
        """Sets the vault of this Calculation.


        :param vault: The vault of this Calculation.  # noqa: E501
        :type: dict(str, VaultCalculationParameters)
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
        if not isinstance(other, Calculation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Calculation):
            return True

        return self.to_dict() != other.to_dict()
