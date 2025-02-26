from flask import Blueprint, request, jsonify
from backend import db
from backend.models.advertisementsModel import Advertisement

advertisements_bp = Blueprint('advertisements', __name__)

@advertisements_bp.route('/api/advertisements', methods=['GET'])
def get_advertisements():
    try:
        ads = Advertisement.query.all()
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

@advertisements_bp.route('/api/advertisements', methods=['POST'])
def create_advertisement():
    try:
        data = request.json
        new_ad = Advertisement(
            title=data['title'],
            description=data['description'],
            image_path=data['image_path'],
            contact=data['contact'],
            publication_date=data.get('publication_date'),  # Opcional, puede venir en la petición
            is_active=bool(data.get('is_active', True))  # Valor por defecto True
        )
        db.session.add(new_ad)
        db.session.commit()
        return jsonify({"message": "Advertisement added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@advertisements_bp.route('/api/advertisements/<int:id>', methods=['PUT'])
def update_advertisement(id):
    try:
        data = request.json  # ✅ Se define antes de usarlo

        required_fields = ['title', 'description', 'image_path', 'contact']
        for field in required_fields:
            if field not in data or not isinstance(data[field], str) or not data[field].strip():
                return jsonify({"error": f"{field} is required"}), 400

        ad = Advertisement.query.get_or_404(id)
        ad.title = data.get('title', ad.title)
        ad.description = data.get('description', ad.description)
        ad.image_path = data.get('image_path', ad.image_path)
        ad.contact = data.get('contact', ad.contact)
        ad.is_active = bool(data.get('is_active', ad.is_active))  # ✅ Se convierte en bool para evitar errores

        db.session.commit()
        return jsonify({"message": "Advertisement updated"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@advertisements_bp.route('/api/advertisements/<int:id>', methods=['DELETE'])
def delete_advertisement(id):
    try:
        ad = Advertisement.query.get_or_404(id)
        db.session.delete(ad)
        db.session.commit()
        return jsonify({"message": "Advertisement deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500