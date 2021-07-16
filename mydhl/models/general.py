from .base import ObjectListModel, BaseModel

class ClientDetail(BaseModel):

    def __init__(self,
        so=None,
        plant=None
    ):

        self.so = so
        self.plant = plant

class Request(BaseModel):

    def __init__(self,
        serviceheader=None
    ):

        self.serviceheader = serviceheader if serviceheader else ServiceHeader()

class ServiceHeader(BaseModel):

    def __init__(self,
        messagetime=None,
        messagereference=None,
        webstoreplatform=None,
        webstoreplatformversion=None,
        shippingsystemplatform=None,
        shippingsystemplatformversion=None,
        plugin=None,
        pluginversion=None
    ):

        self.messagetime = messagetime
        self.messagereference = messagereference
        self.webstoreplatform = webstoreplatform
        self.webstoreplatformversion = webstoreplatformversion
        self.shippingsystemplatform = shippingsystemplatform
        self.shippingsystemplatformversion = shippingsystemplatformversion
        self.plugin = plugin
        self.pluginversion = pluginversion