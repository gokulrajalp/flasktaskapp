from flask import Blueprint, request, jsonify
from services.auth_service import signup_service, login_service

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():

    response, status = signup_service(request.json)

    return jsonify(response), status


@auth_bp.route("/login", methods=["POST"])
def login():
    """
    User Login
    ---
    tags:
      - Authentication

    parameters:
      - in: body
        name: body
        schema:
          type: object

          properties:

            username:
              type: string

            password:
              type: string

    responses:

      200:
        description: Login Success
    """
    response, status = login_service(request.json)

    return jsonify(response), status
