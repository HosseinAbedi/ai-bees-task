FROM  python:3.7-bullseye

############################################################
# Updating the OS and user creation
############################################################

RUN apt-get update && \
    apt-get install -y  \
     python3-pip \
     libblas-dev \
     liblapack-dev \
     libatlas-base-dev \
     libyaml-dev \
     gfortran \
     python3-scipy \
     python3-numpy \
     python3-pandas \ 
     && rm -rf /var/lib/apt/lists/*

RUN adduser app
USER app
WORKDIR /home/app
COPY --chown=app:app requirements.txt requirements.txt
ENV PATH="/home/app/.local/bin:${PATH}"
RUN pip install --no-cache-dir --upgrade pip \
   &&  pip install --no-cache-dir  --user -r requirements.txt
COPY --chown=app:app . .

############################################################
# Installing the requirements and running the server
############################################################

CMD ["bash", "run.sh"]

