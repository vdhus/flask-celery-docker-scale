# Bid optimization API skeleton

## Actions

Import the bid optimization method into `flask-celery/tasks.py` and
replace the placeholder `find_optimal_bids` method.

## Development

In three different terminals, run:

```sh
./development.sh up --build
```

```sh
./development.sh exec web bash
python3 app.py
```

```sh
./development.sh exec worker bash
celery -A tasks worker --loglevel=info
```

## Production

Start using `docker-compose`

```sh
docker-compose up --build
```

