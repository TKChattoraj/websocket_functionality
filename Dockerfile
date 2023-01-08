ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /mysite

WORKDIR /mysite

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

# replace demo.wsgi with <project_name>.wsgi
#CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "mysite.wsgi"]


# alternative CMDs tried:
#CMD ["daphne ", "mysite.asgi:application"]
#CMD python3 manage.py runserver 0.0.0.0:8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
