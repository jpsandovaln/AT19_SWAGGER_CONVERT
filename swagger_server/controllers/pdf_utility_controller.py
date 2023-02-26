import connexion
import six

from swagger_server.models.download import Download  # noqa: E501
from swagger_server import util


def post_imagetopdf(input_file, output_file, lang):  # noqa: E501
    """Converts an image into PDF format file.

     # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str
    :param lang: 
    :type lang: str

    :rtype: Download
    """
    return 'do some magic!'


def post_pdftoimage(input_file=None, output_file=None, quality=None):  # noqa: E501
    """Converts PDF file into image.

     # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str
    :param quality: 
    :type quality: int

    :rtype: Download
    """
    return 'do some magic!'
