@echo off
REM ==============================================================================
REM Installer for Ten Thinking Dimensions Cognitive OS (Windows CMD)
REM ==============================================================================

setlocal

set "SCRIPT_DIR=%~dp0"
set "SRC_DIR=%SCRIPT_DIR%.agents\skills\ten-thinking-dimensions"
set "DEST_DIR=%USERPROFILE%\.gemini\config\skills\ten-thinking-dimensions"

echo ============================================================
echo   Installing: Ten Thinking Dimensions (ผู้ชนะ 10 คิด)
echo ============================================================

if not exist "%SRC_DIR%" (
    echo Error: Source directory %SRC_DIR% not found!
    exit /b 1
)

if not exist "%USERPROFILE%\.gemini\config\skills" (
    mkdir "%USERPROFILE%\.gemini\config\skills"
)

if exist "%DEST_DIR%" (
    rmdir /s /q "%DEST_DIR%"
)

xcopy /E /I /Y "%SRC_DIR%" "%DEST_DIR%"

echo.
echo [SUCCESS] Installed successfully to:
echo   %DEST_DIR%
echo.
echo You can now use "ผู้ชนะ 10 คิด" across all workspaces on this machine!
echo ============================================================

pause
