CouchPotato Exporter
====================

![Docker Pulls](https://img.shields.io/docker/pulls/rj170590/couchpotato_exporter)

:thinking: What is this?
------------------------
A simple docker image running a exporter for couchpotato to be used with Prometheus

:raised_eyebrow: What does it give me?
--------------------------------------
The exporter provides the following metrics for us within Prometheus:
* `couchpotato_total_movies` - Total number of movies within CouchPotato
* `couchpotato_total_wanted` - Total number of movies wanted
* `couchpotato_total_done` - Total number of movies completed

:exploding_head: How do I use this?
-----------------------------------
Run docker as follows with these environment variables:

* `COUCHPOTATO_URL` - The url (including http/https and port) of your CouchPotato instance. E.g. `https://mycouchpotato.local`
* `COUCHPOTATO_API_KEY` - The API key to use with CouchPotato

On the CLI run:

```bash
docker run -p 9315:9315 -e COUCHPOTATO_URL=$COUCHPOTATO_URL -e COUCHPOTATO_API_KEY=$COUCHPOTATO_API_KEY rj170590/couchpotato_exporter
```

Once running, configure a Prometheus job:

```
- job_name: 'couchpotato'
    scrape_interval: 1m
    static_configs:
        - targets: ['172.17.0.1:9316']
```