#! /bin/bash
### BEGIN INIT INFO
# Provides:          BraveRadio
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: init script for BraveRadio
# Description:       Python sound trigger script
### END INIT INFO

# Author: Justin Triplett (justin.triplett@gmail.com)

PATH=/sbin:/usr/sbin:/bin:/usr/bin
DESC="BraveRadio python sound script"
NAME=BraveRadio
PIDFILE=/var/run/$NAME.pid
SCRIPTNAME=/etc/init.d/$NAME
LOGFILE=/var/lib/cloud9/BraveRadio/log/out

case "$1" in
    start)
        echo -e "Starting BraveRadio\n" `date`
        sudo /var/lib/cloud9/BraveRadio/playcontrol.py >> $LOGFILE
        ;;
    stop)
        echo "Stopping BraveRadio"
        killall playcontrol.py
        ;;
    status)
        echo "ps -ef | grep playcontrol"
        COUNT=$(ps -ef | grep -v grep | grep playcontrol | wc -l) 
        echo "COUNT: "$COUNT
        OUTPUT=$(ps -ef | grep -v grep | grep playcontrol) 
        echo $OUTPUT
        ;;
    restart)
        echo "Restarting BraveRadio"
        echo "first killall" 
        killall playcontrol.py
        echo "then start"
        sudo /var/lib/cloud9/BraveRadio/playcontrol.py >> $LOGFILE
        echo ":)"
        ;;
    *)
        echo "Usage: $0 {start|stop|status|restart}"
        ;;
esac


exit 0