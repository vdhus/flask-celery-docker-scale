in one terminal
./development.sh up --build

in one terminal
./development.sh exec web bash
python3 app.py

another terminal
./development.sh exec worker bash
celery -A tasks worker --loglevel=info
