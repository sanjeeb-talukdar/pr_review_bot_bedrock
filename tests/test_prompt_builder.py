def test_prompt_building():
    from utils.prompt_builder import build_prompt
    prompt = build_prompt("use snake_case", "diff --git a/main.py b/main.py")
    assert "=== CODING GUIDELINES ===" in prompt
    assert "=== PULL REQUEST DIFF ===" in prompt
