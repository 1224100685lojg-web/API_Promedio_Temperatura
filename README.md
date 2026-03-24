# API con Flask - Ejercicios Básicos

Este proyecto contiene dos APIs desarrolladas con Flask:

## 🚀 Ejercicio 1: Promedio
Calcula el promedio de calificaciones de un estudiante.

### Endpoint:
POST /promedio

### Ejemplo JSON:
{
  "nombre": "Juan",
  "calificaciones": [80, 90, 85, 70]
}

### Respuesta:
{
  "nombre": "Juan",
  "promedio": 81.25
}

---

## 🌡️ Ejercicio 2: Conversor de Temperatura

Convierte temperaturas entre Celsius y Fahrenheit.

### Endpoint:
POST /convertir-temperatura

### Ejemplo JSON:
{
  "valor": 25,
  "escala": "C"
}

### Respuesta:
{
  "original": "25°C",
  "convertido": "77.0°F"
}

---

## ⚙️ Instalación

1. Crear entorno virtual:
python -m venv venv

2. Activar entorno:
venv\Scripts\activate

3. Instalar dependencias:
python -m pip install -r requirements.txt

4. Ejecutar:
python app.py

---

## 🧪 Pruebas

Usar Postman con método POST y enviar JSON en Body.

---

## 👨‍💻 Autor
Owen
