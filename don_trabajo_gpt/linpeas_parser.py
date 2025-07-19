def extract_findings(json_data):
    import json
    data = json.loads(json_data)
    return [{"name": p, "description": "Process found", "severity": "info"} for p in data.get("Processes", [])]
