#!/bin/bash

# Create a virtual environment
python3.9 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Build the project
echo "Building the project..."
pip install -r requirements.txt

python3.9 -c "import ssl; print(ssl.OPENSSL_VERSION)"

echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear