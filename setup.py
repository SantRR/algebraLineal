import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
VERSION = "0.0.1"
PACKAGE_NAME = "paquete_ibero_al_SRR_EIGO"
AUTHOR = "Santiago Romo Rubio, Edgar Iván Gálvez Ortega"
AUTHOR_EMAIL = "192172-7@iberoleon.edu.mx, 180235-A@iberoleon.edu.mx"
URL = "https://github.com/0mudkip/repo_paquete_ibero_al"

LICENSE = "MIT"
DESCRIPTION = "Librería para realizar funciones simple de álgebra lineal"
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    "numpy"
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
