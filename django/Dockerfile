FROM python:3.11

WORKDIR /data

COPY requeirements.txt .

RUN pip install -r requeirements.txt

RUN pip install psycopg2-binary --force-reinstall --no-cache-dir

COPY . .

EXPOSE 8000
