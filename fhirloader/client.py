"""
client.py
"""
import logging
import requests
from requests.auth import HTTPBasicAuth
from resources import payor, provider, patient, coverage
from functools import partial
from typing import Optional, Callable, Dict

logger = logging.getLogger(__name__)

requests.packages.urllib3.disable_warnings()


def _load_resource(
    search_func: Callable,
    post_func: Callable,
    fhir_url: str,
    resource_name: str,
    data: Dict,
) -> str:

    # search for an existing resource
    search_term = {}
    if resource_name == "Organization":
        search_term = {"name": data["name"]}
    elif resource_name == "Patient":
        family_name = data["name"][0]["family"]
        given_name = data["name"][0]["given"][0]
        search_term = {"name": [family_name, given_name]}

    response = search_func(f"{fhir_url}/{resource_name}", params=search_term)
    response.raise_for_status()
    response_doc = response.json()

    total_hits = response_doc.get("total", 0)
    logger.debug(f"search on {search_term} found {total_hits} results")

    if total_hits > 0:
        entry = response_doc.get("entry", [{}])[0]
        resource_id = entry.get("resource", {}).get("id")
        return resource_id

    logger.debug(f"Creating new {resource_name}")
    response = post_func(f"{fhir_url}/{resource_name}", json=data)
    response.raise_for_status()
    response_doc = response.json()
    return response_doc.get("id")


def load_resources(fhir_url: str, username: str = None, password: str = None, verify: bool = True):
    """
    Loads resources into a target FHIR server
    :param fhir_url: The fhir server base url
    :param username: The fhir server username for basic auth (Optional)
    :param password: The fhir server password for basic auth (Optional)
    :param verify: If set to True, enables SSL certificate validation (Optional). Defaults to True
    :return:
    """
    logging.info("fhirloader parameters:")
    logging.info(f"fhir_url: {fhir_url}")
    logging.info(f"username is {'set' if username else 'not set'}")
    logging.info(f"password is {'set' if password else 'not set'}")
    logging.info(f"verify is {'enabled' if verify else 'disabled'}")

    if username and password:
        basic_auth: Optional[HTTPBasicAuth] = HTTPBasicAuth(username, password)
    else:
        basic_auth = None

    wrapped_search = partial(
        requests.get,
        auth=basic_auth,
        headers={
            "content-type": "application/json",
            "accept": "application/json",
        },
        verify=verify,
    )

    wrapped_post = partial(
        requests.post,
        auth=basic_auth,
        headers={
            "content-type": "application/json",
            "accept": "application/json",
            "prefer": "return=representation",
        },
        verify=verify,
    )

    payor_id: str = _load_resource(
        wrapped_search,
        wrapped_post,
        fhir_url,
        "Organization",
        payor,
    )
    logging.info(f"Payor ID {payor_id}")

    provider_id: str = _load_resource(
        wrapped_search,
        wrapped_post,
        fhir_url,
        "Organization",
        provider,
    )
    logging.info(f"Provider ID {provider_id}")

    patient["managingOrganization"]["reference"] = f"Organization/{payor_id}"
    patient_id: str = _load_resource(
        wrapped_search,
        wrapped_post,
        fhir_url,
        "Patient",
        patient,
    )
    logging.info(f"Patient ID {patient_id}")

    coverage["subscriber"]["reference"] = f"Patient/{patient_id}"
    coverage["beneficiary"]["reference"] = f"Patient/{patient_id}"
    coverage["payor"][0]["reference"] = f"Organization/{payor_id}"
    coverage_id: str = _load_resource(
        wrapped_search,
        wrapped_post,
        fhir_url,
        "Coverage",
        coverage,
    )
    logging.info(f"Coverage ID {coverage_id}")

