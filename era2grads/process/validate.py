import xarray as xr

class ERA5Validator:
    @staticmethod
    def validate_file(file_path: str) -> bool:
        """Verifica que un archivo NetCDF sea válido."""
        try:
            xr.open_dataset(file_path)
            return True
        except:
            return False
