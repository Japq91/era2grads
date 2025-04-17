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
from era2grads import NCDFormatter

formatter = NCDFormatter()
formatter.grads_optimize(
    input_file="datos/viento_500hPa.nc",
    output_file="datos_grads/viento_grads.nc",
    rename_dict={'latitude': 'lat', 'longitude': 'lon'},
    cdo_compression="-f nc4c -z zip_4"
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
### Procesamiento post-descarga
  - Renombrado de variables para GrADS (`latitude` → `lat`, `longitude` → `lon`)
  - Compresión eficiente con CDO (`-f nc4c -z zip_4`)
  - Manejo de warnings de NetCDF/CDO

### Warnings comunes
- `cdi warning (cdfScanVarAttr)`: Indica que algunas variables no se encontraron durante la conversión. Verifica:
  - Los nombres en `rename_dict` coinciden con el NetCDF
  - El archivo de entrada tiene la estructura ERA5 estándar

## 📚 Documentación avanzada
- Notebook principal: [`examples/era2grads_demo.ipynb`](examples/era2grads_demo.ipynb)
- Parámetros avanzados de `grads_optimize`:
  - `cdo_compression`: Opciones de compresión (ej. `-z zip_9` para máxima compresión)
  - `time_dim`: Nombre personalizado para dimensión temporal

## 🤝 Contribuciones
```
https://chat.deepseek.com
```

## Requisitos
```bash
cdo>=2.0.0
cdsapi>=0.6.0
xarray>=2023.0
```

## Estructura del proyecto:
```
📦 era2grads
├── 📄 init.py
├── 📄 setup.py
├── 📁 datos/ # Datos descargados (ignorados por git)
├── 📁 datos_grads/ # Datos procesados (ignorados por git)
├── 📁 era2grads/ # Paquete principal
│ ├── 📄 init.py
│ └── ... # Módulos principales
├── 📁 examples/ # Notebooks de demostración
│ └── era2grads_demo.ipynb
├── 📁 tests/ # Pruebas unitarias
└── 📄 .gitignore # Reglas para ignorar archivos
```

