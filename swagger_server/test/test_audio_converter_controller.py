# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.download import Download  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAudioConverterController(BaseTestCase):
    """AudioConverterController integration test stubs"""

    def test_post_audioextractaudio(self):
        """Test case for post_audioextractaudio

        Extracts an audio file from a video file
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/audioextractaudio',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_audioincreasevolume(self):
        """Test case for post_audioincreasevolume

        Get converted type of audio file with increased volume
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example',
                    multiplier=1.2)
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/audioincreasevolume',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_audiomixaudio(self):
        """Test case for post_audiomixaudio

        Merges two audio files in one audio file.
        """
        data = dict(input_file_1='input_file_1_example',
                    input_file_2='input_file_2_example',
                    output_file='output_file_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/audiomixaudio',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_audiotoaudio(self):
        """Test case for post_audiotoaudio

        Converts audio file to another of audio format file.
        """
        data = dict(input_file='input_file_example',
                    output_file='output_file_example')
        response = self.client.open(
            '/AT19-Jala.University/Converter_Studio/1.0.11/audiotoaudio',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
