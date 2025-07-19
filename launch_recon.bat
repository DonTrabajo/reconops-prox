@echo off
cd /d %~dp0
echo Installing Python dependencies...
pip install -r requirements.txt

echo Running ReconOps Prox test...
python test_runner.py

pause
