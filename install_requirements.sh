# Step 1: Create a virtual environment
python3 -m venv path/to/venv

# Step 2: Activate the virtual environment
source path/to/venv/bin/activate

virtualenv -p $(which python3) path/to/venv

# Step 3: Update the PATH (This is for Anaconda, so if you're not using it in your virtual environment, you can skip this)
export PATH="/opt/homebrew/anaconda3/bin:$PATH"

# Step 4: Install the required Python packages
pip install fastapi[standard]
pip install uvicorn[standard]
pip install httpx[standard]
pip install uagents
pip install google
pip install google-cloud
pip install protobuf
pip install openai

