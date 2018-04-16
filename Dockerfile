FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/requirements
WORKDIR /code
ADD requirements/base.txt /code/requirements/base.txt
ADD requirements/local.txt /code/requirements/local.txt
RUN pip3 install -r requirements/local.txt
ADD src /code/ 
