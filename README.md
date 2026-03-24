# Sticky Notes Application

A Django-based CRUD application for creating, viewing, editing,
and deleting colour-coded sticky notes.

---

## Table of Contents

- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Setup](#setup)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
  - [3. Activate the Virtual Environment](#3-activate-the-virtual-environment)
  - [4. Install Dependencies](#4-install-dependencies)
  - [5. Apply Migrations](#5-apply-migrations)
  - [6. Run the Development Server](#6-run-the-development-server)
- [Running Tests](#running-tests)
- [Linting with Flake8](#linting-with-flake8)
- [Deactivating the Virtual Environment](#deactivating-the-virtual-environment)
- [Generating a Requirements File](#generating-a-requirements-file)

---

## Requirements

- Python 3.12 or higher
- pip

---

## Project Structure

```
sticky_notes/
├── manage.py
├── .flake8
├── requirements.txt
├── README.md
├── sticky_notes/          # Project config directory
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── notes/                 # Notes app
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── admin.py
    ├── apps.py
    ├── tests.py
    └── urls.py
```

---

## Setup

### 1. Clone the Repository

---

### 2. Create a Virtual Environment

**Windows:**
```bash
python -m venv .venv
```

**macOS / Linux:**
```bash
python3 -m venv .venv
```
---

### 3. Activate the Virtual Environment

**Windows (Command Prompt):**
```bash
.venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

Once activated, your terminal prompt will show `(.venv)` at the start,
confirming the environment is active.

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all packages listed in `requirements.txt`, including
Django and any other dependencies.

---

### 5. Apply Migrations

```bash
python manage.py migrate
```

This creates the database tables for all installed apps, including
the `Note` model.

---

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to:

```
http://127.0.0.1:8000/
```

---

## Running Tests

Run the full test suite from the project root:

```bash
python manage.py test notes
```

To see a more detailed output:

```bash
python manage.py test notes --verbosity=2
```

---

## Linting with Flake8

Lint the entire project:

```bash
flake8 .
```

Lint a specific app or file:

```bash
flake8 notes/
flake8 notes/views.py
```

Configuration is defined in `.flake8` at the project root.

---

## Deactivating the Virtual Environment

When you are done working, deactivate the virtual environment:

```bash
deactivate
```
