from setuptools import setup, find_packages

try:
    from unittest import mock
except ImportError:
    has_mock = False
else:
    has_mock = True

setup(
    name="AppMetrics",
    version="0.4.2",

    packages=find_packages(),

    scripts=[],

    install_requires=[],
    extras_require={
        'test': ['nose==1.3.0'] + ['mock==1.0.1'] if has_mock else [],
        'dev': ['coverage==3.7.1', 'ipython==1.1.0', 'python-coveralls==2.4.2'],
        'werkzeug': ['werkzeug']
    },

    package_data={},

    # metadata for upload to PyPI
    author="Antonio Valente",
    author_email="y3sman@gmail.com",
    description="Application metrics collector",
    license="Apache 2.0",
    keywords=["metrics", "folsom", "histogram", "metric", "monitor"],
    url="https://github.com/avalente/appmetrics",
    platforms='Platform Independent',

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: System :: Monitoring",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ]
)
