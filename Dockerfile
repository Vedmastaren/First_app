# Använd den officiella Python-bilden som grund
FROM python:3.8-slim

# Ange arbetsmappen inuti containern
WORKDIR /app

# Installera PostgreSQL-klientbiblioteket
RUN apt-get update && apt-get install -y libpq-dev

# Kopiera projektets kravfil och installera beroenden
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera projektets filer inuti containern
COPY . /app

# Ange kommandot som ska köras när containern startas
CMD ["python", "app.py"]
