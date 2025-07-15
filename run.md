
# Instrucciones para correr el proyecto
---

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instalado:

- Python 3.10 o superior  
- `pip` (Administrador de paquetes de Python)

---

## Instalación del entorno

1. Clona o descarga este repositorio.

2. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual:  
    **En Windows:**
    ```bash
    .\env\Scripts\Activate
    ```
    **En Mac / Linux:**
    ```bash
    source venv/bin/activate
    ```

4. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

---

## Ejecutar la API

Desde la raíz del proyecto ejecutar el siguiente comando:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:  
- **http://127.0.0.1:8000/**

---

## Documentación automática

Puedes consultar la documentación de la API (Swagger UI) en:  
- **http://127.0.0.1:8000/docs**  

Y también puedes ver la documentación alternativa (ReDoc) aquí:  
- **http://127.0.0.1:8000/redoc**

---

## Estructura del proyecto

```
backend/
├── app/
│   ├── main.py
│   ├── data/
│   │   ├── products.json
│   │   ├── sellers.json
│   │   ├── payments.json
│   │   └── reviews.json
├── requirements.txt
├── run.md
```

---

## Endpoints principales

| Método | Ruta                           | Descripción                                  |
|--------|--------------------------------|----------------------------------------------|
| GET    | `/products/{product_id}/full`  | Retorna producto, vendedor, pagos y reviews  |
| GET    | `/products/{product_id}`       | Devuelve un producto por ID                  |
| GET    | `/sellers/{seller_id}`         | Devuelve un vendedor por ID                  |
| GET    | `/payments`                    | Devuelve los métodos de pago                 |
| GET    | `/reviews/{product_id}`        | Calificaciones y comentarios del producto    |

---

## Notas finales
✅ Los datos están almacenados en archivos JSON para simular una base de datos.

✅ Esta API es **solo un prototipo** para fines de la prueba técnica.

✅ El código está preparado para escalar fácilmente a una solución más robusta en el futuro.
