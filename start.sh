#!/bin/bash

echo "Starting Backend Server..."
cd backend
gnome-terminal -- bash -c "python app.py; exec bash" 2>/dev/null || xterm -e "python app.py; bash" &
cd ..

echo "Waiting for backend to start..."
sleep 3

echo "Starting Frontend Server..."
cd frontend
gnome-terminal -- bash -c "npm run dev; exec bash" 2>/dev/null || xterm -e "npm run dev; bash" &
cd ..

echo ""
echo "========================================"
echo "  Smart Store Monitor System Started"
echo "========================================"
echo "  Backend:  http://127.0.0.1:5000"
echo "  Frontend: http://localhost:5173"
echo "========================================"
echo ""
