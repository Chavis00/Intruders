FROM python:3.10.11-slim-buster

# Create workDir
RUN mkdir code
WORKDIR code
ENV PYTHONPATH = /code

#RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
#RUN rustup default nightly



RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender-dev



#upgrade pip if you like here
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy Code
COPY . .

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
