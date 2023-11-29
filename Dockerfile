FROM python:3.9-slim
COPY script.py /script.py
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "script.py"]