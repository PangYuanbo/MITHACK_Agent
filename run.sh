python3 -m venv path/to/venv
source path/to/venv/bin/activate

virtualenv -p $(which python3) path/to/venv
# python3 -m uvicorn MITHACK_Agent.main:app --host 8080
#python3 main.py
fastapi dev main.py 