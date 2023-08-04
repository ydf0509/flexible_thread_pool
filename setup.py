# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='flexible_thread_pool',  #
    version='0.1',
    description=(
        'flexible_thread_pool ，auto expand thread and reduce threads. both support sync and asyncio,fast than concurrent.futures.ThreadpoolExecutor'
    ),
    # long_description=open('README.md', 'r',encoding='utf8').read(),
    keywords=['thread pool','async','asyncio'],
    long_description_content_type="text/markdown",
    long_description=open('README.md', 'r', encoding='utf8').read(),
    author='bfzs',
    author_email='ydf0509@sohu.com',
    maintainer='ydf',
    maintainer_email='ydf0509@sohu.com',
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    platforms=["all"],
    url='https://github.com/ydf0509/flexible_thread_pool',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'nb_log',
    ],
    extras_require={},
)

"""

python setup.py sdist & python -m  twine upload dist/flexible_thread_pool-0.1.tar.gz




"""
