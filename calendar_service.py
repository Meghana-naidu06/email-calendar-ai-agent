from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.events']


def create_calendar_event(title, date, time):

    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)

    creds = flow.run_local_server(port=0)

    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': title,
        'start': {
            'dateTime': '2026-03-09T15:00:00',
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': '2026-03-09T16:00:00',
            'timeZone': 'Asia/Kolkata',
        },
    }

    event = service.events().insert(
        calendarId='primary', body=event).execute()

    print("Event created:", event.get('htmlLink'))