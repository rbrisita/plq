FROM jfloff/alpine-python

RUN mkdir /app
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT [ "flask" ]
CMD [ "run", "--host=0.0.0.0" ]
