cat <<EOF | tee -a .env
ALLOWED_HOSTS="`hostname -i`,127.0.0.1"
EOF
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8080
