# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.download import Download  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPDFUtilityController(BaseTestCase):
    """PDFUtilityController integration test stubs"""

    def test_post_imagetopdf(self):
        """Test case for post_imagetopdf

        Converts an image into PDF format file.
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example',
                    lang='lang_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/imagetopdf',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_pdftoimage(self):
        """Test case for post_pdftoimage

        Converts PDF file into image.
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example',
                    quality=100)
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/pdftoimage',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
