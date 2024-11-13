from collections import OrderedDict
import mysql.connector
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='db_cuaca'
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Mendapatkan suhu maksimum, suhu minimum, dan suhu rata-rata
    cursor.execute('SELECT MAX(suhu) AS suhumax FROM tb_cuaca')
    suhumax = cursor.fetchone()['suhumax']

    cursor.execute('SELECT MIN(suhu) AS suhumin FROM tb_cuaca')
    suhumin = cursor.fetchone()['suhumin']

    cursor.execute('SELECT AVG(suhu) AS suhurata FROM tb_cuaca')
    suhurata = cursor.fetchone()['suhurata']

    # Mendapatkan data suhu maksimum dan humidity maksimum
    cursor.execute('SELECT id, suhu, humid, lux, ts FROM tb_cuaca WHERE suhu = (SELECT MAX(suhu) FROM tb_cuaca)')
    suhu_max = cursor.fetchall()

    cursor.execute('SELECT id, suhu, humid, lux, ts FROM tb_cuaca WHERE humid = (SELECT MAX(humid) FROM tb_cuaca)')
    humid_max = cursor.fetchall()

    # Mendapatkan bulan dan tahun
    cursor.execute('SELECT DISTINCT DATE_FORMAT(ts, "%m-%Y") AS month_year FROM tb_cuaca ORDER BY month_year DESC')
    month_year_max = cursor.fetchall()

    # Menghitung jumlah data cuaca
    cursor.execute('SELECT COUNT(*) AS jumlah_data FROM tb_cuaca')
    jumlah_data = cursor.fetchone()['jumlah_data']

    conn.close()

    # Menyiapkan dictionary untuk data suhu dan humidity maksimum
    nilai_suhu_max_humid_max = OrderedDict()
    for i, suhu in enumerate(suhu_max):
        nilai_suhu_max_humid_max[str(i)] = {
            'idx': suhu['id'],
            'suhu': suhu['suhu'],
            'humid': suhu['humid'],
            'kecerahan': suhu['lux'],
            'timestamp': suhu['ts']
        }
    
    for i, humid in enumerate(humid_max, start=len(nilai_suhu_max_humid_max)):
        if humid['id'] not in [entry['idx'] for entry in nilai_suhu_max_humid_max.values()]:
            nilai_suhu_max_humid_max[str(i)] = {
                'idx': humid['id'],
                'suhu': humid['suhu'],
                'humid': humid['humid'],
                'kecerahan': humid['lux'],
                'timestamp': humid['ts']
            }

    month_year_max_dict = OrderedDict()
    for i, item in enumerate(month_year_max):
        month_year_max_dict[str(i)] = {
            'month_year': item['month_year']
        }

    return render_template('index.html', 
                           suhumax=suhumax, 
                           suhumin=suhumin, 
                           suhurata=f"{suhurata:.2f}",
                           nilai_suhu_max_humid_max=nilai_suhu_max_humid_max, 
                           month_year_max=month_year_max_dict,
                           jumlah_data=jumlah_data)

@app.route('/api/cuaca', methods=['GET'])
def get_cuaca():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT MAX(suhu) AS suhumax FROM tb_cuaca')
    suhumax = cursor.fetchone()['suhumax']

    cursor.execute('SELECT MIN(suhu) AS suhumin FROM tb_cuaca')
    suhumin = cursor.fetchone()['suhumin']

    cursor.execute('SELECT AVG(suhu) AS suhurata FROM tb_cuaca')
    suhurata = cursor.fetchone()['suhurata']

    cursor.execute('SELECT id, suhu, humid, lux, ts FROM tb_cuaca WHERE suhu = %s', (suhumax,))
    suhu_max = cursor.fetchall()

    cursor.execute('SELECT id, suhu, humid, lux, ts FROM tb_cuaca WHERE suhu = %s LIMIT 1', (suhumin,))
    suhu_min = cursor.fetchone()

    month_year_max = get_month_of_year_max(cursor, suhumax)

    # Menghitung jumlah data cuaca
    cursor.execute('SELECT COUNT(*) AS jumlah_data FROM tb_cuaca')
    jumlah_data = cursor.fetchone()['jumlah_data']

    conn.close()

    result = OrderedDict()
    result['submax'] = suhumax
    result['suhurata'] = f"{suhurata:.2f}"

    nilai_suhu_max_humid_max = OrderedDict()

    for i, record in enumerate(suhu_max):
        nilai_suhu_max_humid_max[str(i)] = {
            'suhu': record['suhu'],
            'humid': record['humid'],
            'kecerahan': record['lux'],
            'timestamp': record['ts'],
            'idx': record['id']
        }

    if suhu_min:
        nilai_suhu_max_humid_max[str(len(nilai_suhu_max_humid_max))] = {
            'suhu': suhu_min['suhu'],
            'humid': suhu_min['humid'],
            'kecerahan': suhu_min['lux'],
            'timestamp': suhu_min['ts'],
            'idx': suhu_min['id']
        }

    result['nilai_suhu_max_humid_max'] = nilai_suhu_max_humid_max
    result['month_year_max'] = [
        {'month_year': item['month_year']} for item in month_year_max
    ]
    result['jumlah_data'] = jumlah_data

    return jsonify(result)

def get_month_of_year_max(cursor, suhumax):
    cursor.execute(
        'SELECT DISTINCT DATE_FORMAT(ts, "%m-%Y") AS month_year FROM tb_cuaca WHERE suhu = %s',
        (suhumax,)
    )
    return cursor.fetchall()

if __name__ == '__main__':
    app.run(debug=True)
