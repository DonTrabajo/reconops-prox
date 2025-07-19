# 🚀 ReconOps Prox

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Alpha-yellow)

**Prox Offensive ReconOps Prox** is an AI-powered agent toolkit designed to analyze recon data (e.g., linPEAS, Nmap) and generate actionable findings, command suggestions, and markdown reports.

---

## 🧠 Features

- 🔍 Parse `linPEAS` JSON output
- 🌐 Analyze `Nmap` XML scan results
- 🎯 Recommend follow-up commands for exploitation
- 📄 Generate Markdown-based recon reports
- 🧠 (Optional) Match recon fingerprints to known APT tactics
- 🤖 Deployable as a ChatGPT Agent using `agent_manifest.yaml`

---

## 📦 Folder Structure

```
reconops_prox/
├── agent_manifest.yaml
├── don_trabajo_gpt/
├── functions/
├── templates/
├── examples/
├── test_runner.py
├── requirements.txt
├── launch_recon.bat
├── deploy_recon_agent.bat
└── .gitignore
```

---

## 🚀 Quick Start (Local)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the test suite
python test_runner.py
```

Or simply double-click: `launch_recon.bat`

---

## 🤖 Deploy as GPT Agent

1. Zip the contents of this folder
2. Go to: [https://chat.openai.com/gpts/editor](https://chat.openai.com/gpts/editor)
3. Upload `agent_manifest.yaml` and the zip file
4. Enable tool calling to activate functions

---

## 📂 Example Inputs

- `examples/linpeas_output.json`
- `examples/nmap_output.xml`

Modify these to test your own recon artifacts.

---

## 🛡 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

**Built by Prox Offensive (Don Trabajo GPT Labs)**  
💻 [proxoffensive.com](https://proxoffensive.com)  
🔬 Crafted with tactical AI wizardry and terminal green love.

