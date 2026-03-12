@echo off
echo Starting Backend Server...
cd backend
start cmd /k "python app.py"
cd ..

echo Waiting for backend to start...
timeout /t 3 /nobreak > nul

echo Starting Frontend Server...
cd frontend
start cmd /k "npm run dev"
cd ..

echo.
echo ========================================
echo   Smart Store Monitor System Started
echo ========================================
echo   Backend:  http://127.0.0.1:5000
echo   Frontend: http://localhost:5173
echo ========================================
echo.
