from installer import install_app

app = {
    "name": "7-Zip",
    "winget_id": "7zip.7zip"
}

result = install_app(app)

print("\n--- INSTALL RESULT ---")
print(f"App: {result.app_name}")
print(f"Success: {result.success}")
print(f"Return code: {result.return_code}")
print(f"Error: {result.error}")