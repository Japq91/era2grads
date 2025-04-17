# ERA2GRADS

Herramienta para descargar, procesar y visualizar datos ERA5 en formato NetCDF, optimizados para GrADS.

## 🚀 Características principales
- **Descarga de datos ERA5**:
  - Niveles de presión (variables atmosféricas)
  - Nivel de superficie (variables meteorológicas superficiales)
- **Procesamiento post-descarga**:
  - Validación de datos descargados
  - Transformación de formatos y variables
  - Optimización para GrADS
- **Visualización**:
  - Gráficos básicos con matplotlib/xarray
  - Personalización de visualizaciones

## 📦 Instalación

1. Clona el repositorio:
```bash
   git clone https://github.com/Japq91/era2grads.git
   cd era2grads
```

2. Instala las dependencias:
```bash
   pip install -e .
```

3. Configura tu API key de CDS (Copernicus Data Store):
   - Crea un archivo `$HOME/.cdsapirc` con tus credenciales
   - [Instrucciones para obtener credenciales](https://cds.climate.copernicus.eu/user-guide)

## 🏁 Uso básico

### Descarga de datos
```python
from era2grads import PressureLevelDownloader, SingleLevelDownloader

# Descargar datos de niveles de presión
downloader = PressureLevelDownloader()
downloader.download(
    variables=['u_component_of_wind', 'v_component_of_wind'],
    year=2023,
    month=6,
    days=[15, 16],
    pressure_levels=[500, 850],
    area=[10, -80, -10, -60],  # [N, W, S, E]
    output_file="datos/viento_niveles.nc"
)

# Descargar datos de superficie
surface_downloader = SingleLevelDownloader()
surface_downloader.download(
    variables=['10m_u_component_of_wind', '2m_temperature'],
    year=2023,
    month=6,
    days=list(range(1, 31)),  # Todo el mes
    area=[10, -80, -10, -60],
    output_file="datos/superficie.nc"
)
```

### Procesamiento y conversión
```python
from era2grads.process.transformer import ERA5Transformer

transformer = ERA5Transformer()
transformer.process(
    input_file="datos/viento_niveles.nc",
    output_file="datos_procesados/viento_optimizado.nc",
    rename_variables={'u': 'u_wind', 'v': 'v_wind'},
    scale_factors={'u_wind': 1.0, 'v_wind': 1.0}
)
```

### Visualización
```python
from era2grads.visualize.plotter import ERA5Plotter

plotter = ERA5Plotter()
plotter.plot_contour(
    file_path="datos_procesados/viento_optimizado.nc",
    variable="u_wind",
    level=500,
    time_index=0
)
```

## 📚 Documentación avanzada
Consulta el notebook de demostración [`examples/era2grads_demo.ipynb`] para ejemplos detallados.

## 🤝 Contribuciones
```
--
```

## 📝 Licencia
```
--
```

## Estructura del proyecto:
   ```
   era2grads/
   ├── __init__.py
   ├── download/
   │   ├── __init__.py
   │   ├── pressure.py
   │   └── surface.py
   ├── process/
   │   ├── __init__.py
   │   ├── validator.py
   │   └── transformer.py
   ├── visualize/
   │   ├── __init__.py
   │   └── plotter.py
   ├── docs/
   ├── examples/
   │   └── era2grads_demo.ipynb
   ├── tests/
   ├── setup.py
   └── README.md
   ```

