from .base import APIEndpoint
from datetime import datetime

from mydhl.models.raterequests import *

class RateRequestMethods(APIEndpoint):

    def __init__(self, api):
        super(RateRequestMethods, self).__init__(api, "RateRequest")
    

    def get(self, 
        shipper, 
        recipient,
        packages,
        clientDetails=None,
        shipTimestamp=None,
        dropOffType=RequestedShipment.REGULAR_PICKUP, 
        unitOfMeasurement=RequestedShipment.MEASUREMENT_SI, 
        content=RequestedShipment.CONTENT_DOCUMENTS,
        paymentInfo=RequestedShipment.PAYMENT_DAP,
        nextBusinessDay='N'
    ):

        if not shipTimestamp: shipTimestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        data = {
            "RateRequest" : {
                "ClientDetails" : clientDetails,
                "RequestedShipment" : {
                    "DropOffType" : dropOffType,
                    "ShipTimestamp" : "{shipTimestamp} GMT+02:00".format(shipTimestamp=shipTimestamp),
                    "UnitOfMeasurement" : unitOfMeasurement,
                    "Content" : content,
                    "PaymentInfo" : paymentInfo,
                    "NextBusinessDay" : nextBusinessDay,
                    "Account" : self.api.account,
                    'Ship' : {
                        'Shipper' : {},
                        'Recipient' : {}
                    },
                    'Packages' : {
                        'RequestedPackages' : []
                    }
                }
            }
        }

        shipJson = data['RateRequest']['RequestedShipment']['Ship']

        shipperJson = shipJson['Shipper']
        if shipper.streetLines: shipperJson['Streetlines'] = shipper.streetLines
        if shipper.streetLines2: shipperJson['Streetlines2'] = shipper.streetLines2
        if shipper.streetLines3: shipperJson['Streetlines3'] = shipper.streetLines3
        if shipper.streetName: shipperJson['Streetname'] = shipper.streetName
        if shipper.city: shipperJson['City'] = shipper.city
        if shipper.cityDistrict: shipperJson['CityDistrict'] = shipper.cityDistrict
        if shipper.stateOrProvinceCode: shipperJson['StateOrProvinceCode'] = shipper.stateOrProvinceCode
        if shipper.postalCode: shipperJson['PostalCode'] = shipper.postalCode
        if shipper.countryCode: shipperJson['CountryCode'] = shipper.countryCode
        data['RateRequest']['RequestedShipment']['Ship']['Shipper'] = shipperJson

        recipientJson = shipJson['Recipient']
        if recipient.streetLines: recipientJson['Streetlines'] = recipient.streetLines
        if recipient.streetLines2: recipientJson['Streetlines2'] = recipient.streetLines2
        if recipient.streetLines3: recipientJson['Streetlines3'] = recipient.streetLines3
        if recipient.streetName: recipientJson['Streetname'] = recipient.streetName
        if recipient.city: recipientJson['City'] = recipient.city
        if recipient.cityDistrict: recipientJson['CityDistrict'] = recipient.cityDistrict
        if recipient.stateOrProvinceCode: recipientJson['StateOrProvinceCode'] = recipient.stateOrProvinceCode
        if recipient.postalCode: recipientJson['PostalCode'] = recipient.postalCode
        if recipient.countryCode: recipientJson['CountryCode'] = recipient.countryCode
        data['RateRequest']['RequestedShipment']['Ship']['Recipient'] = recipientJson

        packageList = data['RateRequest']['RequestedShipment']['Packages']['RequestedPackages']

        count = 1
        for package in packages.requestedPackages.items():

            weightJson = {}
            if package.weight.value: weightJson['Value'] = package.weight.value

            dimensionJson = {}
            if package.dimensions.length: dimensionJson['Length'] = package.dimensions.length
            if package.dimensions.width: dimensionJson['Width'] = package.dimensions.width
            if package.dimensions.height: dimensionJson['Height'] = package.dimensions.height

            packageList.append({
                '@number' : count,
                'Weight' : weightJson,
                'Dimensions' : dimensionJson
            })

            count += 1
        
        data['RateRequest']['RequestedShipment']['Packages']['RequestedPackages'] = packageList

        url = self.endpoint

        status, headers, respJson = self.api.post(url, data)
        return RateResponse().parse(respJson['RateResponse'])