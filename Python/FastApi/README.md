# Prueba de FastApi y Streamlit

FastApi maneja el backend y Streamlit maneja el frontend. En esta ocasión el front end es una aplicación web.

## Configuración previa

**Instalar un ambiente virtual de python y los requerimientos**

Ubicate en el directorio donde trabajarás la prueba. Ejemplo proyecto/test

Linux:

```bash
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Windows (PowerShell):

```powershell
python3 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Nota: Si windows te marca error al querer ejecutar concede permisos mediante la instrucción:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Nota: Cada vez que entres a trabajar en este proyecto deberás activar de nuevo el ambiente. No es necesario volver a instalar el ambiente o los requerimientos. Por ejemplo: 

```powershell
.\venv\Scripts\Activate.ps1
```


