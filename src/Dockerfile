FROM python:3.10
WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt
##CMD [ "python", "index.py" ]
CMD [ "streamlit","run", "index.py" ]