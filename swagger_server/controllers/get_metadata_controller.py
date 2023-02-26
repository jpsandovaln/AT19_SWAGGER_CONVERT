import connexion
import six

from swagger_server.models.download import Download  # noqa: E501
from swagger_server import util


def post_metadatageter(input_file=None):  # noqa: E501
    """Gets metadata from a file

     # noqa: E501

    :param input_file: 
    :type input_file: strstr

    :rtype: Download
    """
    return 'do some magic!'
