import json
from flask import Blueprint, jsonify
from models.history_model import HistoryModel


history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def history():
    return jsonify({"history": json.loads(HistoryModel.list_as_json())}), 200
