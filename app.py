from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Database setup
def init_db():
    conn = sqlite3.connect("veterinary_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            region TEXT,
            district TEXT,
            species TEXT,
            disease TEXT,
            vaccination_date TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/submit", methods=["POST"])
def submit_data():
    data = request.json
    try:
        conn = sqlite3.connect("veterinary_data.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reports (region, district, species, disease, vaccination_date)
            VALUES (?, ?, ?, ?, ?)
        """, (data["region"], data["district"], data["species"], data["disease"], data.get("vaccination", None)))
        conn.commit()
        conn.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
