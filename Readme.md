# ChatApp

A Streamlit-based chat application developed using standard Python application practices. The project focuses on clarity, modular structure, and explicit application flow rather than a single-script approach.


## Overview

ChatApp is a Python web application that provides a chat interface with support for authentication, direct messaging, and group conversations. The application is organized as a modular Python project and uses Streamlit as the UI layer.


## Project Structure

The project follows a clean **src-based layout**, where all application code lives inside the `src/` directory.

ChatApp/
├── src/
│   ├── orchestrator.py      # Application entry point
│   ├── screens/             # Streamlit UI screens
│   ├── db/                  # Database access layer
│   ├── controllers/         # Application controllers / request handlers
│   └── utils/               # Utility functions
├── pyproject.toml           # Project metadata and dependencies
├── README.md                # Project documentation
├── LICENSE                  # MIT License
└── .gitignore               # Git ignore rules


## Technologies Used

* Python 3.10.12
* Streamlit 1.52.1
* Git 2.34.1
* mypy 1.19.1 (optional, for static type checking during development)


## Installation

### 1. Clone the repository

git clone <repository-url>
cd muthukumar.md

### 2. Create and activate a virtual environment (recommended)

#### Linux / macOS

python3 -m venv venv
source venv/bin/activate

#### Windows (Command Prompt)

python -m venv venv
venv\Scripts\activate

#### Windows (PowerShell)

python -m venv venv
venv\Scripts\Activate.ps1

### 3. Install dependencies

pip install .

For development (with type checking support):

pip install .[dev]


## Running the Application

Run the Streamlit application **from inside the `src` directory**.

First move into `src`:

cd src

Then run the Streamlit application:

#### Linux / macOS

streamlit run orchestrator.py

#### Windows

streamlit run orchestrator.py


## Development Notes

* The application follows Python standards such as PEP 8 (code style) and PEP 20 (The Zen of Python).
* `orchestrator.py` acts as the explicit application entry point and controls initialization and page routing.
* The codebase is modularized into UI (`screens`), controller (`controllers`), database access (`db`), and utility (`utils`) layers.
* Using the `src/` directory helps keep application code isolated from project configuration files.


## License

This project is licensed under the MIT License.
See the `LICENSE` file for details.
