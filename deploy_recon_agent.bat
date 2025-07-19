@echo off
cd /d %~dp0
echo ===============================
echo Prox Offensive ReconOps Deployer
echo ===============================

echo.
echo [1/3] Installing Python dependencies...
pip install -r requirements.txt

echo.
echo [2/3] Running test suite to validate modules...
python test_runner.py

echo.
echo [3/3] Preparing for GPT Agent deployment...
echo (Manual step) Zip this folder and upload it at: https://chat.openai.com/gpts/editor
echo Agent manifest: agent_manifest.yaml
echo Decorated functions: functions/
echo

pause
