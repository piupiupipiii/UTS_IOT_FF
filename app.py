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

    cursor.execute('SELECT MAX(suhu) AS suhumax FROM tb_cuaca')
    suhumax = cursor.fetchone()['suhumax']

    cursor.execute('SELECT MIN(suhu) AS suhumin FROM tb_cuaca')
    suhumin = cursor.fetchone()['suhumin']

    cursor.execute('SELECT AVG(suhu) AS suhurata FROM tb_cuaca')
    suhurata = cursor.fetchone()['suhurata']

    cursor.execute('SELECT id, suhu, humid, lux, ts FROM tb_cuaca WHERE suhu = (SELECT MAX(suhu) FROM tb_cuaca)')
    suhu_max = cursor.fetchall()

    cursor.execute('SELECT id, suhu, humid, lux, ts FROM tb_cuaca WHERE humid = (SELECT MAX(humid) FROM tb_cuaca)')
    humid_max = cursor.fetchall()

    cursor.execute('SELECT DISTINCT DATE_FORMAT(ts, "%m-%Y") AS month_year FROM tb_cuaca ORDER BY month_year DESC')
    month_year_max = cursor.fetchall()

    conn.close()

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

    return render_template('index.html', suhumax=suhumax, suhurata=f"{suhurata:.2f}",
                           nilai_suhu_max_humid_max=nilai_suhu_max_humid_max, month_year_max=month_year_max_dict)

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

    cursor.execute('SELECT id, suhu, humid, lux, ts FROM tb_cuaca WHERE suhu = (SELECT MAX(suhu) FROM tb_cuaca)')
    suhu_max = cursor.fetchall()

    cursor.execute('SELECT id, suhu, humid, lux, ts FROM tb_cuaca WHERE humid = (SELECT MAX(humid) FROM tb_cuaca)')
    humid_max = cursor.fetchall()

    cursor.execute('SELECT DISTINCT DATE_FORMAT(ts, "%m-%Y") AS month_year FROM tb_cuaca ORDER BY month_year DESC')
    month_year_max = cursor.fetchall()

    conn.close()

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

    # Construct the ordered JSON response
    result = OrderedDict([
        ('month_year_max', month_year_max_dict),
        ('nilai_suhu_max_humid_max', nilai_suhu_max_humid_max),
        ('submax', suhumax),
        ('suhumin', suhumin),
        ('suhurata', f"{suhurata:.2f}")
    ])

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
