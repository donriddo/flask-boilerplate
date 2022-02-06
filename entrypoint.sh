#!/usr/bin/env bash
FLASK_APP=manager.py flask db upgrade
python3 manager.py run
