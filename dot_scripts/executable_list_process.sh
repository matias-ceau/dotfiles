#! /bin/sh

#DOC#@CLI@=2024-07= "list running services"

systemctl list-units --type=service --all --no-pager --no-legend | sort -k4
