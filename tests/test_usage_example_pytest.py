from custom_python_logger.usage_example import main


def test_usage_example_runs(monkeypatch):
    # Patch print and time.sleep to avoid side effects
    monkeypatch.setattr("builtins.print", lambda *a, **k: None)
    monkeypatch.setattr("time.sleep", lambda x: None)
    main()  # Should not raise
