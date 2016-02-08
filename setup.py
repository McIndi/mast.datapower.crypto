import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), "rb")as fin:
        return fin.read()

setup(
    name="mast.datapower.crypto",
    version="2.1.0",
    author="Clifford Bressette",
    author_email="cliffordbressette@mcindi.com",
    description=(
        "A utility to help manage crypto artifacts for IBM DataPower"),
    license="GPLv3",
    keywords="DataPower crypto certificate cert key pki tls",
    url="http://github.com/mcindi/mast.datapower.crypto",
    namespace_packages=["mast", "mast.datapower"],
    packages=['mast', 'mast.datapower', 'mast.datapower.crypto'],
    entry_points={
        'mast_web_plugin': [
            'crypto = mast.datapower.crypto:WebPlugin'
        ]
    },
    package_data={
        "mast.datapower.crypto": ["docroot/*"]
    },
    incude_package_data=True,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPLv3",
    ],
)
