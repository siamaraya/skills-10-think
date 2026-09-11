# ==============================================================================
# Installer for Ten Thinking Dimensions Cognitive OS (Windows PowerShell)
# ==============================================================================

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SrcDir = Join-Path $ScriptDir ".agents\skills\ten-thinking-dimensions"
$DestDir = Join-Path $HOME ".gemini\config\skills\ten-thinking-dimensions"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Installing: Ten Thinking Dimensions (ผู้ชนะ 10 คิด)" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

if (-not (Test-Path $SrcDir)) {
    Write-Host "Error: Source directory $SrcDir not found!" -ForegroundColor Red
    exit 1
}

$ParentDest = Join-Path $HOME ".gemini\config\skills"
if (-not (Test-Path $ParentDest)) {
    New-Item -ItemType Directory -Path $ParentDest -Force | Out-Null
}

if (Test-Path $DestDir) {
    Remove-Item -Recurse -Force $DestDir
}

Copy-Item -Path $SrcDir -Destination $DestDir -Recurse -Force

Write-Host ""
Write-Host "[SUCCESS] Installed successfully to:" -ForegroundColor Green
Write-Host "  $DestDir" -ForegroundColor Green
Write-Host ""
Write-Host "You can now use 'ผู้ชนะ 10 คิด' across all workspaces on this machine!" -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Cyan
