FROM python:3.11

WORKDIR /bot/

COPY ./req.txt ./

RUN pip install --no-cache-dir -r ./req.txt

COPY . .

CMD python ./app.py