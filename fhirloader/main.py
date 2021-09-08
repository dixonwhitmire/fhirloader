"""
main.py
"""
import argparse
import client
import logging

CLI_DESCRIPTION = """
The fhirloader CLI loads coverage related resources into a target FHIR Server
"""


def _create_arg_parser():
    """
    Creates the Argument Parser for the CLI utility.
    :return: ArgumentParser
    """

    parser = argparse.ArgumentParser(
        prog="fhirloader",
        description=CLI_DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "url",
        metavar="url",
        type=str,
        default="https://localhost:9443/fhir-server/api/v4",
        help="FHIR Server base url",
    )
    parser.add_argument("-u", "--username", help="Basic Auth Username")
    parser.add_argument("-p", "--password", help="Basic Auth Username")
    parser.add_argument("-v", "--verify", help="Enable SSL Verification", action="store_true")

    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO
    )

    args = _create_arg_parser()
    logging.info("starting fhir loader")
    verify = args.verify or False
    client.load_resources(args.url, args.username, args.password, verify)
    logging.info("fhir loader complete")
