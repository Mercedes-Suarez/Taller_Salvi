from flask import Blueprint, request, jsonify
from backend.services.session_tokensServices import (
    get_session_tokens_all, get_session_token_by_id,
    create_session_token, update_session_token, delete_session_token
)
# Blueprint para Session Tokens
session_tokens_bp = Blueprint('session_tokens', __name__)

@session_tokens_bp.route('/session_tokens', methods=['GET'])
def get_session_tokens():
    """Obtiene todos los tokens de sesión."""
    try:
        tokens = get_session_tokens_all()
        return jsonify([{ 
            "id": token.id,
            "user_id": token.user_id,
            "token": token.token,
            "creation_date": token.creation_date.isoformat(),
            "expiration_date": token.expiration_date.isoformat()
        } for token in tokens])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@session_tokens_bp.route('/session_tokens', methods=['GET'])
def get_session_token(token_id):
    try:
        token = get_session_token_by_id(token_id)
        if not token:
            return jsonify({"error": "Token not found"}), 404

        return jsonify({
            "id": token.id,
            "user_id": token.user_id,
            "token": token.token,
            "creation_date": token.creation_date.isoformat(),
            "expiration_date": token.expiration_date.isoformat()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
   
@session_tokens_bp.route('/session_tokens', methods=['POST'])
def create_session_token():
    try:
        data = request.json
        new_token = create_session_token(data)
        return jsonify({"message": "Session Token added", "id": new_token.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@session_tokens_bp.route('/session_tokens/<int:id_user>', methods=['PUT'])
def update_session_token(token_id):
    try:
        data = request.json
        updated_token = update_session_token(token_id, data)
        if not updated_token:
            return jsonify({"error": "Token not found"}), 404

        return jsonify({"message": "Session Token updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@session_tokens_bp.route('/session_tokens/<int:id_user>', methods=['DELETE'])
def delete_session_token(token_id):
    try:
        deleted_token = delete_session_token(token_id)
        if not deleted_token:
            return jsonify({"error": "Token not found"}), 404

        return jsonify({"message": "Session Token deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500