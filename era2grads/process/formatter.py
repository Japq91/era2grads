import xarray as xr
import os
import logging
from typing import Optional, Dict

class NCDFormatter:
    """
    Clase para optimizar archivos NetCDF para GrADS usando CDO como paso final.

    Ejemplo:
        NCDFormatter.grads_optimize(
            input_file="datos.nc",
            output_file="datos_opt.nc",
            rename_dict={'pressure_level': 'level'}
        )
    """

    @staticmethod
    def grads_optimize(
        input_file: str,
        output_file: Optional[str] = None,
        rename_dict: Optional[Dict[str, str]] = None,
        cdo_compression: str = "-f nc4c -z zip_2"
    ) -> str:
        """
        Optimiza un NetCDF para GrADS con CDO como paso final.

        Args:
            input_file: Ruta del archivo de entrada.
            output_file: Ruta de salida. Si es None, se usa 'grads_' + input_file.
            rename_dict: Diccionario para renombrar dimensiones.
            cdo_compression: Parámetros de compresión para CDO.

        Returns:
            Ruta del archivo optimizado.
        """
        try:
            # Configuración por defecto
            rename_dict = rename_dict or {'pressure_level': 'level', 'valid_time': 'time'}
            output_file = output_file or f"grads_{os.path.basename(input_file)}"
            tmp_file = f"tmp_{os.path.basename(input_file)}"

            # Paso 1: Renombrar dimensiones con xarray
            with xr.open_dataset(input_file) as ds:
                # Renombrar dimensiones
                for old_name, new_name in rename_dict.items():
                    if old_name in ds.dims:
                        ds = ds.rename({old_name: new_name})

                # Guardar temporalmente
                ds.to_netcdf(tmp_file)

            # Paso 2: Compresión y optimización con CDO
            os.system(f'cdo {cdo_compression} copy {tmp_file} {output_file}')

            # Limpieza
            if os.path.exists(tmp_file):
                os.remove(tmp_file)

            logging.info(f"Archivo optimizado con CDO: {output_file}")
            return output_file

        except Exception as e:
            logging.error(f"Error al optimizar el archivo: {e}")
            if os.path.exists(tmp_file):
                os.remove(tmp_file)
            raise
