import cdsapi
from typing import Union, List
class SingleLevelDownloader:
    """
    Descargador de datos ERA5 para variables de superficie (single-level).
    Ejemplo de uso:
        downloader = SingleLevelDownloader()
        downloader.download(
            variables=['2m_temperature'],
            year=2024,
            month=6,
            days=[15, 16],
            area=[10, -80, -10, -60],
            output_file="surface_data.nc")
    """
    def __init__(self):
        self.client = cdsapi.Client()
    def download(
        self,
        variables: List[str],
        year: Union[int, str, List],
        month: Union[int, str, List],
        days: List[int],
        area: List[float],
        output_file: str,
        time: List[str] = None,
        **kwargs
    ):
        """ Descarga datos de superficie desde ERA5.
            Args:
            variables: Lista de variables (ej: ['2m_temperature', '10m_u_component_of_wind']).
            year: Año(s) como entero, string o lista.
            month: Mes(es) como entero, string o lista.
            days: Lista de días del mes.
            area: [Norte, Oeste, Sur, Este] en grados decimales.
            output_file: Nombre del archivo NetCDF de salida.
            times: Lista de horas en formato 'HH:MM'. Si es None, usa todas las horas.
            **kwargs: Parámetros adicionales para el request.
        """
        if time is None: 
            time = [f"{h:02d}:00" for h in range(24)]  # todas horas
        request = {
            'product_type': 'reanalysis',
            'variable': variables,
            'year': year,
            'month': month,
            'day': days,
            'time': time,
            'area': area,
            'format': 'netcdf',
            **kwargs
        }
        self.client.retrieve('reanalysis-era5-single-levels', request, output_file)
