# Personal Web (Flask) - Portfolio en Espanol

Sitio web personal enfocado en posicionamiento como **Analytics Engineer**.

## Secciones

- `/` Inicio (propuesta de valor + resultados)
- `/work` Experiencia (casos profesionales anonimizados)
- `/projects` Proyectos personales (curados)
- `/services` Servicios
- `/resume` Curriculumn (PDF + resumen)
- `/contact` Contacto (form con Cloudflare Turnstile)

## Requisitos

- Python 3.11+ (recomendado 3.12)

## Ejecutar local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Luego abre `http://127.0.0.1:5000/`.

## Variables de entorno

El formulario de contacto usa Mail + Cloudflare Turnstile.

Ejemplo `.env` (no se versiona):

```bash
SECRET_KEY=...

TURNSTILE_SECRET_KEY=...

MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=...
MAIL_PASSWORD=...
MAIL_DEFAULT_SENDER=...

RECIPIENT_EMAIL=...
```

