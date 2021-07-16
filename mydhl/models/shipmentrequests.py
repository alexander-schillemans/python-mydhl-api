from .base import ObjectListModel, BaseModel

class ShipmentRequest(BaseModel):

    def __init__(self,
        requestedshipment
    ):

        self.requestedshipment = requestedshipment if requestedshipment else RequestedShipment()