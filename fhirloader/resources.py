"""
resources.py

"""
payor = {
    "resourceType": "Organization",
    "text": {
        "status": "generated",
        "div": '<div xmlns="http://www.w3.org/1999/xhtml">\n      \n      <p>Unified Insurance Co</p>\n    \n    </div>',
    },
    "identifier": [{"system": "urn:oid:2.16.840.1.113883.3.19.2.3", "value": "666666"}],
    "name": "Unified Insurance Co",
}

provider = {
    "resourceType": "Organization",
    "text": {
        "status": "generated",
        "div": '<div xmlns="http://www.w3.org/1999/xhtml">\n      \n      <p>Downtown Medical Center</p>\n    \n    </div>',
    },
    "identifier": [{"system": "http://hl7.org.fhir/sid/us-npi", "value": "1144221847"}],
    "name": "Downtown Medical Center",
}

patient = {
    "resourceType": "Patient",
    "text": {
        "status": "generated",
        "div": '<div xmlns="http://www.w3.org/1999/xhtml">\n      \n      <p>Patient John Doe, Inc. MR = 654321</p>\n    \n    </div>',
    },
    "identifier": [
        {
            "use": "usual",
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "MR",
                    }
                ]
            },
            "system": "urn:oid:0.1.2.3.4.5.6.7",
            "value": "654321",
        }
    ],
    "active": True,
    "name": [{"use": "official", "family": "Doe", "given": ["John"]}],
    "gender": "male",
    "managingOrganization": {
        "reference": "Organization/001",
        "display": "Unified Insurance Co.",
    },
    "meta": {
        "tag": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActReason",
                "code": "HTEST",
                "display": "test health data",
            }
        ]
    },
}

coverage = {
  "resourceType": "Coverage",
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the coverage</div>"
  },
  "identifier": [
    {
      "system": "http://unifiedinsurance.com/certificate",
      "value": "12345"
    }
  ],
  "status": "active",
  "type": {
    "coding": [
      {
        "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
        "code": "EHCPOL",
        "display": "extended healthcare"
      }
    ]
  },
  "subscriber": {
    "reference": "Patient/17bbc7c35b6-f0b8fdb6-5673-4c01-8f0a-453b07a5d2cd"
  },
  "beneficiary": {
    "reference": "Patient/4"
  },
  "dependent": "0",
  "relationship": {
    "coding": [
      {
        "code": "self"
      }
    ]
  },
  "period": {
    "start": "2021-01-01",
    "end": "2021-12-31"
  },
  "payor": [
    {
      "reference": "Organization/17bbc7d80e4-5d3a2ee8-aab8-4406-bf46-dbf3df9e300c"
    }
  ],
  "class": [
    {
      "type": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/coverage-class",
            "code": "group"
          }
        ]
      },
      "value": "CBI35",
      "name": "Corporate Baker's Inc. Local #35"
    }
  ]
}