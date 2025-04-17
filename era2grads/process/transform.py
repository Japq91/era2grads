import xarray as xr

class ERA5Transformer:
    @staticmethod
    def calculate_wind_speed(u: xr.DataArray, v: xr.DataArray) -> xr.DataArray:
        """Calcula la velocidad del viento (√(u² + v²))."""
        return (u**2 + v**2)**0.5
