# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Imagetotext(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, input_file: str=None, output_file: str=None, lang: str=None):  # noqa: E501
        """Imagetotext - a model defined in Swagger

        :param input_file: The input_file of this Imagetotext.  # noqa: E501
        :type input_file: str
        :param output_file: The output_file of this Imagetotext.  # noqa: E501
        :type output_file: str
        :param lang: The lang of this Imagetotext.  # noqa: E501
        :type lang: str
        """
        self.swagger_types = {
            'input_file': str,
            'output_file': str,
            'lang': str
        }

        self.attribute_map = {
            'input_file': 'input_file',
            'output_file': 'output_file',
            'lang': 'lang'
        }
        self._input_file = input_file
        self._output_file = output_file
        self._lang = lang

    @classmethod
    def from_dict(cls, dikt) -> 'Imagetotext':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The imagetotext of this Imagetotext.  # noqa: E501
        :rtype: Imagetotext
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input_file(self) -> str:
        """Gets the input_file of this Imagetotext.

        Choose image file to convert:  # noqa: E501

        :return: The input_file of this Imagetotext.
        :rtype: str
        """
        return self._input_file

    @input_file.setter
    def input_file(self, input_file: str):
        """Sets the input_file of this Imagetotext.

        Choose image file to convert:  # noqa: E501

        :param input_file: The input_file of this Imagetotext.
        :type input_file: str
        """
        if input_file is None:
            raise ValueError("Invalid value for `input_file`, must not be `None`")  # noqa: E501

        self._input_file = input_file

    @property
    def output_file(self) -> str:
        """Gets the output_file of this Imagetotext.


        :return: The output_file of this Imagetotext.
        :rtype: str
        """
        return self._output_file

    @output_file.setter
    def output_file(self, output_file: str):
        """Sets the output_file of this Imagetotext.


        :param output_file: The output_file of this Imagetotext.
        :type output_file: str
        """
        allowed_values = ["txt"]  # noqa: E501
        if output_file not in allowed_values:
            raise ValueError(
                "Invalid value for `output_file` ({0}), must be one of {1}"
                .format(output_file, allowed_values)
            )

        self._output_file = output_file

    @property
    def lang(self) -> str:
        """Gets the lang of this Imagetotext.

        Language encoding <i>(default: \"eng\", select \"spa\" to include latin special characters)</i>:  # noqa: E501

        :return: The lang of this Imagetotext.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang: str):
        """Sets the lang of this Imagetotext.

        Language encoding <i>(default: \"eng\", select \"spa\" to include latin special characters)</i>:  # noqa: E501

        :param lang: The lang of this Imagetotext.
        :type lang: str
        """
        allowed_values = ["eng", "spa", "eng+spa"]  # noqa: E501
        if lang not in allowed_values:
            raise ValueError(
                "Invalid value for `lang` ({0}), must be one of {1}"
                .format(lang, allowed_values)
            )

        self._lang = lang
