From python:3.14.5-slim
workdir /app
copy requirement.txt .
run pip install -r requirement.txt
copy . . 
cmd ["uvicorn","main:app"]