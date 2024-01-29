export DATABASE_URL=postgresql://fastapi_traefik:fastapi_traefik@localhost:5432/fastapi_traefik
export SECRET_KEY=2f92041b9c778316ebbaf5e639c19d1088e6372f8904728eaa1f79a30cd05e2e
export ALGORITHM=HS256

uvicorn app.main:app --reload --host 127.0.0.1 --port 8008