from functions.decorator import tool

@tool(name="match_apt_profile", description="Match recon patterns to known APT groups")
def match_apt_profile(parsed_data: dict) -> dict:
    if "open_ports" in parsed_data and 3389 in parsed_data["open_ports"]:
        return {"apt_match": "Possible RDP targeting behavior (APT33-like)"}
    return {"apt_match": "No strong match found"}
