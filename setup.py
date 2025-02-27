#!/usr/bin/env python
"""Cloudflare API code - setup.py file"""
import re
from setuptools import setup, find_packages

_version_re = re.compile(r"__version__\s=\s'(.*)'")


def main():
    """Cloudflare API code - setup.py file"""

    with open('README.md') as read_me:
        long_description = read_me.read()

    with open('CloudFlare/__init__.py', 'r') as f:
        version = _version_re.search(f.read()).group(1)

    setup(
        name='cloudflare',
        version=version,
        description='Python wrapper for the Cloudflare v4 API',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Martin J. Levy',
        author_email='mahtin@mahtin.com',
        url='https://github.com/cloudflare/python-cloudflare',
        license='MIT',
        options={"bdist_wheel": {"universal": True}},
        packages=['cli4', 'examples']+find_packages(),
        include_package_data=True,
        data_files = [('share/man/man1', ['cli4/cli4.1'])],
        install_requires=['requests', 'pyyaml', 'jsonlines', 'beautifulsoup4'],
        keywords='cloudflare',
        entry_points={
            'console_scripts': [
                'cli4=cli4.__main__:main'
            ]
        },
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3'
        ]
    )

if __name__ == '__main__':
    main()
