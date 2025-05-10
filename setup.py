from setuptools import setup, find_packages

setup(
    name='custom-python-logger',
    version='1.0.0',
    packages=find_packages(include=['custom_python_logger', 'custom_python_logger.*']),
    install_requires=[
        'colorlog>=4.0.0',
        'setuptools>=42.0.0',
        'wheel>=0.36.2',
        'colorlog>=6.7.0',
        'pytest>=6.2.4',
        'pathlib>=1.0.1',
    ],
    author='Avi Zaguri',
    author_email='',
    description='A custom logger with color support and additional features.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aviz92/custom-python-logger',
    project_urls={
        'Repository': 'https://github.com/aviz92/custom-python-logger',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
