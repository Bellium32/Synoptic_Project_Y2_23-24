document.addEventListener('DOMContentLoaded', () => {
// Function to fetch Sen Monorom weather data from the OpenWeatherMap API
    const fetchSenMonoromWeatherData = async () => {
        const apiKey = 'd3dda624a81af4587511e0524a1bbc5a';
        const lat = 12.5776539;
        const lon = 106.9349172;
        const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Error fetching Sen Monorom weather data: ${response.statusText}`);
            }
            const weatherData = await response.json();
            return weatherData;
        } catch (error) {
            console.error('Error:', error);
            return null;
        }
    };

    // Function to display Sen Monorom weather data on the webpage
    const displaySenMonoromWeather = (weatherData) => {
        const senMonoromElement = document.getElementById('senMonorom');
        if (weatherData) {
            const temperature = weatherData.main.temp;
            const weatherDescription = weatherData.weather[0].description;
            const weatherEmoji = getWeatherEmoji(weatherData.weather[0].id); // Get the relevant emoji
            senMonoromElement.innerHTML = `
                <h2>Sen Monorom Weather</h2>
                <div>Temperature: ${temperature}°C</div>
                <div>Weather: ${weatherEmoji} ${weatherDescription}</div>
            `;
        } else {
            senMonoromElement.textContent = 'Unable to fetch Sen Monorom weather data.';
        }
    };

    // Fetch and display Sen Monorom weather data
    fetchSenMonoromWeatherData().then(weatherData => {
        displaySenMonoromWeather(weatherData);
    });

    const apiKey = 'd3dda624a81af4587511e0524a1bbc5a';
    const lat = 12.5776539;
    const lon = 106.9349172;

    const getWeatherEmoji = (weatherId) => {
        const emojiMap = {
            200: "⛈️", 201: "⛈️", 202: "⛈️", 210: "⛈️", 211: "⛈️", 212: "⛈️", 221: "⛈️", 230: "⛈️", 231: "⛈️", 232: "⛈️",
            300: "🌦️", 301: "🌦️", 302: "🌦️", 310: "🌦️", 311: "🌦️", 312: "🌦️", 313: "🌦️", 314: "🌦️", 321: "🌦️",
            500: "🌧️", 501: "🌧️", 502: "🌧️", 503: "🌧️", 504: "🌧️", 511: "🌧️", 520: "🌧️", 521: "🌧️", 522: "🌧️", 531: "🌧️",
            600: "❄️", 601: "❄️", 602: "❄️", 611: "❄️", 612: "❄️", 613: "❄️", 615: "❄️", 616: "❄️", 620: "❄️", 621: "❄️", 622: "❄️",
            701: "🌫️", 711: "🌫️", 721: "🌫️", 731: "🌫️", 741: "🌫️", 751: "🌫️", 761: "🌫️", 762: "🌫️", 771: "🌫️", 781: "🌪️",
            800: "🌞",
            801: "🌤️", 802: "⛅", 803: "🌥️", 804: "💭"
        };
        return emojiMap[weatherId] || "❓";
    };

    const fetchWeatherData = async () => {
        const url = `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Error fetching weather data: ${response.statusText}`);
            }
            const forecastData = await response.json();
            return forecastData;
        } catch (error) {
            console.error(error);
            return null;
        }
    };

    const showPopup = (message) => {
        const popup = document.getElementById('popup');
        popup.querySelector('.popup-content p').textContent = message;
        popup.style.display = 'block';
    };

    const displayWeatherData = (forecastData) => {
        const today = new Date().toISOString().split('T')[0];
        const todayWeather = forecastData.list.find(f => f.dt_txt.startsWith(today));
        if (todayWeather) {
            const weatherId = todayWeather.weather[0].id;
            const weatherEmoji = getWeatherEmoji(weatherId);
            const weatherDescription = todayWeather.weather[0].description;
            const temperature = todayWeather.main.temp;

            const weatherInfoClass = weatherId >= 200 && weatherId < 300 ? 'weather-info red-block' : 'weather-info';

            if (weatherId >= 200 && weatherId < 300) {
                showPopup("Warning: Thunderstorm expected today!");
            }

            document.getElementById('today').innerHTML = `
                <div class="${weatherInfoClass}">
                    <div>${weatherEmoji} ${weatherDescription}</div>
                    <div class="temperature">${temperature}°C</div>
                </div>
                <div class="temp-range">Low: ${todayWeather.main.temp_min}°C | High: ${todayWeather.main.temp_max}°C</div>
            `;
        }

        const hourlyElement = document.getElementById('hourly');
        hourlyElement.innerHTML = '';
        forecastData.list.filter(f => f.dt_txt.startsWith(today)).forEach(hourly => {
            const hourElement = document.createElement('div');
            hourElement.className = 'hour';
            hourElement.innerHTML = `
                <div>${new Date(hourly.dt_txt).getHours()}:00</div>
                <div>${getWeatherEmoji(hourly.weather[0].id)} ${hourly.main.temp}°C</div>
            `;
            hourlyElement.appendChild(hourElement);
        });

        const forecastElement = document.getElementById('forecast');
        forecastElement.innerHTML = '';
        const dailyTemps = {};
        const dailyWeather = {};
        forecastData.list.forEach(forecast => {
            const date = forecast.dt_txt.split(' ')[0];
            if (!dailyTemps[date]) {
                dailyTemps[date] = [];
            }
            dailyTemps[date].push(forecast.main.temp);
            if (new Date(forecast.dt_txt).getHours() === 12) {
                dailyWeather[date] = forecast;
            }
        });
        Object.keys(dailyTemps).forEach(date => {
            if (date !== today) {
                const temps = dailyTemps[date];
                const avgTemp = (temps.reduce((a, b) => a + b) / temps.length).toFixed(1);
                const minTemp = Math.min(...temps).toFixed(1);
                const maxTemp = Math.max(...temps).toFixed(1);
                const middayWeather = dailyWeather[date];
                forecastElement.innerHTML += `
                    <div class="day-forecast">
                        <div>${date}</div>
                        <div>${getWeatherEmoji(middayWeather.weather[0].id)} ${middayWeather.weather[0].description}</div>
                        <div>${avgTemp}°C (Low: ${minTemp} | High: ${maxTemp})</div>
                    </div>
                `;
            }
        });
    };

    fetchWeatherData().then(forecastData => {
        if (forecastData) {
            displayWeatherData(forecastData);
        }
    });

    document.getElementById('popup').querySelector('.close-button').addEventListener('click', () => {
        document.getElementById('popup').style.display = 'none';
    });

    const ttsTodayButton = document.getElementById('ttsToday');
    const ttsHourlyButton = document.getElementById('ttsHourly');
    const ttsForecastButton = document.getElementById('ttsForecast');

    ttsTodayButton.addEventListener('click', () => {
        const todayText = document.getElementById('today').innerText;
        const speech = new SpeechSynthesisUtterance(todayText);
        window.speechSynthesis.speak(speech);
    });

    ttsHourlyButton.addEventListener('click', () => {
        const hourlyText = document.getElementById('hourly').innerText;
        const speech = new SpeechSynthesisUtterance(hourlyText);
        window.speechSynthesis.speak(speech);
    });

    ttsForecastButton.addEventListener('click', () => {
        const forecastText = document.getElementById('forecast').innerText;
        const speech = new SpeechSynthesisUtterance(forecastText);
        window.speechSynthesis.speak(speech);
    });

    const ttsSenMonoromButton = document.getElementById('ttsSenMonorom');
    ttsSenMonoromButton.addEventListener('click', async () => {
        const senMonoromWeatherData = await fetchSenMonoromWeatherData();
        if (senMonoromWeatherData) {
            const temperature = senMonoromWeatherData.main.temp;
            const weatherDescription = senMonoromWeatherData.weather[0].description;
            const weatherEmoji = getWeatherEmoji(senMonoromWeatherData.weather[0].id);
            const senMonoromText = `Sen Monorom Weather, Temperature is ${temperature} degrees Celsius. ${weatherDescription}.`;
            const speech = new SpeechSynthesisUtterance(senMonoromText);
            window.speechSynthesis.speak(speech);
        }
    });

    
});

