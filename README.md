
# MyCV - Personal Portfolio & Interactive Resume

A dynamic, web-based CV and portfolio application built using Python (Flask), HTML5, CSS3, and JavaScript. It showcases professional experience, technical skills, projects, and educational background in a clean, responsive layout.

---

## Features

- **Interactive Layout:** Modular view separating the home introduction and detailed CV presentation.
- **Responsive Design:** Optimized with modern CSS for both desktop and mobile screens.
- **Dynamic Frontend:** Interactive UI components handled by vanilla JavaScript (`main.js`).
- **Python Backend:** Lightweight Flask backend serving templates and routing requests.

---

## Project Structure

```text
├── app.py             # Flask application server and route definitions
├── base.html          # Base layout template
├── cv.html            # Detailed curriculum vitae / resume page
├── index.html         # Landing page / overview
├── main.js            # Client-side scripts and interactive behavior
├── photo.png          # Profile picture asset
├── requirement.txt    # Python package dependencies
└── style.css          # Styling and responsive design rules

```

---

## Getting Started

### Prerequisites

* Python 3.8 or higher
* `pip` (Python package manager)

### Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/himadritsahu-20/mycv.git](https://github.com/himadritsahu-20/mycv.git)
cd mycv

```


2. **Create and activate a virtual environment (optional but recommended):**
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirement.txt

```


4. **Run the application:**
```bash
python app.py

```


5. Open your web browser and navigate to:
```text
http://127.0.0.1:5000/

```



---

## Customization

* **Update Personal Details:** Edit `index.html` and `cv.html` to update your experience, projects, education, and contact links.
* **Profile Photo:** Replace `photo.png` with your own image (keeping the same filename or updating the image path in the HTML templates).
* **Styles & Themes:** Adjust colors, typography, and spacing in `style.css`.

---

## License

This project is open-source and available under the MIT License.

