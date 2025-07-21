# weird_thought_process

A web-based blogging application designed to encourage and capture unconventional, creative, and free-flowing ideas.

---

## Table of Contents
* [About](#about)
* [Features](#features)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Accessing the App](#accessing-the-app)
* [Project Structure](#project-structure)
* [Technologies Used](#technologies-used)
* [Contributing](#contributing)
* [License](#license)
* [Author](#author)

---

## About
The `weird_thought_process` project is an open-source web application that serves as a platform for users to share and catalog creative, quirky, or "weird" thoughts as blog entries. The goal is to encourage free thought, spark conversation, and provide a dedicated space for unique perspectives that may not find a home on mainstream platforms.

Ideal for students, writers, or anyone who loves to let their thoughts wander, `weird_thought_process` transforms random musings into shareable content.

---

## Features
* **User authentication** and account management.
* Ability to **write, edit, and delete blog posts**.
* **Browse and view posts** from all users.
* **Admin controls** for managing content and user activity.
* **Responsive and modern** user interface.

---

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
* **Python** (recommended version: 3.x)
* **pip** (Python package installer)
* **Virtualenv** (optional, but highly recommended for managing dependencies)

### Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/dilip9398/weird_thought_process.git](https://github.com/dilip9398/weird_thought_process.git)
    cd weird_thought_process
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up the database:**
    ```bash
    python manage.py migrate
    ```

4.  **Create a superuser** (for admin access):
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

### Accessing the App
Open your web browser and navigate to: `http://127.0.0.1:8000/`

---

## Project Structure
| Directory/File    | Purpose                                     |
|-------------------|---------------------------------------------|
| `accounts/`       | User authentication & account logic         |
| `weird_blog/`     | Blog app, posts, views, templates           |
| `wb_project/`     | Project-level configuration and settings    |
| `staticfiles/`    | Static assets (CSS, JS, images)             |
| `admin/`          | Admin interface files                       |
| `.platform/`      | Platform.sh deployment configurations (if used) |
| `manage.py`       | Django's command-line utility               |


---

## Technologies Used
* **Django** (Python web framework)
* **JavaScript**
* **CSS**
* **HTML**

---

## Contributing
Contributions are warmly welcomed! If you have an idea for a new feature, a bug fix, or any other improvement, please feel free to:
1.  **Open an issue** to discuss your proposed changes.
2.  **Submit a pull request** with your contributions.

---

## License
This project is open-source and released under the **MIT License**. See the `LICENSE` file for more details.

---

## Author
Created and maintained by **dilip9398**.

Feel free to star or fork the repository to show your support or to start contributing!
