#!/bin/sh

# Set the content type
echo "Content-Type: text/html"
echo ""

# RTC device
RTC=rtc0

# Read date and time from RTC
DATE=$(cat /sys/class/rtc/$RTC/date 2>&-)
TIME=$(cat /sys/class/rtc/$RTC/time 2>&-)
DATETIME="$DATE $TIME"

# Output the HTML page
echo "<html>"
echo "<head><title>System RTC Date and Time</title></head>"
echo "<body>"

if [ "$DATETIME" = " " ]; then
    echo "<p>Error: Unable to read date and time from $RTC</p>"
else
    echo "<p>$DATETIME</p>"
fi

echo "</body>"
echo "</html>"
