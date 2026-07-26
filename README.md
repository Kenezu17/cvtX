[ConvertX-website-kenezu17s-projects.vercel.app](https://cvt-9qmkcbo9z-kenezu17s-projects.vercel.app/)]

# ConvertX

ConvertX is a modern web-based file conversion platform that allows users to quickly convert files between multiple formats. It features a React frontend and a FastAPI backend, providing a fast, responsive, and user-friendly experience.

## ✨ Features

- 📄 PDF to DOCX
- 📄 DOCX to PDF
- 🖼️ Image (JPG/PNG) to PDF
- 📊 CSV to XLSX
- 📈 Excel to PDF
- ⚡ Fast file processing
- 🔒 Secure uploads with automatic file cleanup
- 📱 Responsive UI built with React and Tailwind CSS

## 🛠️ Tech Stack

### Frontend
- React
- Vite
- Tailwind CSS
- Axios

### Backend
- FastAPI
- Python
- LibreOffice
- Pillow
- pandas
- openpyxl

## 📁 Project Structure

```text
ConvertX/
├── ConvertX/               # Frontend directory
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile          # Frontend container config
├── backend/                # Backend directory
│   ├── app/
│   │   ├── main.py
│   │   └── ...
│   ├── requirements.txt
│   └── Dockerfile          # Backend container config
├── docker-compose.yml      # Orchestrates both services
└── README.md
```

## 🚀 How to Run on Your Laptop

You can run this full-stack application on your laptop using **Docker** (Recommended) or by setting up the services **Manually**.

### 🐳 Method 1: Using Docker (Fastest & Easiest)
With Docker, you do not need to install Node.js, Python, or LibreOffice on your computer. Docker handles all dependencies automatically inside isolated containers.

#### Prerequisites
- Install [Docker Desktop](https://docker.com) on your machine and ensure it is running.

#### Setup Steps
1. Open your terminal in the project root directory (`ConvertX/`).
2. Build and launch both the frontend and backend containers in the background simultaneously by running:
   ```bash
   docker compose up --build -d
   ```
3. Open your web browser and access the application at:
   - **Frontend UI**: `http://localhost:5173`
   - **Backend API Docs**: `http://localhost:5000/docs`

#### Managing the Docker Containers
- **View logs**: `docker compose logs -f`
- **Stop the app**: `docker compose down`
- **Stop and wipe volume caches**: `docker compose down -v`

---

### 🛠️ Method 2: Manual Setup (Without Docker)
If you prefer not to use Docker, you must install all the individual platform prerequisites natively on your operating system.

#### Prerequisites
- **Python 3.11+**
- **Node.js 18+**
- **LibreOffice** (Must be installed locally and added to your system environment variables path)

#### 1. Backend Manual Setup
```bash
cd backend

# Create a virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Linux/macOS)
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt

# Run the local server
uvicorn app.main:app --reload
```
*The local manual backend runs at `http://localhost:5000` (or your configured port).*

#### 2. Frontend Manual Setup
Before starting, create a `.env` file inside your frontend directory (`ConvertX/`) containing your backend URL:
```env
VITE_API_URL=http://localhost:5000
```

Then run the following commands:
```bash
cd ConvertX

# Install npm libraries
npm install

# Start Vite dev server
npm run dev
```
*The local frontend runs at `http://localhost:5173`.*

---

## 📦 Supported Conversions

| Input Format | Output Format |
|:---|:---|
| PDF | DOCX |
| DOCX | PDF |
| JPG / PNG | PDF |
| CSV | XLSX |
| XLSX | PDF |

*Note: Cross-family file conversions (such as changing an Excel spreadsheet `.xlsx` directly into a Word document `.docx`) are not supported.*

## 🔒 File Security

- Uploaded files are stored temporarily.
- Converted files are automatically deleted after a configurable time.
- No permanent file storage is used.

## 📌 Future Improvements

- Drag-and-drop uploads
- Batch file conversion
- User authentication
- Cloud storage integration
- Conversion history
- Progress tracking

## 📄 License

This project is licensed under the MIT License.

---
Built with ❤️ using React, FastAPI, and Python.
