fetch('http://127.0.0.1:5000/api/cuaca')
    .then(response => response.json())
    .then(data => {
        // Menampilkan data yang didapatkan
        document.getElementById('submax').textContent = data.submax;
        document.getElementById('suhumin').textContent = data.suhumin;
        document.getElementById('suhurata').textContent = data.suhurata;

        // Menampilkan data suhuMaxHumid
        const suhuMaxHumidDiv = document.getElementById('suhuMaxHumid');
        data.nilai_suhu_max_humid_max.forEach(item => {
            const div = document.createElement('div');
            div.classList.add('data-item');
            div.innerHTML = `
                <p><strong>Idx:</strong> ${item.idx}</p>
                <p><strong>Suhu:</strong> ${item.suhu}°C</p>
                <p><strong>Humidity:</strong> ${item.humid}%</p>
                <p><strong>Kecerahan:</strong> ${item.kecerahan}</p>
                <p><strong>Timestamp:</strong> ${item.timestamp}</p>
            `;
            suhuMaxHumidDiv.appendChild(div);
        });

        // Menampilkan data month_year_max
        const monthYearMaxDiv = document.getElementById('monthYearMax');
        data.month_year_max.forEach(item => {
            const div = document.createElement('div');
            div.classList.add('data-item');
            div.innerHTML = `<p><strong>Bulan-Tahun:</strong> ${item.month_year}</p>`;
            monthYearMaxDiv.appendChild(div);
        });
    })
    .catch(error => {
        console.error('Error fetching data:', error);
        const errorMessageDiv = document.getElementById('error-message');
        errorMessageDiv.textContent = "Failed to load data from the server.";
    });
