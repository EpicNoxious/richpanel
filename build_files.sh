echo "BUILD START"
python3.9 -m pip install -r requirements.txt


echo "MAKE MIGRATIONS"
python3.9 manage.py makemigrations app
python3.9 manage.py migrate app
python3.9 manage.py makemigrations
python3.9 manage.py migrate

echo "COLLECT STATIC"
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
