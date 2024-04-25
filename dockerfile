FROM python:3.10-slim-buster

# prepare environment
RUN apt-get -y update
RUN apt-get -y upgrade
RUN pip install --upgrade pip

# copy and install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --user -r /requirements.txt

# create and set working directory
#WORKDIR /app

# install srai_athena_frontend_telegram module
COPY fromurl_backend /fromurl_backend
COPY font /font
COPY asset /asset
COPY script /script
COPY setup.py /setup.py
COPY setup.cfg /setup.cfg
COPY README.md /README.md
RUN pip install --user -e .

# contains config
CMD python app/main.py