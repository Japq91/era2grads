import cdsapi
from abc import ABC, abstractmethod

class ERA5DownloaderBase(ABC):
    def __init__(self):
        self.client = cdsapi.Client()
    
    @abstractmethod
    def download(self, *args, **kwargs):
        """Método abstracto para implementar en clases hijas."""
        pass

    def _build_request(self, **params):
        """Construye el request común para ERA5."""
        return {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            **params
        }
