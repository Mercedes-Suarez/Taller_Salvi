from flask import Blueprint, request, jsonify
from backend import db
from backend.models.advertisementsModel import Advertisement

advertisements_bp = Blueprint('advertisements', __name__)

@advertisements_bp.route('/advertisements', methods=['GET'])
def get_advertisements():
    ads = Advertisement.query.all()
    return jsonify([{
        "id_advertisement": ad.id_advertisement,
        "title": ad.title,
        "description": ad.description,
        "image_path": ad.image_path,
        "contact": ad.contact,
        "publication_date": ad.publication_date,
        "asset": ad.asset
    } for ad in ads])

@advertisements_bp.route('/advertisements', methods=['POST'])
def create_advertisement():
    data = request.json
    new_ad = Advertisement(
        title=data['title'],
        description=data['description'],
        image_path=data['image_path'],
        contact=data['contact'],
        publication_date=data['publication_date'],
        asset=data['asset']
    )
    db.session.add(new_ad)
    db.session.commit()
    return jsonify({"message": "Advertisement added"}), 201

@advertisements_bp.route('/advertisements/<int:id>', methods=['PUT'])
def update_advertisement(id):
    ad = Advertisement.query.get_or_404(id)
    data = request.json
    ad.title = data.get('title', ad.title)
    ad.description = data.get('description', ad.description)
    ad.image_path = data.get('image_path', ad.image_path)
    ad.contact = data.get('contact', ad.contact)
    ad.asset = data.get('asset', ad.asset)
    db.session.commit()
    return jsonify({"message": "Advertisement updated"})

@advertisements_bp.route('/advertisements/<int:id>', methods=['DELETE'])
def delete_advertisement(id):
    ad = Advertisement.query.get_or_404(id)
    db.session.delete(ad)
    db.session.commit()
    return jsonify({"message": "Advertisement deleted"})