#! /bin/sh

#DOC#@CLI@ "list running services"

systemctl list-units --type=service --all --no-pager --no-legend | sort -k4
