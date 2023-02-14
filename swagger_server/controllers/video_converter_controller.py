import connexion
import six

from swagger_server.models.download import Download  # noqa: E501
from swagger_server import util


def post_videotoimages(input_file, output_file, fps):  # noqa: E501
    """Extracts and compress images from a video into a zip file.

     # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str
    :param fps: 
    :type fps: str

    :rtype: Download
    """
    return 'do some magic!'


def post_videotovideo(input_file, output_file):  # noqa: E501
    """Converts video format.

     # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str

    :rtype: Download
    """
    return 'do some magic!'
