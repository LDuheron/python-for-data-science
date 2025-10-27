
from datetime import datetime

now = datetime.now()
jan_70 = now.timestamp()

print(f'Seconds since January 1, 1970: {jan_70:,.3f} or {jan_70:2e} in scientific notation')
print(f'{now.strftime("%b %d %Y")}')