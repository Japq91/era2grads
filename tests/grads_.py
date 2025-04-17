from era2grads.process import NCDFormatter
# Con parámetros personalizados

NCDFormatter.grads_optimize(
    input_file="borrar_superficie_1.nc",
    output_file="salida_grads.nc",
    rename_dict={'latitude': 'lat', 'longitude': 'lon'},
    cdo_compression="-f nc4c -z zip_4"
)

