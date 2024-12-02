from flask import Blueprint, request, jsonify
from services.openai_api import generate_summary
from services.emailer import send_summary_email
from services.db_service.summary import save_summary, get_summary_by_id, get_all_summaries

summary_bp = Blueprint("summary", __name__, url_prefix="/api/summary")

@summary_bp.route("/", methods=["POST"])
def create_summary():
    """Crea un resumen a partir de una URL."""
    data = request.json
    original_url = data.get("url", None)
    email = data.get("email", None)

    if not original_url:
        return jsonify({"error": "La URL es obligatoria"}), 400

    try:
        print("Generando resumen para la URL:", original_url)  # Print para ver la URL
        # Generar resumen con OpenAI
        summary_response = generate_summary(original_url)
        print("Resumen generado:", summary_response)  # Print para ver el resumen generado

        # Guardar en la base de datos
        new_summary = save_summary(original_url, summary_response, email)
        print("Resumen guardado en la base de datos con ID:", new_summary.id)  # Print para ver el ID del resumen guardado

        # Enviar por correo si aplica
        if email:
            send_summary_email(email, original_url, summary_response)
            print("Correo enviado a:", email)  # Print para ver el correo enviado

        return jsonify({"id": new_summary.id, "summary": summary_response}), 201
    except RuntimeError as e:
        print("Error al crear el resumen:", str(e))  # Print para ver el error
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        print("Error inesperado:", str(e))  # Print para ver el error inesperado
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500

@summary_bp.route("/", methods=["GET"])
def get_summaries():
    """Obtiene resúmenes por ID o todos."""
    summary_id = request.args.get("id")

    try:
        if summary_id:
            # Obtener un resumen por ID
            summary = get_summary_by_id(summary_id)
            if not summary:
                return jsonify({"error": "Resumen no encontrado"}), 404
            return jsonify({
                "id": summary.id,
                "original_url": summary.original_url,
                "summary_text": summary.summary_text,
                "category": summary.category,
                "fake_news_level": summary.fake_news_level,
                "tone": summary.tone,
                "created_at": summary.created_at,
                "email": summary.email
            }), 200
        else:
            # Obtener todos los resúmenes
            summaries = get_all_summaries()
            return jsonify([{
                "id": summary.id,
                "original_url": summary.original_url,
                "summary_text": summary.summary_text,
                "category": summary.category,
                "fake_news_level": summary.fake_news_level,
                "tone": summary.tone,
                "created_at": summary.created_at,
                "email": summary.email
            } for summary in summaries]), 200
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500
