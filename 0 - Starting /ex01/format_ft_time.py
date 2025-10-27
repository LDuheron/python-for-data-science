
from datetime import datetime

now = datetime.now()
jan_1970 = datetime(1970, 1, 1)
delta = now - jan_1970

print(f'Seconds since January 1, 1970: {delta.total_seconds()} or {delta.total_seconds():e} in scientific notation')
print(f'{now.strftime("%b %d %Y")}')