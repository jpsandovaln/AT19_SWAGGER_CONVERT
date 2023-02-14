# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.download import Download  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDownloadController(BaseTestCase):
    """DownloadController integration test stubs"""

    def test_get_download(self):
        """Test case for get_download

        Downloads a file.
        """
        query_string = [('file_name', 'file_name_example')]
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/download',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
