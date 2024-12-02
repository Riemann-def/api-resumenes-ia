from app.extensions import db
from models.summary import Summary
from datetime import datetime, timezone

def save_summary(original_url, summary, email):
    """Guarda un nuevo resumen en la base de datos."""
    try:
        new_summary = Summary(
            original_url=original_url,
            summary_text=summary['resumen'],
            email=email,
            category=summary['category'],
            tone=summary['tone'],
            fake_news_level=summary['fake_news_level'],
            created_at=datetime.now(timezone.utc)
        )
        db.session.add(new_summary)
        db.session.commit()
        return new_summary
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Error al guardar el resumen: {str(e)}")

def get_summary_by_id(summary_id):
    """Obtiene un resumen por ID."""
    try:
        return Summary.query.get(summary_id)
    except Exception as e:
        raise RuntimeError(f"Error al obtener el resumen con ID {summary_id}: {str(e)}")

def get_all_summaries():
    """Obtiene todos los resúmenes de la base de datos."""
    try:
        return Summary.query.all()
    except Exception as e:
        raise RuntimeError(f"Error al obtener todos los resúmenes: {str(e)}")
