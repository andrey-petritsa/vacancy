from flask import Blueprint, jsonify, request

from ui.short_vacancy_card import ShortVacancyCard
from ui.vacancy_card import VacancyCard
from details.utils import command_registry

bp = Blueprint("routes", __name__)


@bp.route("/api/health_check", methods=["GET"])
def health_check():
    return jsonify(True)

@bp.route("/api/show_vacancies_cards", methods=["GET"])
def show_vacancies_cards():
    search_query = request.args.to_dict()
    token = request.headers.get('X-TOKEN')
    vacancies = command_registry.show_vacancies_command.execute(search_query, token)
    vacancies_cards = [VacancyCard.show(vacancy) for vacancy in vacancies]
    return jsonify(vacancies_cards=vacancies_cards)

@bp.route("/api/show_short_vacancies_cards", methods=["GET"])
def show_short_vacancies_cards():
    search_query = request.args.to_dict()
    token = request.headers.get('X-TOKEN')
    vacancies = command_registry.show_vacancies_command.execute(search_query, token)
    vacancies_cards = [ShortVacancyCard.show(vacancy) for vacancy in vacancies]
    return jsonify(short_vacancies_cards=vacancies_cards)


@bp.route("/api/generate_cover_latter", methods=["POST"])
def generate_cover_letter():
    request_data = request.json
    token = request.headers.get('X-TOKEN')
    vacancy = {
        'text':request_data['text']
    }

    cover_latter = command_registry.generate_cover_latter_command.execute(vacancy, token)
    return jsonify(cover_latter=cover_latter)


@bp.route("/api/change_vacancy_status", methods=["POST"])
def change_vacancy_status():
    vacancy_id = request.json.get('vacancy_id')
    vacancy_status = request.json.get('vacancy_status')
    token = request.headers.get('X-TOKEN')
    command_registry.change_vacancy_status_command.execute(vacancy_id, vacancy_status, token)
    return '', 200


@bp.route("/api/show_user/<user_token>", methods=["GET"])
def show_user(user_token):
    user = command_registry.show_user_command.execute(user_token)
    return jsonify(user=user)
