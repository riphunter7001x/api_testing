from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='1234',
            database='stud'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            query = 'SELECT * FROM student'
            cursor.execute(query)
            rows = cursor.fetchall()

            data = []
            for row in rows:
                data.append({'rollno': row[0], 'sname': row[1], 'dept': row[2]})

            return jsonify(data)

    except Error as e:
        print('Error:', e)
        return jsonify({'error': 'An error occurred'})

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run()
