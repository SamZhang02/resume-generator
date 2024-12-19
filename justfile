set dotenv-load

default:
  just --list

fmt:
  black .

install-deps:
    echo "Installing from requirements.txt..."
    venv/bin/pip3 install -r requirements.txt

install args:
  echo "Installing {{args}}..."
  venv/bin/pip3 install {{args}}
  echo "Updating requirements.txt..."
  venv/bin/pip3 freeze > requirements.txt

run args:
  venv/bin/python3 -m {{args}}

demo:
  venv/bin/python3 -m App.app --data_path info.json --out_path sam_zhang_resume.tex --format_tex
