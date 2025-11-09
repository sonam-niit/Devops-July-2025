from flask import Flask,jsonify
import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

load_dotenv(dotenv_path='/home/ubuntu/app/.env')

app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
        )
        return conn
    except OperationalError as e:
        print(f"Database connectivity failed: {e}")
        return None
    
@app.route('/')
def hello():
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        return jsonify({
            'status':"Connected to DB",
            'DB_Version': db_version[0]
        })
    else:
        return jsonify({
            'status':'falied to connect with DB'
        }),500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)