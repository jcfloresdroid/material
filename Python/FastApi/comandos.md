## Comandos para levantar los servicios.

**Para levantar FastApi:**

```bash
uvicorn fastapi_test:app --reload
```

(Estará corriendo en `[http://127.0.0.1:8000](http://127.0.0.1:8000)`)



**Para levantar streamlit:**

En otra ventana de la terminal que este en el mismo directorio del proyecto:

```bash
streamlit run streamlit_test.py
```

(Se abrirá tu navegador en `http://localhost:8501` interactuando directamente con FastAPI)


