FROM python:latest
WORKDIR /usr/src
RUN git clone https://github.com/ADGEfficiency/crunchbase
WORKDIR /usr/src/crunchbase
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
