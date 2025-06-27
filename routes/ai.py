from flask import Blueprint, request, jsonify
from utils.openai_handler import generate_dummy_debrief

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/generate-debrief', methods=['POST'])
def generate_debrief():
    data = request.get_json()
    student_name = data.get('student_name')
    phase = data.get('phase')
    maneuver_ratings = data.get('maneuver_ratings')
    notes = data.get('notes')
    # Dummy logic for now
    debrief = generate_dummy_debrief(student_name, phase, maneuver_ratings, notes)
    return jsonify({'debrief': debrief}) 