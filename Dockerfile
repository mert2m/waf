FROM python:3.9-slim

# Uygulama için gerekli paketleri yükle
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# WAF ve ana uygulama kodunu kopyala
COPY waf.py /app/waf.py
COPY main.py /app/main.py

# Ana uygulamayı çalıştır
CMD ["python", "./main.py"]
