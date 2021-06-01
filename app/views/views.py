from flask import jsonify, request
from app.services.services import KenzieSerieServices


def register_views(app):

    @app.route("/")
    def home():
        return {"msg": "homepage"}, 200

    @app.route("/series", methods=["POST"])
    def create():
        serie_to_create = request.get_json()
        res = KenzieSerieServices.insert_table(serie_to_create)

        if not res:
            return {"msg": "Cannot contain null fields"}, 400

        return jsonify(res), 201
 
    @app.route("/series", methods=["GET"])
    def series():
        res = KenzieSerieServices.select_table()

        return {"data": res}, 200

    @app.route("/series/<int:serie_id>")
    def select_by_id(serie_id):
        res = KenzieSerieServices.select_table_by_id(serie_id)

        if not res:
            return {"error": "Not Found"}, 404


        return {"data": res}, 200