from nueraflow_ai.memory import MemoryStore


def test_memory_add_and_search(tmp_path):
    store = MemoryStore(str(tmp_path / "memory.sqlite3"))
    memory_id = store.add("Use Python for the first Nueraflow prototype", "test")
    assert memory_id == 1
    results = store.search("Nueraflow prototype")
    assert len(results) == 1
    assert results[0]["source"] == "test"
