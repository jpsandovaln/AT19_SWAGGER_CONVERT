import connexion
import six

from swagger_server.models.download import Download  # noqa: E501
from swagger_server import util


def post_imagebw(input_file, output_file):  # noqa: E501
    """Converts an image into black and white image

     # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str

    :rtype: Download
    """
    return 'do some magic!'


def post_imageflip(input_file, output_file):  # noqa: E501
    """Converts an image into a flipped image.

     # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str

    :rtype: Download
    """
    return 'do some magic!'


def post_imageresize(input_file, output_file, new_size):  # noqa: E501
    """Resizes an image

     # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str
    :param new_size: 
    :type new_size: str

    :rtype: Download
    """
    return 'do some magic!'


def post_imagerotate(input_file, output_file, grades):  # noqa: E501
    """Rotates an image specified n-degrees.

     # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str
    :param grades: 
    :type grades: str

    :rtype: Download
    """
    return 'do some magic!'


def post_imagetoimages(input_file, output_file):  # noqa: E501
    """Convert image to another type of image

     # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str

    :rtype: Download
    """
    return 'do some magic!'


def post_imagetotext(input_file=None, output_file=None, lang=None):  # noqa: E501
    """Image to text

    Converts an image into txt file # noqa: E501

    :param input_file: 
    :type input_file: strstr
    :param output_file: 
    :type output_file: str
    :param lang: 
    :type lang: str

    :rtype: Download
    """
    return 'do some magic!'
