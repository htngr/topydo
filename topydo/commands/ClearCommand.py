import sys


def get_platform():
    os = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in os:
        return sys.platform

    # return print(os[sys.platform])
    return os[sys.platform]
