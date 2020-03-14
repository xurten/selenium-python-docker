FROM python:latest

COPY tests/other .
RUN python -m unittest tests.py > python_results.txt
ENTRYPOINT /bin/bash