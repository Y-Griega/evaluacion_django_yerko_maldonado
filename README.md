
# Evaluacion 2 back end

Este proyecto es una aplicación web desarrollada en Django. A continuación se detallan los pasos para ejecutar el proyecto localmente.

## Tener python instalado

Asegúrate de tener Python instalado. Puedes verificar la instalación con:
  ```bash
  python --version
  ```

## La Instalación

1. **Clona el repositorio en tu máquina**
   ```bash
   git clone (https://github.com/Y-Griega/evaluacion_django_yerko_maldonado.git)
   ```
2. **Navega al directorio del proyecto**:
   ```bash
   cd evaluacion_django_yerko_maldonado
   ```
3. **Crear un entorno virtual**
   ```bash
   python -m venv env
   ```
   Activa el entorno virtual
     ```bash
     .\env\Scripts\activate
     ```

4. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## Migraciones de base de datos

Ejecuta las migraciones de la base de datos para configurar las tablas
```bash
python manage.py migrate
```

## Ejecutar el proyecto

Inicia el servidor de desarrollo con el siguiente comando:
```bash
python manage.py runserver
```

Luego, abre tu navegador y visita [http://127.0.0.1:8000](http://127.0.0.1:8000) para ver el proyecto en funcionan.


