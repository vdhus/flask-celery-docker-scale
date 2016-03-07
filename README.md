## flask-celery-docker-scale
Example docker-compose config for scaling celery worker with separate code base. It uses the classical addition task as an example.

To run the example:
```bash

docker-compose build
docker-compose up -d # run in detached mode

```

No load `http://your-dockermachine-ip:5000/add/2/3` in browser. It should create a task and return a task id.

To check the status of the job hit `http://your-dockermachine-ip:5000/check/taskid`. It should either show `PENDING` or the result `5`.

To monitor that the worker is working fine go to `http://your-dockermachine-ip:5555`. It should show one worker ready to serve.

To scale the workers, now run `docker-compose scale worker=5`. This will create `4` more containers each running a worker. `http://your-dockermachine-ip:5555` should now show 5 workers waiting for some jobs!
