from functions.decorator import tool

@tool(name="suggest_commands", description="Suggest follow-up commands based on findings")
def suggest_commands(parsed_data: dict) -> dict:
    commands = []
    if "open_ports" in parsed_data:
        for port in parsed_data["open_ports"]:
            commands.append(f"nmap -sV -p {port} <target>")
    return {"commands": commands}
