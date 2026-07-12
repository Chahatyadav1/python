FROM python:3.12-slim
WORKDIR /app
COPY Day-11.py .
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
RUN groupadd -r controller && useradd -r -g controller -u 10001 controller
USER 10001
EXPOSE 8000
CMD ["gunicorn","--bind","0.0.0.0:8000","-w","4","Day-11:app"]