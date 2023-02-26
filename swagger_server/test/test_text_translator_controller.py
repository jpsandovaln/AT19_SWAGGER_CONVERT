# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestTextTranslatorController(BaseTestCase):
    """TextTranslatorController integration test stubs"""

    def test_post_text_translator(self):
        """Test case for post_text_translator

        Translates a text to any language
        """
        data = dict(text='text_example',
                    language='language_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/texttranslator',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
