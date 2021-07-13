from .base import APIEndpoint

from mydhl.models.raterequests import *

class RateRequestMethods(APIEndpoint):

    def __init__(self, api):
        super(RateRequestMethods, self).__init__(api, "RateRequest")
    
    def testMockData(self):

        data = {
            "RateRequest" : {
                "ClientDetails" : None,
                "RequestedShipment" : {
                "DropOffType" : "REGULAR_PICKUP",
                "ShipTimestamp" : "2021-07-13T14:00:00 GMT+02:00",
                "UnitOfMeasurement" : "SI",
                "Content" : "DOCUMENTS",
                "PaymentInfo" : "DAP",
                "NextBusinessDay" : "Y",
                "Account" : self.api.account,
                "Ship" : {
                    "Shipper" : {
                    "City" : "Woluwelaan 151",
                    "PostalCode" : 1831,
                    "CountryCode" : "BE"
                    },
                    "Recipient" : {
                    "City" : "Leuven",
                    "PostalCode" : "3000",
                    "CountryCode" : "BE"
                    }
                },
                "Packages" : {
                    "RequestedPackages" : {
                    "@number" : "1",
                    "Weight" : {
                        "Value" : 2
                    },
                    "Dimensions" : {
                        "Length" : 20,
                        "Width" : 20,
                        "Height" : 30
                    }
                    }
                }
                }
            }
        }

        url = self.endpoint

        status, headers, respJson = self.api.post(url, data)
        return RateResponse().parse(respJson['RateResponse'])