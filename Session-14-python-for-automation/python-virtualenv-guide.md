#  Python Virtual Environments & Dependency Management

A **Python virtual environment** is an isolated workspace that allows you to install and manage dependencies for different projects **without conflicts**.

With virtual environments, each project can have its own dependencies, independent of the global Python installation.

---

##  Benefits of Virtual Environments
- Keep packages isolated.  
- Prevent version conflicts.  
- Manage different dependencies for different projects.  

---

##  Creating a Virtual Environment

Run:

```bash
python -m venv myenv
```

This will create a folder named `myenv` containing a fully isolated Python environment.

---

## ▶ Activating the Virtual Environment

### On Windows (Command Prompt / PowerShell):
```bash
myenv\Scripts\activate
```

Once activated, you can install dependencies such as:

```bash
pip install requests flask
```

### On Linux / macOS / WSL:
```bash
source myenv/bin/activate
```

### Deactivate:
```bash
deactivate
```

---

##  Advanced Dependency Management with Pipenv

[Pipenv](https://pipenv.pypa.io/en/latest/) combines `pip` and `virtualenv` to simplify dependency management.

### Benefits:
- Tracks dependencies in **Pipfile** and **Pipfile.lock**.  
- Simplifies version control.  
- Makes project sharing easier.  

### Installation:
```bash
pip install pipenv
```

### Install Dependencies:
```bash
pipenv install requests
```

This automatically creates a virtual environment and generates `Pipfile` and `Pipfile.lock`.

### Activate Environment:
```bash
pipenv shell
```

Any command you run inside this shell will use the virtual environment.

---

##  Using Pipenv on WSL (Ubuntu/Linux)

1. Update system packages:
   ```bash
   sudo apt update
   ```
2. Install Pipenv:
   ```bash
   sudo apt install pipenv
   ```
3. Verify installation:
   ```bash
   pipenv --version
   ```
4. Create a virtual environment from requirements:
   ```bash
   pipenv install -r requirements.txt
   ```

---

 Now you can manage your Python dependencies easily and avoid conflicts between projects!
