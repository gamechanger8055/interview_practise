from grokking.meeting_calendar.dao.meetings_dao import MeetingDAO
from grokking.meeting_calendar.dao.user_dao import UserDAO
from grokking.meeting_calendar.dao.user_meeting_dao import UserMeetingDAO
from grokking.meeting_calendar.service.meeting_service import MeetingService
from grokking.meeting_calendar.service.user_meeting_service import UserMeetingService
from grokking.meeting_calendar.service.user_service import UserService



if __name__ == '__main__':
    # Initialize DAOs
    user_dao = UserDAO()
    meeting_dao = MeetingDAO()
    user_meeting_dao = UserMeetingDAO()

    # Initialize Services
    user_service = UserService(user_dao)
    meeting_service = MeetingService(meeting_dao)
    user_meeting_service = UserMeetingService(user_meeting_dao)

    # Example usage
    user = user_service.create_user(1, 'Alice', 'alice@example.com')
    print(user)

    retrieved_user = user_service.get_user_by_id(1)
    print(retrieved_user)