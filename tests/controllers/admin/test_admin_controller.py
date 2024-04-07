from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    UserModel({"name": "Peter", "token": "token_secreto12"}).save()
    history = HistoryModel.find_one()
    if history is not None:
        response = app_test.delete(
            f"admin/history/{str(history.data['_id'])}",
            headers={"Authorization": "token_secreto12", "User": "Peter"},
        )

        assert response.status_code == 204


def test_history_delete_not_found(app_test):
    UserModel({"name": "Peter", "token": "token_secreto12"}).save()
    response = app_test.delete(
        "admin/history/5f4f4f4f4f4f4f4f4f4f4f4f",
        headers={"Authorization": "token_secreto12", "User": "Peter"},
    )

    assert response.status_code == 404


def test_history_delete_unauthorized(app_test):
    UserModel({"name": "Peter", "token": "token_secreto12"}).save()
    history = HistoryModel.find_one()
    if history is not None:
        response = app_test.delete(
            f"admin/history/{str(history.data['_id'])}",
            headers={"Authorization": "token_secreto", "User": "Peter"},
        )

        assert response.status_code == 401
