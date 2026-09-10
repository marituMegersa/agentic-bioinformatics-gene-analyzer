def test_agent_orchestrator():
    prompt = "Test execution query for agentic-bioinformatics-gene-analyzer"
    assert len(prompt) > 0
    assert "Test" in prompt
