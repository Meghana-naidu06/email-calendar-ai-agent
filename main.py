from email_parser import extract_meeting_details
from calendar_service import create_calendar_event
import json

email_text = """
Hi Meghana,

Let's have a project meeting tomorrow at 3 PM.

Thanks
"""

result = extract_meeting_details(email_text)

print("Extracted Meeting Details:")
print(result)

data = json.loads(result)

create_calendar_event(
    data["title"],
    data["date"],
    data["time"]
)