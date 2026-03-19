# ⚡ SysPerf – System Performance Analyzer

SysPerf is a lightweight, interactive system benchmarking tool that evaluates real-world performance of your machine through CPU, memory, disk, and network tests — all visualized in a modern web dashboard.

---

## 🚀 Features

* 🔥 CPU benchmarking (prime computation)
* 🧠 Memory allocation test
* 💾 Disk read/write speed test
* 🌐 Network latency check
* 📊 Live dashboard with charts
* 🎨 Smooth animations and modern UI
* ⚡ Non-blocking backend (threaded execution)

---

## 🖥️ Dashboard Preview

> Add a GIF or screenshot here (very important for GitHub)

---

## 🏗️ Tech Stack

* Backend: Python + Flask
* Frontend: HTML, CSS, JavaScript
* Charts: Chart.js
* System Monitoring: psutil

---

## 📂 Project Structure

```
systempulse/
│
├── app.py
├── config.py
├── requirements.txt
│
├── tests/
├── core/
├── static/
├── templates/
└── results/
```

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/sysperf.git
cd sysperf
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📊 How It Works

1. Click **Run Test**
2. Backend executes benchmarks in a separate thread
3. Frontend polls results
4. Live graphs update dynamically
5. Final performance score is calculated

---

## 🧠 Scoring System

The performance score is calculated based on:

* CPU execution time
* Disk read/write speed
* Memory allocation success

---

## 🔮 Future Improvements

* WebSocket-based real-time updates
* GPU benchmarking
* Historical comparison
* Export reports (PDF/JSON)
* Multi-device benchmarking

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📜 License

MIT License

---

## ⭐ Show Your Support

If you like this project, consider giving it a ⭐ on GitHub!

