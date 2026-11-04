import requests


def test_main_page():
    url = "https://xenoss.io"
    response = requests.get(url)
    assert response.status_code == 200
    assert "text/html" in response.headers.get("Content-Type", "")
    assert "xenoss" in response.text
    assert "AI and data engineering services for enterprises" in response.text
    
    
def test_links():
    capabilities_url = "https://xenoss.io/capabilities"
    capabilities = ["/data-engineering", "/generative-ai",
                    "/predictive-modeling", "/data-migration",
                    "/fine-tuning-llm"]
    solutions_url = "https://xenoss.io/solutions"
    solutions = ["/enterprise-multi-agent-systems",
                 "/enterprise-llm-knowledge-management",
                 "/enterprise-hyperautomation-systems"]
    for capability in capabilities:
        response = requests.get(capabilities_url + capability)
        assert response.status_code == 200
    for solution in solutions:
        response = requests.get(solutions_url + solution)
        assert response.status_code == 200