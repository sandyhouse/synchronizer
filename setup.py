"""Setup for pip package."""

import importlib.util

import setuptools
from setuptools import Extension

spec = importlib.util.spec_from_file_location('package_info', 'synchronizer/package_info.py')
package_info = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package_info)


__contact_emails__ = package_info.__contact_emails__
__contact_names__ = package_info.__contact_names__
__description__ = package_info.__description__
__download_url__ = package_info.__download_url__
__homepage__ = package_info.__homepage__
__keywords__ = package_info.__keywords__
__license__ = package_info.__license__
__package_name__ = package_info.__package_name__
__repository_url__ = package_info.__repository_url__
__version__ = package_info.__version__


with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
long_description_content_type = "text/markdown"


setuptools.setup(
    name=__package_name__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url=__repository_url__,
    download_url=__download_url__,
    author=__contact_names__,
    author_email=__contact_emails__,
    maintainer=__contact_names__,
    maintainer_email=__contact_emails__,
    license=__license__,
    classifiers=[
        # How mature is this project? Common values are
        #  1 - Planning
        #  2 - Pre-Alpha
        #  3 - Alpha
        #  4 - Beta
        #  5 - Production/Stable
        #  6 - Mature
        #  7 - Inactive
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        # Indicate what your project relates to
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',
        # Supported python versions
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        # Additional Setting
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_namespace_packages(include=["synchronizer"]),
    # Add in any packaged data.
    include_package_data=True,
    # PyPI package information.
    keywords=__keywords__,
    entry_points={
        'console_scripts': [
            'synchronizer=synchronizer.cli:main',
        ],
    },
)
