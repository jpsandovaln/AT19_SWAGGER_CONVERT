# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.download import Download  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVideoConverterController(BaseTestCase):
    """VideoConverterController integration test stubs"""

    def test_post_videotoimages(self):
        """Test case for post_videotoimages

        Extracts and compress images from a video into a zip file.
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example',
                    fps='fps_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/videotoimage/zip',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_videotovideo(self):
        """Test case for post_videotovideo

        Converts video format.
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/videotovideo',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
