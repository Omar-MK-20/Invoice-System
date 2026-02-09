# Invoice System

A full-stack invoice management application with a **FastAPI** backend and a **React + TypeScript + Vite** frontend. It lets you manage customers, cars, services, and create detailed invoices.

---

## Project Description

The **Invoice System** is a web application for creating and managing invoices. It supports:

- **Customers** – Store and manage customer information
- **Cars** – Link cars to customers
- **Services** – Define services that can be added to invoices
- **Invoices** – Create invoices with multiple line items (services), linked to customers and cars

The backend exposes a REST API (FastAPI + SQLAlchemy) and uses a **MySQL** database. The frontend is a single-page app (React, React Router, HeroUI, Tailwind CSS) that consumes this API.

---

## Folder Structure

```
Invoice-System/
├── Backend/
│   ├── .env                    # Environment variables (DATABASE_URL, etc.) — create from template below
│   ├── requirements.txt        # Python dependencies
│   ├── query.sql               # SQL scripts (if any)
│   └── server/
│       ├── main.py             # FastAPI app entry point
│       ├── DB/
│       │   └── connection.py    # Database connection and session
│       ├── Models/             # SQLAlchemy models
│       │   ├── CarModel.py
│       │   ├── CustomerModel.py
│       │   ├── InvoiceModel.py
│       │   ├── InvoiceItemModel.py
│       │   └── ServiceModel.py
│       ├── Routers/            # API route handlers
│       │   ├── car.py
│       │   ├── customer.py
│       │   ├── invoice.py
│       │   └── service.py
│       ├── Schemas/            # Pydantic request/response schemas
│       │   ├── CarSchema.py
│       │   ├── CustomerSchema.py
│       │   ├── InvoiceSchema.py
│       │   └── ServiceSchema.py
│       └── Services/           # Business logic
│           ├── CarService.py
│           ├── CustomerService.py
│           ├── InvoiceService.py
│           └── ServiceService.py
├── Frontend/
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.ts
│   ├── index.html
│   ├── public/
│   └── src/
│       ├── main.tsx
│       ├── App.tsx
│       ├── index.css
│       ├── components/         # Reusable UI (e.g. NavBar)
│       ├── interfaces/         # TypeScript types
│       ├── pages/              # Route pages (Home, Invoices, CreateInvoice, etc.)
│       └── schemas/            # Validation (e.g. Zod)
├── Database/                   # ERD and schema diagrams
│   ├── ERD.drawio
│   ├── ERD.drawio.png
│   ├── Schema.drawio
│   └── Schema.drawio.png
└── README.md
```

---

## Backend Setup & Run

### 1. Create and activate a virtual environment

From the project root:

**Windows (PowerShell):**
```powershell
cd Backend
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
cd Backend
python -m venv venv
venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
cd Backend
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

With the virtual environment activated (you should see `(venv)` in the prompt):

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a file **`Backend/.env`** with your MySQL connection string. The app expects a variable named **`DATABASE_URL`**:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/invoice_system_db
```

Replace `username` and `password` with your MySQL user and password. Ensure the database `invoice_system_db` exists (create it in MySQL if needed).

### 4. Run the backend with Uvicorn

From the **`Backend`** directory (with `venv` activated):

```bash
uvicorn server.main:server --reload --host 0.0.0.0 --port 8000
```

- **`server.main:server`** – module `server.main`, FastAPI app instance named `server`
- **`--reload`** – auto-reload on code changes (optional)
- **`--host 0.0.0.0`** – listen on all interfaces (optional)
- **`--port 8000`** – default port; change if needed

API base URL: **http://localhost:8000**. Open **http://localhost:8000/docs** for Swagger UI.

---

## Frontend Setup & Run

### 1. Install dependencies

From the project root:

```bash
cd Frontend
npm install
```

### 2. Run the development server

```bash
npm run dev
```

Vite usually serves the app at **http://localhost:5173**. The frontend is configured to call the backend at `http://localhost:8000` (CORS is set in the backend for this origin).

### Other npm scripts

- **`npm run build`** – Production build
- **`npm run preview`** – Preview production build locally
- **`npm run lint`** – Run ESLint

---

## Quick Start Summary

| Step | Location   | Command / Action |
|------|------------|-------------------|
| 1    | `Backend/` | `python -m venv venv` then activate `venv` |
| 2    | `Backend/` | `pip install -r requirements.txt` |
| 3    | `Backend/` | Create `.env` with `DATABASE_URL=mysql+pymysql://username:password@localhost:3306/invoice_system_db` |
| 4    | `Backend/` | `uvicorn server.main:server --reload --port 8000` |
| 5    | `Frontend/`| `npm install` then `npm run dev` |

Then open **http://localhost:5173** for the app and **http://localhost:8000/docs** for the API docs.
