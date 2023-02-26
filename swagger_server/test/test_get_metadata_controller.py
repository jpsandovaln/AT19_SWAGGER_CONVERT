# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.download import Download  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetMetadataController(BaseTestCase):
    """GetMetadataController integration test stubs"""

    def test_post_metadatageter(self):
        """Test case for post_metadatageter

        Gets metadata from a file
        """
        data = dict(input_file='input_file_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/metadatageter',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
