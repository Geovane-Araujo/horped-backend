FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

COPY letsencrypt.crt /app
COPY letsencrypt.key /app

ENV SSL_CERTIFICATE=/app/letsencrypt.crt
ENV SSL_KEY=/app/letsencrypt.key

EXPOSE 5010
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5010", "--cert=$SSL_CERTIFICATE", "--key=$SSL_KEY"]