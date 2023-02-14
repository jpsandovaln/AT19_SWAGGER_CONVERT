# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Audioincreasedvolume(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, input_file: str=None, output_file: str=None, multiplier: float=None):  # noqa: E501
        """Audioincreasedvolume - a model defined in Swagger

        :param input_file: The input_file of this Audioincreasedvolume.  # noqa: E501
        :type input_file: str
        :param output_file: The output_file of this Audioincreasedvolume.  # noqa: E501
        :type output_file: str
        :param multiplier: The multiplier of this Audioincreasedvolume.  # noqa: E501
        :type multiplier: float
        """
        self.swagger_types = {
            'input_file': str,
            'output_file': str,
            'multiplier': float
        }

        self.attribute_map = {
            'input_file': 'input_file',
            'output_file': 'output_file',
            'multiplier': 'multiplier'
        }
        self._input_file = input_file
        self._output_file = output_file
        self._multiplier = multiplier

    @classmethod
    def from_dict(cls, dikt) -> 'Audioincreasedvolume':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The audioincreasedvolume of this Audioincreasedvolume.  # noqa: E501
        :rtype: Audioincreasedvolume
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input_file(self) -> str:
        """Gets the input_file of this Audioincreasedvolume.

        Choose audio file to convert:  # noqa: E501

        :return: The input_file of this Audioincreasedvolume.
        :rtype: str
        """
        return self._input_file

    @input_file.setter
    def input_file(self, input_file: str):
        """Sets the input_file of this Audioincreasedvolume.

        Choose audio file to convert:  # noqa: E501

        :param input_file: The input_file of this Audioincreasedvolume.
        :type input_file: str
        """
        if input_file is None:
            raise ValueError("Invalid value for `input_file`, must not be `None`")  # noqa: E501

        self._input_file = input_file

    @property
    def output_file(self) -> str:
        """Gets the output_file of this Audioincreasedvolume.

        Choose the output format:  # noqa: E501

        :return: The output_file of this Audioincreasedvolume.
        :rtype: str
        """
        return self._output_file

    @output_file.setter
    def output_file(self, output_file: str):
        """Sets the output_file of this Audioincreasedvolume.

        Choose the output format:  # noqa: E501

        :param output_file: The output_file of this Audioincreasedvolume.
        :type output_file: str
        """
        allowed_values = ["mp3", "wav", "ogg", "flac", "wma"]  # noqa: E501
        if output_file not in allowed_values:
            raise ValueError(
                "Invalid value for `output_file` ({0}), must be one of {1}"
                .format(output_file, allowed_values)
            )

        self._output_file = output_file

    @property
    def multiplier(self) -> float:
        """Gets the multiplier of this Audioincreasedvolume.

        Specify the multiplier <i>(To increase volumen write a value greater then 0, to decrease, the value should be lower than 0)</i>:  # noqa: E501

        :return: The multiplier of this Audioincreasedvolume.
        :rtype: float
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier: float):
        """Sets the multiplier of this Audioincreasedvolume.

        Specify the multiplier <i>(To increase volumen write a value greater then 0, to decrease, the value should be lower than 0)</i>:  # noqa: E501

        :param multiplier: The multiplier of this Audioincreasedvolume.
        :type multiplier: float
        """
        if multiplier is None:
            raise ValueError("Invalid value for `multiplier`, must not be `None`")  # noqa: E501

        self._multiplier = multiplier
