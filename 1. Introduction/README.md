# FastAPI Minimal Application

## Installation

1. **Clone or download this repository and open the folder path**
2. **Create and activate a virtual environment (optional but recommended):**
   
   On Windows:
   ```bash
   python -m venv .env
   .env\Scripts\activate
   ```
   On macOS/Linux:
   ```bash
   python3 -m venv .env
   source .env/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```

## Running the Application

Start the server with:
```bash
uvicorn main:app --reload
```

- The API will be available at: http://127.0.0.1:8000/
- Interactive API docs: http://127.0.0.1:8000/docs

## Endpoints
- `GET /` — Returns a welcome message.
- `GET /items/{item_id}` — Retrieve an item by its ID, with optional query parameter `q`.

## Deactivating and Closing the Project

To deactivate the virtual environment:

- On Windows:
   ```bash
   deactivate
   ```
- On macOS/Linux:
   ```bash
   deactivate
   ```

To close the project, simply close your terminal and code editor.
