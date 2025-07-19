from functions.decorator import tool
from don_trabajo_gpt.linpeas_parser import extract_findings

@tool(name="parse_linpeas", description="Parse linPEAS JSON and extract key findings")
def parse_linpeas(json_data: str) -> dict:
    return {"findings": extract_findings(json_data)}
