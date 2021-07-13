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
        if shipper.streetlines: shipperJson['Streetlines'] = shipper.streetlines
        if shipper.streetlines2: shipperJson['Streetlines2'] = shipper.streetlines2
        if shipper.streetlines3: shipperJson['Streetlines3'] = shipper.streetlines3
        if shipper.streetname: shipperJson['Streetname'] = shipper.streetname
        if shipper.city: shipperJson['City'] = shipper.city
        if shipper.citydistrict: shipperJson['CityDistrict'] = shipper.citydistrict
        if shipper.stateorprovincecode: shipperJson['StateOrProvinceCode'] = shipper.stateorprovincecode
        if shipper.postalcode: shipperJson['PostalCode'] = shipper.postalcode
        if shipper.countrycode: shipperJson['CountryCode'] = shipper.countrycode
        data['RateRequest']['RequestedShipment']['Ship']['Shipper'] = shipperJson

        recipientJson = shipJson['Recipient']
        if recipient.streetlines: recipientJson['Streetlines'] = recipient.streetlines
        if recipient.streetlines2: recipientJson['Streetlines2'] = recipient.streetlines2
        if recipient.streetlines3: recipientJson['Streetlines3'] = recipient.streetlines3
        if recipient.streetname: recipientJson['Streetname'] = recipient.streetname
        if recipient.city: recipientJson['City'] = recipient.city
        if recipient.citydistrict: recipientJson['CityDistrict'] = recipient.citydistrict
        if recipient.stateorprovincecode: recipientJson['StateOrProvinceCode'] = recipient.stateorprovincecode
        if recipient.postalcode: recipientJson['PostalCode'] = recipient.postalcode
        if recipient.countrycode: recipientJson['CountryCode'] = recipient.countrycode
        data['RateRequest']['RequestedShipment']['Ship']['Recipient'] = recipientJson

        packageList = data['RateRequest']['RequestedShipment']['Packages']['RequestedPackages']

        count = 1
        for package in packages.requestedpackages.items():

            weightJson = {}
            if package.weight.value: weightJson['Value'] = package.weight.value

            dimensionJson = {}
            print(package.dimensions.length)
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