# put your python code here
walk_hour = int(input())
walk_minute = int(input())
walk_second = int(input())
rain_hour = int(input())
rain_minute = int(input())
rain_second = int(input())
seconds_diff = rain_second - walk_second
minutes_diff = rain_minute - walk_minute
hours_diff = rain_hour - walk_hour
seconds_between = seconds_diff + 60 * minutes_diff + 3600 * hours_diff
print(seconds_between)