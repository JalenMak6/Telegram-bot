FROM python:3.9
  
WORKDIR /app

ADD main.py stock_function.py test.py .

RUN pip install --upgrade pip \
   && python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
