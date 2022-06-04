#!/usr/bin/env bash
export $(cat .env)

uwsgi --http :$SERVER_PORT --wsgi-file server.py  --callable app --master --processes 2 --threads 2 -b 65536 --listen 128
