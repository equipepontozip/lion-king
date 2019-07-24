FROM frolvlad/alpine-python-machinelearning

WORKDIR /api

ADD requirements.txt /api/

RUN pip install -r requirements.txt

ADD . /api/

CMD python api/server.py 
