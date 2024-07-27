CRM project

Overview
-CRM is a customer relationship management (CRM) system built with Django. It helps manage leads, clients, and teams efficiently, providing a streamlined interface for users to interact with their CRM data.

Features
    -User Authentication and Profile Management
    -Team Management
    -Lead Management (Add, Edit, Delete, Convert to Client)
    -Client Management
    -Dashboard with Recent Leads and Clients
    -Responsive Design with Tailwind CSS

Tech Stack
    -Backend: Django 5.0.6
    -Frontend: HTML, CSS, Tailwind CSS
    -Database: SQLite (default)

Usage
    -Log in with your superuser account.
    -Create and manage teams.
    -Add and manage leads.
    -Convert leads to clients.
    -View recent leads and clients on the dashboard.

Requirements
    Python 3.12.4
    Django 5.0.6
    Tailwind CSS v3.0

Project Structure
CRM_Project/
├── client/
├── core/
├── dashboard/
├── lead/
├── team/
├── userprofile/
├── templates/
├── static/
│   ├── css/
│   │   └── output.css
│   └── src/
│       └── input.css
├── manage.py
├── package.json
├── requirements.txt
├── tailwind.config.js
├── README.md
