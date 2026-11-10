<#
Mini SOC safe simulation script.

Run only in a Windows lab you own or are authorized to test.
The commands below are intentionally benign. Their purpose is to create
process telemetry for Sysmon/Wazuh detection practice.
#>

Write-Host "[1/3] Generating discovery process events..."
whoami
ipconfig /all
netstat -ano

Write-Host "[2/3] Generating benign encoded PowerShell process..."
$payload = 'Write-Output "MINI-SOC-LAB: benign encoded PowerShell test"'
$bytes = [System.Text.Encoding]::Unicode.GetBytes($payload)
$encoded = [Convert]::ToBase64String($bytes)
powershell.exe -NoProfile -EncodedCommand $encoded

Write-Host "[3/3] Generating benign web-download-pattern process..."
# This intentionally points to localhost on an unlikely-to-be-open port.
# The request is expected to fail; the command line still creates useful telemetry.
powershell.exe -NoProfile -Command "try { Invoke-WebRequest -Uri 'http://127.0.0.1:65535/mini-soc-test' -UseBasicParsing -TimeoutSec 2 } catch { Write-Output 'Expected lab connection failure' }"

Write-Host "Done. Review Sysmon Event ID 1 and Wazuh rules 100100-100102."
