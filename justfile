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
