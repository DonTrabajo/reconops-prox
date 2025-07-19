from functions.decorator import tool
import xmltodict

@tool(name="parse_nmap", description="Parse Nmap XML and list open ports")
def parse_nmap(xml_data: str) -> dict:
    doc = xmltodict.parse(xml_data)
    ports = []
    try:
        port_data = doc["nmaprun"]["host"]["ports"]["port"]
        if isinstance(port_data, list):
            ports = [int(p["@portid"]) for p in port_data if p["state"]["@state"] == "open"]
        else:
            ports = [int(port_data["@portid"])]
    except Exception as e:
        return {"error": str(e)}
    return {"open_ports": ports}
