import connexion
import six

from swagger_server.models.download import Download  # noqa: E501
from swagger_server import util


def get_download(file_name=None):  # noqa: E501
    """Downloads a file.

     # noqa: E501

    :param file_name: Please choose the file to download:
    :type file_name: strstr

    :rtype: Download
    """
    return 'do some magic!'
