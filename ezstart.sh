#!/bin/bash
source venv/bin/activate
python launcher.py 
sleep 5s
chromium-browser --kiosk "http://127.0.0.1:5000"