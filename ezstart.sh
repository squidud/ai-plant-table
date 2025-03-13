#!/bin/bash
source ~/ai-plant-table/venv/bin/activate
python ~/ai-plant-table/launcher.py &
sleep 5s
chromium-browser --kiosk "http://127.0.0.1:5000"