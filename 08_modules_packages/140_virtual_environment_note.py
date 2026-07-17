print("""
A virtual environment isolates project dependencies.

Create a virtual environment:
    python -m venv venv

Activate (Windows):
    venv\\Scripts\\activate

Activate (macOS/Linux):
    source venv/bin/activate

Deactivate:
    deactivate

After activating, pip installs packages only inside the venv.

Install dependencies:
    pip install requests

Save:
    pip freeze > requirements.txt

Share your project:
    Others run:  pip install -r requirements.txt
""")
