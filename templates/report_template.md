# Prox Offensive Recon Report

**Target System:** {{ target }}

**Top Findings:**
{% for f in findings %}
- **{{ f.name }}**  
  {{ f.description }}  
  Severity: {{ f.severity }}
{% endfor %}

**Suggested Commands:**
{% for cmd in commands %}
- `{{ cmd }}`
{% endfor %}
