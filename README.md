# ConvertX

ConvertX is a modern web-based file conversion platform that allows users to quickly convert files between multiple formats. It features a React frontend and a FastAPI backend, providing a fast, responsive, and user-friendly experience.

## ✨ Features

- 📄 PDF to DOCX
- 📄 DOCX to PDF
- 🖼️ Image (JPG/PNG) to PDF
- 🖼️ JPG to PNG
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

```
ConvertX/
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   ├── uploads/
│   ├── outputs/
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- LibreOffice
- Git

### Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

## 🔧 Environment Variables

Frontend (`.env`)

```env
VITE_API_URL=http://localhost:8000
```

## 📦 Supported Conversions

| Input | Output |
|--------|--------|
| PDF | DOCX |
| DOCX | PDF |
| JPG/PNG | PDF |
| CSV | XLSX |
| XLSX | PDF |

## 🔒 File Security

- Uploaded files are stored temporarily.
- Converted files are automatically deleted after a configurable time.
- No permanent file storage is used.

## 🐳 Docker Support

The backend can be containerized using Docker.

```bash
docker build -t convertx-backend .

docker run -p 8000:8000 convertx-backend
```

## 📌 Future Improvements

- Drag-and-drop uploads
- Batch file conversion
- User authentication
- Cloud storage integration
- Conversion history
- Progress tracking
- Additional file formats

## 📄 License

This project is licensed under the MIT License.

---

Built with ❤️ using React, FastAPI, and Python.
