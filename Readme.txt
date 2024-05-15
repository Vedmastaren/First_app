1. Skapa en venv
python -m venv venv 
eller 
python3 -m venv venv

2. Aktivera venv
source venv/Scripts/activate

3. Ladda ner flask, psycopg2 och dotenv
pip install Flask
pip install psycopg2
pip install python-dotenv

4. skapa en app.py fil
app.py

5. Skapa en html fil
Skapa en mapp med namn templates
Skapa en fil i mappen 
index.html

6. Skapa en lokal databas och logga in med dina uppgifter (använde postgres)
notes.sql
Skapa tables och kör dem med CTRL + E x2

7. Skapa en .gitignore fil för att ignorera valda ting
.gitignore

8. Skapa en .env fil för att dölja uppgifter
.env

9. Kör appen 
python app.py
