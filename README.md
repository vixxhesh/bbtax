# SpiderWeb

## Overview

**SpiderWeb** is a full-stack Django web application designed to manage blogs, appointments, contacts, and resources. This project provides an admin panel for authorized users to manage various aspects of the application and allows general users to interact with the blog and resource management functionalities.

## Features

- **Blog Management**: Users can create, read, update, and delete blog posts.
- **Appointment Scheduling**: Allows users to schedule appointments through a form.
- **Contact Management**: Stores and manages user contact information.
- **Resource Store**: Authorized users can upload PDF and Word files, while all users can download them.
- **Admin Panel**: Accessible only by authenticated users, enabling management of all models in the app.
- **Rich Text Editing**: Blog content supports rich-text editing via TinyMCE.
- **Search Functionality**: Users can search for resources in the resource store by keywords.

## Project Structure

- **Blog**: Manage blog posts and content.
- **Appointments**: Schedule and manage appointments.
- **Contact**: Store and manage contact messages from users.
- **Resource Store**: Upload and download important files.
- **Admin Panel**: Manage all aspects of the application through a protected interface.

## Tech Stack

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django, Python
- **Database**: SQLite (default), PostgreSQL (optional)
- **Rich Text Editor**: TinyMCE
- **Deployment**: Heroku

## Installation

### Prerequisites

- Python 3.x
- Django 3.2+
- Virtualenv
- PostgreSQL (optional, for production)
- Git

### Clone the Repository

```bash
git clone https://github.com/your-username/spiderweb.git
cd spiderweb
