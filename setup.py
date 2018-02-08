from setuptools import setup

with open('README.md') as readme:
    readme = readme.read()

setup(
    name='sslwireless_sms',
    packages=['sslwireless_sms'],
    version='0.0.2',
    description='A simple python wrapper for sslwireless sms api.',
    long_description=readme,
    author='Rahul Haque',
    author_email='rahulhaque07@gmail.com',
    install_requires=[
        'requests',
        'xmltodict'
    ],
    license='MIT',
    url='https://github.com/rahulhaque/sslwireless-sms-wrapper-python',
    download_url='https://github.com/rahulhaque/sslwireless-sms-wrapper-python/archive/v0.0.1.tar.gz',
    keywords=['python', 'sslwireless', 'sms', 'api-wrapper'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
