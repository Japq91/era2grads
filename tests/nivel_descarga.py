from era2grads import PressureLevelDownloader
# Configuración de la descarga
downloader = PressureLevelDownloader()
downloader.download(
    variables=['u_component_of_wind', 'v_component_of_wind'],
    year=[2023],
    month=[6],
    days=[15],
    pressure_levels=[500, 850],
    area=[10, -80, -10, -60],  # [N, O, S, E] -> América del Sur
    output_file="borrar_leves_1.nc"
)
