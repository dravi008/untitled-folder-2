from flask import Blueprint, request, jsonify
from app import db
from models.models import Student

students_bp = Blueprint('students', __name__)

@students_bp.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get('name')
    user_id = data.get('user_id')
    if not all([name, user_id]):
        return jsonify({'error': 'Missing fields'}), 400
    student = Student(name=name, user_id=user_id)
    db.session.add(student)
    db.session.commit()
    return jsonify({'message': 'Student added', 'student_id': student.id}), 201

@students_bp.route('/students/<int:user_id>', methods=['GET'])
def list_students(user_id):
    students = Student.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': s.id, 'name': s.name} for s in students]) 