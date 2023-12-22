from cx_Freeze import setup, Executable

# Ruta al archivo principal .py
main_script = 'main.py'

# Configuración de la construcción
build_exe_options = {
    'include_files': [
        # Lista de rutas a carpetas adicionales que deseas incluir
        'img',
        'sounds',
        # Agrega más carpetas según sea necesario
    ],
    'packages': [],  # Lista de paquetes de Python adicionales que se deben incluir
}

# Configuración del ejecutable
executables = [
    Executable(
        main_script,
        icon='icon.ico'       
               )
]

setup(
    name='Capuchin',
    version='1.0',
    description='Descripción de la aplicación',
    options={'build_exe': build_exe_options},
    executables=executables
)
