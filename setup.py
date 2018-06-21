from setuptools import setup, find_packages

setup(
    name='doc_reviewer',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
        'click',
    ],
    extras_require={
        'testing': [
            'pytest',
            'pytest-mock',
        ],
    },
    author='James Collins',
    author_email='collijk@uw.edu',
)
