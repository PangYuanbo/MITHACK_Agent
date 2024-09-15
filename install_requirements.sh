python3 -m venv path/to/venv
source path/to/venv/bin/activate

export PATH="/opt/homebrew/anaconda3/bin:$PATH"
python3 -m pip install google.protobuf.timestamp_pb2

python3 -m pip install fastapi[standard]
python3 -m pip install uvicorn[standard]
python3 -m pip install httpx[standard]
python3 -m pip install uagents
python3 -m pip install protobuf

python3 -m pip install openai