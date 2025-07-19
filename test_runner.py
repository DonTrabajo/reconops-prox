import json
from functions.parse_linpeas import parse_linpeas
from functions.parse_nmap import parse_nmap
from functions.generate_report import generate_report
from functions.suggest_commands import suggest_commands
from functions.match_apt_profile import match_apt_profile

with open("examples/linpeas_output.json") as f:
    linpeas_data = f.read()
with open("examples/nmap_output.xml") as f:
    nmap_data = f.read()

linpeas_result = parse_linpeas(linpeas_data)
nmap_result = parse_nmap(nmap_data)
report = generate_report(linpeas_result)
commands = suggest_commands(nmap_result)
apt_match = match_apt_profile(nmap_result)

print("=== Parsed linPEAS ===")
print(json.dumps(linpeas_result, indent=2))
print("=== Parsed Nmap ===")
print(json.dumps(nmap_result, indent=2))
print("=== Suggested Commands ===")
print(json.dumps(commands, indent=2))
print("=== APT Profile Match ===")
print(json.dumps(apt_match, indent=2))
print("=== Report ===")
print(report["report_markdown"])
