# 🧭 Travel Planner API

A backend service for managing travel projects and destinations, integrated with the **Art Institute of Chicago API**

---

## 🚀 Features

### 📁 Travel Projects

* Create a project (with the option to add places immediately)
* Update a project (name, description, start_date)
* Delete a project

  * But cannot be deleted if it contains visited places
* Get a list of projects
* Get a single project

---

### 📍 Places

* Add a place to a project
* Update a place:

  * notes (`notes`)
  * visit status (`visited`)
* Get a list of places in a project
* Get a specific place

---

## 🌐 Integration

The service uses:

* **Art Institute of Chicago API**

Example:

```
GET https://api.artic.edu/api/v1/artworks/{id}
```

👉 `external_id` = artwork ID from this API

---

## 🏗️ Architecture

The project follows a layered architecture:

```
Router → Service → Repository → Database
```

```
app/
├── routers/        # HTTP endpoints
├── services/       # business logic
├── repositories/  # database access
├── models/        # SQLAlchemy models
├── schemas/       # Pydantic schemas
├── integrations/  # external APIs
└── core/          # configuration (database)
```

---

## ⚙️ Технологии

* FastAPI
* SQLAlchemy
* SQLite
* httpx (for API requests)

---

## ▶️ Running the Project

### 1. Clone the repository

```bash
git clone <repo_url>
cd travel-planner
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

---


## 📌 Example Requests

### Create a project

```json
POST /projects/

{
  "name": "My Trip",
  "description": "Chicago Art Tour",
  "start_date": "2026-04-01"
}
```

---

### Add a place

```json
POST /projects/1/places/

{
  "external_id": 129884
}
```

---

### Update a place

```json
PATCH /projects/1/places/1

{
  "visited": true,
  "notes": "Amazing artwork!"
}
```

---

## ⚠️ Limitations

* Maximum 10 places per project
* Cannot add the same place twice
* Cannot delete a project if it contains visited places
* All places are validated via the external API

---

## 🧠 Implementation Details

* Asynchronous requests to the external API
* Clear separation of layers (Repository / Service / Router)
* Data validation with Pydantic
* Working with external IDs (external_id)

---

## 

The README file was written by ChatGPT.
