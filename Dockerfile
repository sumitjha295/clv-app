FROM python:3

COPY . /usr/src/app

WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app/src

CMD [ "python", "./app.py" ]