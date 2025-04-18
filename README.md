# backend-beardStyle-Web

Este proyecto es una API desarrollada con Django y Django REST Framework para gestionar datos relacionados con la aplicación "BeardStyle".

## Estructura del Proyecto

- **myproject/**: Contiene la configuración principal del proyecto Django.
  - `settings.py`: Configuración del proyecto.
  - `urls.py`: Definición de las rutas principales.
  - `wsgi.py` y `asgi.py`: Configuración para servidores WSGI y ASGI.
- **myapp/**: Contiene la lógica de la aplicación.
  - `models.py`: Definición de los modelos de datos.
  - `serializers.py`: Serialización de los datos.
  - `views.py`: Lógica de las vistas y endpoints.
  - `urls.py`: Rutas específicas de la aplicación.
  - `admin.py`: Configuración del panel de administración.

## Funcionalidades Principales

### Inserción de Datos
- **Endpoint**: `POST /api/resource/`
- **Descripción**: Permite crear un nuevo recurso en la base de datos.
- **Código relevante**:
  ```python
  class ResourceCreateView(generics.CreateAPIView):
      queryset = Resource.objects.all()
      serializer_class = ResourceSerializer
  ```

### Consulta de Datos
- **Endpoint**: `GET /api/resource/`
- **Descripción**: Recupera una lista de recursos.
- **Código relevante**:
  ```python
  class ResourceListView(generics.ListAPIView):
      queryset = Resource.objects.all()
      serializer_class = ResourceSerializer
  ```

### Actualización de Datos
- **Endpoint**: `PUT /api/resource/<id>/`
- **Descripción**: Actualiza un recurso existente.
- **Código relevante**:
  ```python
  class ResourceUpdateView(generics.UpdateAPIView):
      queryset = Resource.objects.all()
      serializer_class = ResourceSerializer
  ```

### Eliminación de Datos
- **Endpoint**: `DELETE /api/resource/<id>/`
- **Descripción**: Elimina un recurso existente.
- **Código relevante**:
  ```python
  class ResourceDeleteView(generics.DestroyAPIView):
      queryset = Resource.objects.all()
      serializer_class = ResourceSerializer
  ```

## Cómo Probar en Postman

### 1. Inserción de Datos
- **Método**: POST
- **URL**: `http://localhost:8000/api/resource/`
- **Body** (JSON):
  ```json
  {
      "field1": "value1",
      "field2": "value2"
  }
  ```

### 2. Consulta de Datos
- **Método**: GET
- **URL**: `http://localhost:8000/api/resource/`

### 3. Actualización de Datos
- **Método**: PUT
- **URL**: `http://localhost:8000/api/resource/<id>/`
- **Body** (JSON):
  ```json
  {
      "field1": "new_value1",
      "field2": "new_value2"
  }
  ```

### 4. Eliminación de Datos
- **Método**: DELETE
- **URL**: `http://localhost:8000/api/resource/<id>/`

## Requisitos Previos

1. Instalar las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

2. Aplicar las migraciones:
   ```bash
   python manage.py migrate
   ```

3. Iniciar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Notas Adicionales
- Asegúrate de configurar correctamente la base de datos en `settings.py`.
- Puedes acceder al panel de administración en `http://localhost:8000/admin/` después de crear un superusuario con:
  ```bash
  python manage.py createsuperuser
  ```
