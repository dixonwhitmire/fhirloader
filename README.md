# fhirloader
A simple FHIR data load utility for a specific group of coverage related resources

## Usage

```shell
user@mbp fhirloader % pipenv run cli --help
usage: fhirloader [-h] [-u USERNAME] [-p PASSWORD] [-v] url

The fhirloader CLI loads coverage related resources into a target FHIR Server

positional arguments:
  url                   FHIR Server base url

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Basic Auth Username
  -p PASSWORD, --password PASSWORD
                        Basic Auth Username
  -v, --verify          Enable SSL Verification

```
