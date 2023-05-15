FROM python:3.11

WORKDIR /data

COPY requeirements.txt .

RUN pip install -r requeirements.txt

COPY . .

EXPOSE 4200

CMD python run.py 0.0.0.0:4200
