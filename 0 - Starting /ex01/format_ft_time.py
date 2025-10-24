
from datetime import datetime

now = datetime.now()

print(f'Seconds since January 1, 1970: {now.timestamp()} or {now.timestamp():e} in scientific notation')
print(f'{now.strftime("%b %d %Y")}')