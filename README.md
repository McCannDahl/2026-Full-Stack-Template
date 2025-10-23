# 2026-Full-Stack-Template
how I like to start projects: CDK w/ SAM API, Alembic DB management, Flutter frontend

backend
```
cd backend
source ./.venv/Scripts/activate
python -m pip install -r requirements.txt
docker info
cdk synth
sam local start-api -t cdk.out/BackendStack.template.json -d 5858
```

# TODO
- [ ] gety debugger working