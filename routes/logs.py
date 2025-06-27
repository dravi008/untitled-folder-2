from flask import Blueprint, request, jsonify
from app import db
from models.models import FlightLog
from datetime import datetime

logs_bp = Blueprint('logs', __name__)

@logs_bp.route('/flight-log', methods=['POST'])
def add_flight_log():
    data = request.get_json()
    student_id = data.get('student_id')
    date = data.get('date')
    phase = data.get('phase')
    maneuver_ratings = data.get('maneuver_ratings')
    notes = data.get('notes')
    ai_debrief = data.get('ai_debrief')
    if not all([student_id, date, phase, maneuver_ratings]):
        return jsonify({'error': 'Missing fields'}), 400
    log = FlightLog(
        student_id=student_id,
        date=datetime.strptime(date, '%Y-%m-%d'),
        phase=phase,
        maneuver_ratings=maneuver_ratings,
        notes=notes,
        ai_debrief=ai_debrief
    )
    db.session.add(log)
    db.session.commit()
    return jsonify({'message': 'Flight log added', 'log_id': log.id}), 201 