import pytest
from nueraflow_ai.knowledge import KnowledgeSource


def test_source_requires_http_url():
    with pytest.raises(ValueError):
        KnowledgeSource("Example", "file:///etc/passwd", "document").validate()


def test_source_accepts_https():
    KnowledgeSource("Python docs", "https://docs.python.org/3/", "documentation").validate()
