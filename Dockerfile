FROM python:3.9-alpine

WORKDIR /usr/api/sx_api

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]