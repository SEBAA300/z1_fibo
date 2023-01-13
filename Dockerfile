FROM python:latest
RUN mkdir /pyap
COPY fibo.py /pyap/fibo.py
WORKDIR /pyap
RUN pip install pystrich
CMD ["python", "./fibo.py"]
