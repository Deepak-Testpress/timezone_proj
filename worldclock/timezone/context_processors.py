from django.utils import timezone
from backports.zoneinfo import ZoneInfo
import re
import pytz


common_timezones = {
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "New York": "America/New_York",
    "Kolkata": "Asia/Kolkata",
}
timezones = pytz.common_timezones
print(timezones)
timezone_name = timezone.get_current_timezone_name()
print(timezone_name)
print()
city = re.sub("(.*[\\\/])","",timezone_name)
print(city)
print(timezone.now())
def time(request):
    return {"time": timezone, "city":city, "timezones":common_timezones }
