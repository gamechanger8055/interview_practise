from flask import Flask, jsonify, request
from grokking.meeting_calendar.dao.meetings_dao import MeetingDAO
from grokking.meeting_calendar.dao.user_dao import UserDAO
from grokking.meeting_calendar.dao.user_meeting_dao import UserMeetingDAO
from grokking.meeting_calendar.service.meeting_service import MeetingService
from grokking.meeting_calendar.service.user_meeting_service import UserMeetingService
from grokking.meeting_calendar.service.user_service import UserService

app = Flask(__name__)

# Mock DAO objects
user_dao = UserDAO()
meeting_dao = MeetingDAO()
user_meeting_dao = UserMeetingDAO()

# Initialize services
user_service = UserService(user_dao)
meeting_service = MeetingService(meeting_dao)
user_meeting_service = UserMeetingService(user_meeting_dao)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = user_service.create_user(data['id'], data['name'], data['email'])
    return jsonify({'users': vars(user)}), 201


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify({'users': vars(user)}), 200
    return jsonify({'messgae': "User Not found"}), 404


@app.route('/meetings', methods=['POST'])
def create_meeting():
    data = request.get_json()
    meeting = meeting_service.create_meeting(data['id'], data['description'], data['date'], data['recurrence_type'],
                                             data['created_by_user_id'])
    return jsonify({'meeting': vars(meeting)}), 201


@app.route('/meetings/<int:meeting_id>', methods=['GET'])
def get_meeting(meeting_id):
    meeting = meeting_service.get_meeting_by_id(meeting_id)
    if meeting:
        return jsonify({'meeting': vars(meeting)})
    else:
        return jsonify({'message': 'Meeting not found'}), 404


if __name__ == "__main__":
    app.run(debug=True)
