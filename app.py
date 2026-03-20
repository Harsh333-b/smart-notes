from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            tag TEXT,
            created_at TEXT
        )
    ''')

    # Basic optimization (index for faster search)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_title ON notes(title)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_content ON notes(content)")

    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db()
    notes = conn.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    tag = request.form['tag']
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    conn = get_db()
    conn.execute("INSERT INTO notes (title, content, tag, created_at) VALUES (?, ?, ?, ?)",
                 (title, content, tag, created_at))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_note(id):
    conn = get_db()
    conn.execute("DELETE FROM notes WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    conn = get_db()

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tag = request.form['tag']

        conn.execute(
            "UPDATE notes SET title=?, content=?, tag=? WHERE id=?",
            (title, content, tag, id)
        )
        conn.commit()
        conn.close()
        return redirect('/')

    note = conn.execute("SELECT * FROM notes WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template('edit.html', note=note)

@app.route('/search')
def search():
    query = request.args.get('q', '')

    conn = get_db()
    notes = conn.execute(
        "SELECT * FROM notes WHERE title LIKE ? OR content LIKE ? ORDER BY id DESC",
        (f'%{query}%', f'%{query}%')
    ).fetchall()
    conn.close()

    return jsonify([dict(n) for n in notes])

init_db()
import os

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)