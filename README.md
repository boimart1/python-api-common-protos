
# Google APIs common protos

[![pypi](https://img.shields.io/pypi/v/googleapis-common-protos.svg)](https://pypi.org/project/googleapis-common-protos/)


googleapis-common-protos contains the python classes generated from the common
protos in the [googleapis/api-common-protos](https://github.com/googleapis/api-common-protos) repository.

## How to manually update the Optel package on Artifactory

1. Setup or activate your virtual environment:
   1. If you do not already have virtualenv globally installed, run: `py -3 -m pip install virtualenv`
   2. Create the virtual environment: `py -3 -m virtualenv env`
   3. Activate the virtual environment: `env\Scripts\activate.bat`
   4. Install some requirements: `pip install nox setuptools twine`
2. Update the version in setup.py.
3. Generate the protos: `nox -s generate_protos`
4. Fix the formatting: `nox -s blacken`
5. Commit the newly-generated files.
6. If `dist/` already exists, delete it: `rmdir /S /Q dist`
7. Generate the package wheel: `setup.py bdist_wheel`
8. Push the package to Artifactory: `twine upload --repository-url https://artifactory.dev.optelgroup.com/artifactory/api/pypi/ds-pypi-dev-local dist/* -u <ARTIFACTORY_USERNAME> -p <ARTIFACTORY_PASSWORD>`, where `<ARTIFACTORY_USERNAME>` and `<ARTIFACTORY_PASSWORD>` are your credentials.