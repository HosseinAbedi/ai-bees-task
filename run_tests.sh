#!/usr/bin/env bash
export $(cat .env) 
pip install pytest-cov
pytest --cov=src   ./tests/unit/tests.py  --cov-report=xml  
coverage xml -i

