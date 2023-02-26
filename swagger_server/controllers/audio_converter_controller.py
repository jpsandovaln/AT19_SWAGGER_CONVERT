import connexion
import six

from swagger_server.models.download import Download  # noqa: E501
from swagger_server import util


def post_audioextractaudio(input_file, output_file):  # noqa: E501
    """Extracts an audio file from a video file

     # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str

    :rtype: Download
    """
    return 'do some magic!'


def post_audioincreasevolume(input_file, output_file, multiplier):  # noqa: E501
    """Get converted type of audio file with increased volume

    Convert inserted audio file to another type of audio file with increased volume # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str
    :param multiplier: 
    :type multiplier: float

    :rtype: Download
    """
    return 'do some magic!'


def post_audiomixaudio(input_file_1=None, input_file_2=None, output_file=None):  # noqa: E501
    """Merges two audio files in one audio file.

     # noqa: E501

    :param input_file_1: 
    :type input_file_1: strstr
    :param input_file_2: 
    :type input_file_2: strstr
    :param output_file: 
    :type output_file: str

    :rtype: Download
    """
    return 'do some magic!'


def post_audiotoaudio(input_file=None, output_file=None):  # noqa: E501
    """Converts audio file to another of audio format file.

     # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str

    :rtype: Download
    """
    return 'do some magic!'
