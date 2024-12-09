# React FastAPI AI Application

A full-stack application built with React frontend, FastAPI backend, Firebase integration, and OpenAI capabilities.

## Project Structure

```
.
├── frontend/          # React frontend application
├── backend/           # FastAPI backend application
├── docs/              # Documentation
└── README.md
```

## Getting Started

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
npm install
npm start
```

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Environment Variables

Create `.env` files in both frontend and backend directories. See `.env.example` files for required variables.

## Features

- React frontend with modern UI/UX
- FastAPI backend for efficient API handling
- Firebase integration for authentication and database
- OpenAI integration for AI capabilities

## Contributing

Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details