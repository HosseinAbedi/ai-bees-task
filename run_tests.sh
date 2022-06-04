#!/usr/bin/env bash
export $(cat .env) # local only
pip install pytest-cov
python -m spacy download en
pytest --cov=src   ./tests/unit/functional_tests.py  --cov-report=xml  
coverage xml -i

