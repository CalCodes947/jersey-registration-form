# 🏏 Cricket Jersey Registration System

A lightweight, interactive Python Command Line Interface (CLI) application designed to automate, validate, and manage sports jersey orders for teams. 

This project was inspired by a real-world scenario—simplifying a chaotic group chat registration process into a structured, error-free data pipeline.

---

## 🚀 Features

* **Persistent CSV Data Storage:** Automatically initializes a `Jersey_data.csv` file with structured headers upon its first run, appending every validated entry in real-time.
* **Robust Input Validation:** 
  * Restricts size selections to standard formats (`S`, `M`, `L`, `XL`, `XXL`, `XXXL`) using case-insensitive normalization.
  * Prevents application crashes due to bad user input by catching numeric formatting errors (`ValueError`) on jersey numbers.
* **Smart State Management (Flag System):** Provides a confirmation screen allowing users to review their details. If they choose to correct a mistake, a local state flag resets the application for that specific entry without breaking the workflow.
* **Multi-Profile Continuous Capture:** Features a loop structure that allows back-to-back registrations for an entire team in a single terminal session.

---

## 🛠️ Tech Stack & Concepts Applied

* **Language:** Python 3.x
* **File I/O:** Built-in `os` and `open()` context managers (`with` statements) for safe file manipulation.
* **Error Handling:** `try-except` blocks for runtime input protection.
* **Control Flow:** Nested validation loops, conditional states (`if/elif/else`), and execution control tokens (`break`, `continue`).

---

## 📦 How It Works (Data Pipeline)

```text
[ Start ] ──> [ Input: Name, Size, Number ] ──> [ Data Validation Loops ]
                                                            │
[ CSV File Saved ] <── [ Confirmed: Yes ] <── [ Review Summary Screen ]
       │                                                    │
[ Next Player? ]                                     [ Confirmed: No ]
  ├── Yes ──> (Loop Restarts)                               │
  └── No  ──> [ Safe Exit ] <───────────────────────────────┘
