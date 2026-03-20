# 🧠 Smart Notes App

## 📌 Project Overview
Smart Notes App is a full-stack web application built using Flask that allows users to create, edit, delete, and search notes efficiently. The application provides a clean user interface with real-time search and keyword highlighting for better user experience.

---

## 🚀 Features

- ✅ Create Notes
- 📄 View Notes
- ✏️ Edit Notes
- ❌ Delete Notes
- 🔍 Real-time Search (AJAX)
- ✨ Keyword Highlighting
- 🏷️ Tag-based Filtering
- 📅 Timestamp for each note
- 🎨 Clean and Modern UI

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **Database:** SQLite  
- **Deployment:** Replit / Render  

---

## ⚙️ How It Works

1. User creates a note using the form.
2. Data is stored in SQLite database (`notes.db`).
3. Notes are displayed dynamically on the homepage.
4. Search uses AJAX to fetch results from backend without reloading.
5. Matching keywords are highlighted in real-time.

---

## 🔍 Search Functionality

- Uses JavaScript `fetch()` API
- Sends query to `/search` route
- Backend uses SQL `LIKE` query:
  
```sql
SELECT * FROM notes 
WHERE title LIKE '%keyword%' 
OR content LIKE '%keyword%'
