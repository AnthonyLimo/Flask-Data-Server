FROM python:3
WORKDIR /code
ENV FLASK_APP data.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install -i https://test.pypi.org/simple/ africastalking==1.1.7.post4
COPY . .
CMD ["flask","run"]