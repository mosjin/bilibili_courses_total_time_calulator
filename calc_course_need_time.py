"""
Read time from txt and calc course total time needs
"""

from datetime import datetime, timedelta

ctimes = list()
with open( "course_time.txt", 'r', encoding = "UTF-8" ) as file:
    for line in file:
        line = line.rstrip( "\n" )
        if line:
            ctimes.append( line )

#start = datetime.strptime( "2023-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
#tm_format = "%Y-%m-%d %H:%M:%S"
tm_format = "%H:%M:%S"
start = datetime.strptime( ctimes[ 0 ], tm_format )
end_time = start

for ts in ctimes:
    dt = datetime.strptime( ts, tm_format )
    # print(dt, type( dt ), dt.hour, dt.minute, dt.second )
    end_time += timedelta( 0, dt.second, 0, 0, dt.minute, dt.hour )

print( f"start time: {start}" )
print( f"end time: {end_time}" )
print( f"difference: {end_time - start}" )
