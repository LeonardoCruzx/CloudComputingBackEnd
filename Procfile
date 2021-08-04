release: python manage.py migrate --no-input
web: gunicorn cloudinary_backend.wsgi --log-file=-