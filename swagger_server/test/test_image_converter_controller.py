# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.download import Download  # noqa: E501
from swagger_server.test import BaseTestCase


class TestImageConverterController(BaseTestCase):
    """ImageConverterController integration test stubs"""

    def test_post_imagebw(self):
        """Test case for post_imagebw

        Converts an image into black and white image
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/imagebw',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_imageflip(self):
        """Test case for post_imageflip

        Converts an image into a flipped image.
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/imageflip',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_imageresize(self):
        """Test case for post_imageresize

        Resizes an image
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example',
                    new_size='new_size_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/imageresize',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_imagerotate(self):
        """Test case for post_imagerotate

        Rotates an image specified n-degrees.
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example',
                    grades='grades_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/imagerotate',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_imagetoimages(self):
        """Test case for post_imagetoimages

        Convert image to another type of image
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/imagetoimage',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_imagetotext(self):
        """Test case for post_imagetotext

        Image to text
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example',
                    lang='lang_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/imagetotext',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
