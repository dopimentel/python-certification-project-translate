import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    history_list = json.loads(HistoryModel.list_as_json())
    assert history_list[0]["text_to_translate"] == "Hello, I like videogame"
    assert history_list[0]["translate_from"] == "en"
    assert history_list[0]["translate_to"] == "pt"
    assert history_list[1]["text_to_translate"] == "Do you love music?"
    assert history_list[1]["translate_from"] == "en"
    assert history_list[1]["translate_to"] == "pt"
    assert len(history_list) == 2
