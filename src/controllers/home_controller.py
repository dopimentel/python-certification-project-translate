from bson import ObjectId
from flask import Blueprint, jsonify, render_template, request
from models.history_model import HistoryModel
from models.user_model import UserModel
from models.language_model import LanguageModel

home_controller = Blueprint("home_controller", __name__)


@home_controller.route("/", methods=["GET"])
def home():
    languages = LanguageModel.list_dicts()
    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )
