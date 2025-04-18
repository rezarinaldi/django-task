## Django Task
### Guide

```bash
python -m venv .venv
```
For Windows, bisa pakai Git Bash,
```bash
source .venv/Scripts/activate
```
For Mac,
```bash
source .venv/bin/activate
```

```bash
pip install django
```

```bash
pip install bson
```

```bash
pip freeze > requirements.txt
```
Jika sudah ada ada file requirements.txt, kita bisa menjalankan perintah ini,
```bash
pip install -r requirements.txt
```

Membuat Project
```bash
django-admin startproject myproject
```

Membuat Aplikasi
```bash
python manage.py startapp myapp
# atau
./manage.py startapp myapp
../manage.py startapp myapp (jika sedang di dalam folder berikutnya)
```

Membuat Super User Data
```bash
./manage.py createsuperuser
---
Username: Dikosongi, gunakan default
Email: Dikosongi
Password: minimal 8 karakter, jika tidak 8 karakter sebenarnya masih bisa
```

Membuat Migration Model
```bash
./manage.py makemigrations
./manage.py migrate
```

Menjalankan Server
```bash
./manage.py runserver
```

Formatter Black
```
black .
```

Sorting with Isort
```
isort .
```

- Server akan berjalan di http://127.0.0.1:8000/
- Halaman admin akan berjalan di http://127.0.0.1:8000/admin

### Source
- [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/index.html)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Black](https://black.readthedocs.io/en/stable/)
- [Isort](https://pycqa.github.io/isort/)