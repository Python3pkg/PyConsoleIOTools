from setuptools import setup, find_packages

setup(
    name='consoleiotools',
    version='1.2.0',
    description='Some console tools for inputs and outputs',
    long_description='Some console tools for inputs and outputs, by Kyan',
    url='https://github.com/kyan001/PyConsoleIOTools',
    author='Kai Yan',
    author_email='kai@superfarmer.net',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: User Interfaces',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='console input output tool',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    py_modules=["consoleiotools"],
    install_requires=[],
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
)
