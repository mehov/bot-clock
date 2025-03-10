#!/bin/sh

# Every 10 minutes between 6:00 and 22:00
echo "*/10 6-22 * * * root wget -O /dev/null -o /dev/null http://${1}/keepalive" > /etc/cron.d/bot-clock
