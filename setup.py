from setuptools import setup, find_packages

setup(
    name='imhotep_jshint',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/justinabrahms/imhotep_jshint',
    license='MIT',
    author='Justin Abrahms',
    author_email='justin@abrah.ms',
    description='An imhotep plugin for jshint validation',
    entry_points={
        'imhotep_linters': [
            '.js = imhotep_jshint.plugin:JSHint'
        ],
    },
)
