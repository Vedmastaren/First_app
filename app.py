from flask import Flask, render_template, request, redirect
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
dbname = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')

app = Flask(__name__)

# Funktion för att skapa en anslutning till databasen
def connect_to_db():
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    return conn

# Funktion för att hämta alla anteckningar från databasen
def get_notes():
    conn = connect_to_db()
    c = conn.cursor()
    c.execute('SELECT * FROM notes')
    notes = c.fetchall()
    conn.close()
    return notes

# Funktion för att lägga till en ny anteckning i databasen
def add_note(title, content):
    conn = connect_to_db()
    c = conn.cursor()
    c.execute('INSERT INTO notes (title, content) VALUES (%s, %s)', (title, content))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    notes = get_notes()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note_route():
    title = request.form.get('title', '')  # Hämta titeln från formuläret, default till tom sträng om den inte finns
    content = request.form['content']  # Hämta innehållet från formuläret

    if content:  # Kontrollera om innehållet finns
        add_note(title, content)  # Lägg till anteckningen i databasen
    else:
        print("Content is empty. Note not added.")  # Skriv ut ett felmeddelande om innehållet är tomt

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
