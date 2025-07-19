from functions.decorator import tool
from jinja2 import Template

@tool(name="generate_report", description="Generate markdown report from findings")
def generate_report(data: dict) -> dict:
    findings = data.get("findings", [])
    template_str = """# Prox Offensive Recon Report

**Findings:**
{% for f in findings %}
- **{{ f.name }}** - {{ f.description }} (Severity: {{ f.severity }})
{% endfor %}
"""
    template = Template(template_str)
    report_md = template.render(findings=findings)
    return {"report_markdown": report_md}
