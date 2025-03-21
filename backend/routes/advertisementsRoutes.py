from flask import Blueprint, request, jsonify
from backend.services.advertisementsServices import get_all_ads, get_ad_by_id, create_ad, update_ad , delete_ad
from backend.models import db
from backend.models.advertisementsModel import Advertisement

advertisements_bp = Blueprint('advertisements', __name__)

@advertisements_bp.route('/advertisements', methods=['GET'])
def get_advertisements():
    try:
        ads = get_all_ads()
        return jsonify([{
            "id": ad.id,
            "title": ad.title,
            "description": ad.description,
            "image_path": ad.image_path,
            "contact": ad.contact,
            "publication_date": ad.publication_date,
            "is_active": ad.is_active
        } for ad in ads])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@advertisements_bp.route('/advertisements/<int:id>', methods=['GET'])
def get_advertisement_by_id(id):
    try:
        ad = get_ad_by_id(id)
        return jsonify({
            "id": ad.id,
            "title": ad.title,
            "description": ad.description,
            "image_path": ad.image_path,
            "contact": ad.contact,
            "publication_date": ad.publication_date,
            "is_active": ad.is_active
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@advertisements_bp.route('/advertisements', methods=['POST'])
def create_advertisement():
    try:
        data = request.json
        new_ad = create_ad(data)

        return jsonify({"message": "Advertisement added", "id":new_ad.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@advertisements_bp.route('/advertisements/<int:id>', methods=['PUT'])
def update_advertisement(id):
    try:
        data = request.json  # ✅ Se define antes de usarlo
        update_ad = update_ad(id,data)
        return jsonify({"message": "Advertisement updated"})
    except ValueError as ve:
        return jsonify({"error":str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@advertisements_bp.route('/advertisements/<int:id>', methods=['DELETE'])
def delete_advertisement(id):
    try:
        delete_ad(id)
        return jsonify({"message": "Advertisement deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500