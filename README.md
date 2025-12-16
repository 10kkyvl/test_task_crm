# Django CRM MVP (Test Assignment)

## Tech stack
- Django (admin for CRUD UI)
- Django REST Framework (minimal API endpoints)
- PostgreSQL
- Docker Compose
- uv (Python package manager)

## How to run

### 1) Start services
```bash
docker-compose up --build
```

### 2) Create admin user
```bash
docker-compose exec web python manage.py createsuperuser
```

Open:
- Admin UI: `/admin/`
- API root: `/api/`

## Features implemented

### Admin UI (CRUD)
- Full CRUD for:
  - Client (name, phone, email, created_at)
  - Deal (client, title, amount, status, created_at)
  - Note (deal, text, created_at)
- Client list with pagination and search by name/phone/email (admin list view)
- Client detail showing related deals (admin relations/inlines)
- Deal detail showing related notes and allowing adding notes (admin relations/inlines)

### Minimal API (DRF)
- `GET /api/clients/` - list clients (JSON, ModelSerializer, DRF generic views)
- `GET /api/deals/?status=new` - list deals filtered by status

## Research approach used
From the research document, the selected approach is **Django Admin-first** for the MVP due to:
- fastest delivery of complete CRUD
- reliability of Django built-ins
- minimal custom UI code, which reduces bugs and maintenance

## Notes
- Unit tests were not added because the assignment focuses on quick MVP delivery and the primary UI is Django Admin.
