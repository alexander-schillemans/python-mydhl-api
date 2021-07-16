from .base import ObjectListModel, BaseModel
from .general import Address, ClientDetail, Dimensions, Request, Billing, DocumentImages, CustomerBarcode, CustomerLogo, Weight, Dimensions

class ShipmentRequest(BaseModel):

    def __init__(self,
        messageId=None,
        clientDetail=None,
        request=None,
        requestedShipment=None
    ):

        self.messageId = messageId
        self.clientDetail = clientDetail if clientDetail else ClientDetail()
        self.request = request if request else Request()
        self.requestedShipment = requestedShipment if requestedShipment else RequestedShipment()

class RequestedShipment(BaseModel):

    def __init__(self,
        shipmentInfo=None,
        shipTimestamp=None,
        pickupLocationCloseTime=None,
        specialPickupInstruction=None,
        pickupLocation=None,
        paymentInfo=None,
        internationalDetail=None,
        onDemandDeliveryOptions=None,
        ondemandDeliveryURLRequest=None,
        ship=None,
        packages=None,
        dangerousGoods=None,
        getRateEstimates=None,
        shipmentNotifications=None
    ):

        self.shipmentInfo = shipmentInfo if shipmentInfo else ShipmentInfo()
        self.shipTimestamp = shipTimestamp
        self.pickupLocationCloseTime = pickupLocationCloseTime
        self.specialPickupInstruction = specialPickupInstruction
        self.pickupLocation = pickupLocation
        self.paymentInfo = paymentInfo
        self.internationalDetail = internationalDetail if internationalDetail else InternationalDetail()
        self.onDemandDeliveryOptions = onDemandDeliveryOptions if onDemandDeliveryOptions else OnDemandDeliveryOptions()
        self.onDemandDeliveryURLRequest = ondemandDeliveryURLRequest
        self.ship = ship if ship else Ship()
        self.packages = packages if packages else ShipmentPackages()
        self.dangerousGoods = dangerousGoods if dangerousGoods else DangerousGoods()
        self.getRateEstimates = getRateEstimates
        self.shipmentNotifications = shipmentNotifications if shipmentNotifications else ShipmentNotifications()

class ShipmentNotifications(ObjectListModel):

    def __init__(self):
        super(ShipmentNotifications, self).__init__(list=[], listObject=ShipmentNotification)

class ShipmentNotification(BaseModel):

    def __init__(self,
        notificationMethod=None,
        emailAddress=None,
        mobilePhoneNumber=None,
        bespokeMessage=None,
        languageCode=None,
        languageCountryCode=None
    ):

        self.notificationMethod = notificationMethod
        self.emailAddress = emailAddress
        self.mobilePhoneNumber = mobilePhoneNumber
        self.bespokeMessage = bespokeMessage
        self.languageCode = languageCode
        self.languageCountryCode = languageCountryCode

class Ship(BaseModel):

    def __init__(self,
        shipper=None,
        pickup=None,
        bookingRequestor=None,
        buyer=None,
        recipient=None
    ):

        self.shipper = shipper if shipper else PersonalInfo()
        self.pickup = pickup if pickup else PersonalInfo()
        self.bookingRequestor = bookingRequestor if bookingRequestor else PersonalInfo()
        self.buyer = buyer if buyer else PersonalInfo()
        self.recipient = recipient if recipient else PersonalInfo()

class PersonalInfo(BaseModel):
    
    def __init__(self,
        contact=None,
        address=None,
        registrationNumbers=None,
        bankDetail=None
    ):

        self.contact = contact if contact else Contact()
        self.address = address if address else Address()
        self.registrationNumbers = registrationNumbers if registrationNumbers else RegistrationNumbers()
        self.bankDetail = bankDetail if bankDetail else BankDetail()

class BankDetail(BaseModel):

    def __init__(self,
        bankName=None
    ):

        self.bankName = bankName

class RegistrationNumbers(ObjectListModel):

    def __init__(self):
        super(RegistrationNumbers, self).__init__(list=[], listObject=RegistrationNumber)

class RegistrationNumber(BaseModel):

    def __init__(self,
        number=None,
        numberTypeCode=None,
        numberIssuerCountryCode=None
    ):

        self.number = number
        self.numberTypeCode = numberTypeCode
        self.numberIssuerCountryCode = numberIssuerCountryCode

class Contact(BaseModel):

    def __init__(self,
        personName=None,
        companyName=None,
        phoneNumber=None,
        emailAddress=None,
        mobilePhoneNumber=None
    ):

        self.personName = personName
        self.companyName = companyName
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.mobilePhoneNumber = mobilePhoneNumber

class OnDemandDeliveryOptions(BaseModel):

    def __init__(self,
        deliveryOption=None,
        location=None,
        instructions=None,
        gateCode=None,
        LWNTypeCode=None,
        neighbourName=None,
        neighbourHouseNumber=None,
        authorizerName=None,
        selectedServicePointID=None,
        requestedDeliveryDate=None
    ):

        self.deliveryOption = deliveryOption
        self.location = location
        self.instructions = instructions
        self.gateCode = gateCode
        self.LWNTypeCode = LWNTypeCode
        self.neighbourName = neighbourName
        self.neighbourHouseNumber = neighbourHouseNumber
        self.authorizerName = authorizerName
        self.selectedServicePointID = selectedServicePointID
        self.requestedDeliveryDate = requestedDeliveryDate

class InternationalDetail(BaseModel):

    def __init__(self,
        commodities=None,
        content=None,
        exportDeclaration=None
    ):

        self.commodities = commodities
        self.content = content
        self.exportDeclaration = exportDeclaration if exportDeclaration else ExportDeclaration()

class ExportDeclaration(BaseModel):

    def __init__(self,
        destinationPort=None,
        exporterCode=None,
        exporterID=None,
        exportLicense=None,
        exportLineItems=None,
        exportReason=None,
        importLicense=None,
        invoiceDate=None,
        invoiceNumber=None,
        invoiceDeclarationTexts=None,
        invoiceSignatureDetails=None,
        otherCharges=None,
        packageMarks=None,
        payerGSTVAT=None,
        recipientReference=None,
        remarks=None,
        termsOfPayment=None
    ):

        self.destinationPort = destinationPort
        self.exporterCode = exporterCode
        self.exporterID = exporterID
        self.exportLicense = exportLicense
        self.exportLineItems = exportLineItems
        self.exportReason = exportReason
        self.importLicense = importLicense
        self.invoiceDate = invoiceDate
        self.invoiceNumber = invoiceNumber
        self.invoiceDeclarationTexts = invoiceDeclarationTexts
        self.invoiceSignatureDetails = invoiceSignatureDetails
        self.otherCharges = otherCharges
        self.packageMarks = packageMarks
        self.payerGSTVAT = payerGSTVAT
        self.recipientReference = recipientReference
        self.remarks = remarks
        self.termsOfPayment = termsOfPayment

class ShipmentInfo(BaseModel):

    def __init__(self,
        dropOffType=None,
        rateRequestConfirmed=None,
        serviceType=None,
        localServiceType=None,
        account=None,
        billing=None,
        specialServices=None,
        currency=None,
        unitOfMeasurement=None,
        shipmentIdentificationNumber=None,
        useOwnShipmentIdentificationNumber=None,
        packagesCount=None,
        sendPackage=None,
        labelType=None,
        labelTemplate=None,
        archiveLabelTemplate=None,
        customsInvoiceTemplate=None,
        shipmentReceiptTemplate=None,
        paperlessTradeEnabled=None,
        paperlessTradeImage=None,
        documentImages=None,
        labelOptions=None,
        shipmentReferences=None,
        parentShipmentIdentificationNumber=None,
        requestTransliterateResponse=None,
        requestAdditionalInformation=None,
        requestEstimatedDeliveryDate=None,
        estimatedDeliveryDateType=None,
        requestPickupDetails=None
    ):

        self.dropOffType = dropOffType
        self.rateRequestConfirmed = rateRequestConfirmed
        self.serviceType = serviceType
        self.localServiceType = localServiceType
        self.account = account
        self.billing = billing if billing else ShipmentBilling()
        self.specialServices = specialServices if specialServices else SpecialServices()
        self.currency = currency
        self.unitOfMeasurement = unitOfMeasurement
        self.shipmentIdentificationNumber = shipmentIdentificationNumber
        self.useOwnShipmentIdentificationNumber = useOwnShipmentIdentificationNumber
        self.packagesCount = packagesCount
        self.sendPackage = sendPackage
        self.labelType = labelType
        self.labelTemplate = labelTemplate
        self.archiveLabelTemplate = archiveLabelTemplate
        self.customsInvoiceTemplate = customsInvoiceTemplate
        self.shipmentReceiptTemplate = shipmentReceiptTemplate
        self.paperlessTradeEnabled = paperlessTradeEnabled
        self.paperlessTradeImage = paperlessTradeImage
        self.documentImages = documentImages if documentImages else DocumentImages()
        self.labelOptions = labelOptions if labelOptions else LabelOptions()
        self.shipmentReferences = shipmentReferences if shipmentReferences else ShipmentReferences()
        self.parentShipmentIdentificationNumber = parentShipmentIdentificationNumber
        self.requestTransliterateResponse = requestTransliterateResponse
        self.requestAdditionalInformation = requestAdditionalInformation
        self.requestEstimatedDeliveryDate = requestEstimatedDeliveryDate
        self.estimatedDeliveryDateType = estimatedDeliveryDateType
        self.requestPickupDetails = requestPickupDetails

class ShipmentBilling(Billing):

    def __init__(self,
        shipperAccountNumber=None,
        shippingPaymentType=None,
        billingAccountNumber=None,
        dutyAndTaxPayerAccountNumber=None,
        shipmentPrepaidTotalCharge=None,
        neverOverrideBillingService=None
    ):

        super().__init__(shipperAccountNumber, shippingPaymentType, billingAccountNumber)
        self.dutyAndTaxPayerAccountNumber = dutyAndTaxPayerAccountNumber
        self.shipmentPrepaidTotalCharge = shipmentPrepaidTotalCharge if shipmentPrepaidTotalCharge else ShipmentPrepaidTotalCharge()
        self.neverOverrideBillingService = neverOverrideBillingService

class ShipmentPrepaidTotalCharge(BaseModel):

    def __init__(self,
        currencyCode=None,
        amount=None,
        paymentMethod=None
    ):

        self.currencyCode = currencyCode
        self.amount = amount
        self.paymentMethod = paymentMethod

class SpecialServices(ObjectListModel):

    def __init__(self):
        super(SpecialServices, self).__init__(list=[], listObject=SpecialService)

class SpecialService(BaseModel):

    def __init__(self,
        serviceType=None,
        serviceValue=None,
        currencyCode=None,
        paymentCode=None,
        startDate=None,
        endDate=None,
        textInstruction=None
    ):

        self.serviceType = serviceType
        self.serviceValue = serviceValue
        self.currencyCode = currencyCode
        self.paymentCode = paymentCode
        self.startDate = startDate
        self.endDate = endDate
        self.textInstruction = textInstruction


class LabelOptions(BaseModel):
    
    def __init__(self,
        customerLogo=None,
        customerBarcode=None,
        printerDPI=None,
        requestWaybillDocument=None,
        hideAccountInWaybillDocument=None,
        numberOfWaybillDocumentCopies=None,
        requestDHLCustomsInvoice=None,
        DHLCustomsInvoiceLanguageCode=None,
        DHLCustomsInvoiceLanguageCountryCode=None,
        DHLCustomsInvoiceType=None,
        requestShipmentReceipt=None,
        detachOptions=None,
        requestBarcodeInfo=None,
        labelRegText=None,
        custData=None,
        requestLabelsToFitA4=None,
        requestDHLLogoOnLabel=None
    ):

        self.customerLogo = customerLogo if customerLogo else CustomerLogo()
        self.customerBarcode = customerBarcode if customerBarcode else CustomerBarcode()
        self.printerDPI = printerDPI
        self.requestWaybillDocument = requestWaybillDocument
        self.hideAccountInWaybillDocument = hideAccountInWaybillDocument
        self.numberOfWaybillDocumentCopies = numberOfWaybillDocumentCopies
        self.requestDHLCustomsInvoice = requestDHLCustomsInvoice
        self.DHLCustomsInvoiceLanguageCode = DHLCustomsInvoiceLanguageCode
        self.DHLCustomsInvoiceLanguageCountryCode = DHLCustomsInvoiceLanguageCountryCode
        self.DHLCustomsInvoiceType = DHLCustomsInvoiceType
        self.requestShipmentReceipt = requestShipmentReceipt
        self.detachOptions = detachOptions if detachOptions else DetachOptions()
        self.requestBarcodeInfo = requestBarcodeInfo
        self.labelRegText = labelRegText
        self.custData = custData
        self.requestLabelsToFitA4 = requestLabelsToFitA4
        self.requestDHLLogoOnLabel = requestDHLLogoOnLabel

class DetachOptions(BaseModel):

    def __init__(self,
        allInOnePDF=None,
        splitShipmentReceiptAndCustomsInvoice=None,
        splitTransportLabelAndWaybillDocument=None,
        splitLabelsByPieces=None,
        shipmentReceiptWithLabels=None
    ):

        self.allInOnePDF = allInOnePDF
        self.splitShipmentReceiptAndCustomsInvoice = splitShipmentReceiptAndCustomsInvoice
        self.splitTransportLabelAndWaybillDocument = splitTransportLabelAndWaybillDocument
        self.splitLabelsByPieces = splitLabelsByPieces
        self.shipmentReceiptWithLabels = shipmentReceiptWithLabels

class ShipmentReferences(ObjectListModel):

    def __init__(self):
        super(ShipmentReferences, self).__init__(list=[], listObject=ShipmentReference)

class ShipmentReference(BaseModel):

    def __init__(self,
        shipmentReference=None,
        shipmentReferenceType=None
    ):

        self.shipmentReference = shipmentReference
        self.shipmentReferenceType = shipmentReferenceType

class ShipmentPackages(ObjectListModel):

    def __init__(self):
        super(ShipmentPackages, self).__init__(list=[], listObject=ShipmentPackage)

class ShipmentPackage(BaseModel):

    def __init__(self,
       weight=None,
       dimensions=None,
       pieceIdentificationNumber=None,
       packageContentDescription=None,
       customerReferences=None,
       parentPieceIdentificationNumber=None,
       packageReferences=None
    ):

        self.weight = weight if weight else Weight()
        self.dimensions = dimensions if dimensions else Dimensions()
        self.pieceIdentificationNumber = pieceIdentificationNumber
        self.packageContentDescription = packageContentDescription
        self.customerReferences = customerReferences
        self.parentPieceIdentificationNumber = parentPieceIdentificationNumber
        self.packageReferences = packageReferences if packageReferences else PackageReferences()

class PackageReferences(ObjectListModel):

    def __init__(self):
        super(PackageReferences, self).__init__(list=[], listObject=PackageReference)
    
class PackageReference(BaseModel):

    def __init__(self,
        packageReference=None,
        packageReferenceType=None
    ):

        self.packageReference = packageReference
        self.packageReferenceType = packageReferenceType

class DangerousGoods(ObjectListModel):

    def __init__(self):
        super(DangerousGoods, self).__init__(list=[], listObject=Content)

class Content(BaseModel):

    def __init__(self,
        contentID=None,
        dryIceTotalNetWeight=None,
        UNCode=None
    ):

        self.contentID = contentID
        self.dryIceTotalNetWeight = dryIceTotalNetWeight
        self.UNCode = UNCode