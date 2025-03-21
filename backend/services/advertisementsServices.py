from backend.models import db
from backend.models.advertisementsModel import Advertisement

def get_all_ads():
    """Obtiene todos los anuncios"""
    return Advertisement.query.all()

def get_ad_by_id(ad_id):
    """Obtiene un anuncio por ID"""
    return Advertisement.query.get_or_404(ad_id)

def create_ad(data):
    """Crea un nuevo anuncio"""
    new_ad = Advertisement(
        title=data['title'],
        description=data['description'],
        image_path=data['image_path'],
        contact=data['contact'],
        publication_date=data.get('publication_date'),  # Opcional
        is_active=bool(data.get('is_active', True))  # Valor por defecto True
    )
    db.session.add(new_ad)
    db.session.commit()
    return new_ad

def update_ad(ad_id, data):
    """Actualiza un anuncio"""
    ad = Advertisement.query.get_or_404(ad_id)

    required_fields = ['title', 'description', 'image_path', 'contact']
    for field in required_fields:
        if field not in data or not isinstance(data[field], str) or not data[field].strip():
            raise ValueError(f"{field} is required")

    ad.title = data.get('title', ad.title)
    ad.description = data.get('description', ad.description)
    ad.image_path = data.get('image_path', ad.image_path)
    ad.contact = data.get('contact', ad.contact)
    ad.is_active = bool(data.get('is_active', ad.is_active))

    db.session.commit()
    return ad

def delete_ad(ad_id):
    """Elimina un anuncio"""
    ad = Advertisement.query.get_or_404(ad_id)
    db.session.delete(ad)
    db.session.commit()
    return ad