import os
import sys


# project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def env_mode():
    """
    Check if we want to be in dev mode or staging mode, this will be used to pull in correct settings overrides.
    :return bool:
    """
    if os.environ.get('DEV_MODE') is not None:
        return 'DEV'
    if os.environ.get('STAGING_MODE') is not None:
        return 'STAGING'


def in_test_mode():
    if sys.argv[1:2] == ['test']:
        return True
    return False


def show_toolbar(request):
    """
    Force debug toolbar due to issue inside docker from external to container.

    Additionally we dont want this to be true if we are running tests locally in docker
    as this is not an accurate reflection of the live codebase.

    :param request:
    :return bool:
    """
    if in_test_mode():
        return False
    return False
    # return True
