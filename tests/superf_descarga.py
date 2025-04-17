from era2grads import SingleLevelDownloader  
# Configuración
downloader = SingleLevelDownloader()
downloader.download(
    variables=['2m_temperature', '10m_u_component_of_wind'],  # variables de superficie
    year=2021,  
    month=6,
    days=[15],
    area=[10, -80, -10, -60],
    output_file="borrar_superficie_1.nc"  # Cambia el nombre del archivo
)
