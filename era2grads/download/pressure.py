import cdsapi
from typing import Union, List
class PressureLevelDownloader:
    """Descarga datos ERA5 para niveles de presión. Versión simple y autónoma."""
    def __init__(self): 
        self.client = cdsapi.Client()
    def download(
        self,
        variables: List[str],
        year: Union[int, str, List],
        month: Union[int, str, List],
        days: List[int],
        pressure_levels: List[int],
        area: List[float],
        output_file: str,
        time: List[str] = None,
        **kwargs):
        """ Args:
            variables: Lista de variables (ej: ['u_component_of_wind', 'temperature'])
            years: Lista de años (ej: [2020, 2021] o ['2020'])
            months: Lista de meses (1-12)
            days: Lista de días (1-31)
            pressure_levels: Lista de niveles en hPa (ej: [500, 850])
            area: [Norte, Oeste, Sur, Este] (ej: [10, -80, -10, -60])
            output_file: Nombre del archivo de salida (ej: 'datos.nc')
        """
        if time is None: 
            time = [f"{h:02d}:00" for h in range(24)]  # todas horas
        request = {
            'product_type': 'reanalysis',
            'variable': variables,
            'year': year,
            'month': month,
            'day': days,
            'time': time,  # Todas las horas
            'pressure_level': pressure_levels,
            'area': area,
            'format': 'netcdf',
            **kwargs
        }
        self.client.retrieve('reanalysis-era5-pressure-levels', request, output_file)
