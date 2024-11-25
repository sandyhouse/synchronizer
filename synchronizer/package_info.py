# Copyright (c) 2024.  All rights reserved.


MAJOR = 0
MINOR = 0
PATCH = 2
PRE_RELEASE = 'rc0'

# Use the following formatting: (major, minor, patch, pre-release)
VERSION = (MAJOR, MINOR, PATCH, PRE_RELEASE)

__shortversion__ = '.'.join(map(str, VERSION[:3]))
__version__ = '.'.join(map(str, VERSION[:3])) + ''.join(VERSION[3:])

__package_name__ = 'multiprocess-synchronizer'
__contact_names__ = 'Long LI'
__contact_emails__ = 'lilong.albert@gmail.com'
__homepage__ = (
    'https://github.com/sandyhouse/synchronizer'
)
__repository_url__ = 'https://github.com/sandyhouse/synchronizer'
__download_url__ = 'https://github.com/sandyhouse/synchronizer/releases'
__description__ = (
    'A library to synchronize multiple processes in a distributed system.'
)
__license__ = 'Apache 2.0'
__keywords__ = (
    'synchronization', 'distributed', 'multiprocessing'
)
