FROM python:3.8-slim

WORKDIR /code

ADD extractor.py /code

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc 

COPY Pipfile* /code/
RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "extractor.py"]