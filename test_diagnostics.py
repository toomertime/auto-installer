from diagnostics import check_winget

result = check_winget()

print("\n--- DIAGNOSTIC RESULTS ---")
print(f"Ready: {result.ready}")
print(f"WinGet path: {result.winget_path}")
print(f"WinGet version: {result.winget_version}")
print(f"WinGet source available: {result.winget_source_available}")
print(f"Error: {result.error}")