# List of apps available for installation
# Each app is represented as a dictionary with its name, category, and winget ID
# The "process_name" key is optional and specifies the name of the process to kill after installation
# The "install_location" key is optional and specifies where the app should be installed
APPS = [
    # Browsers
    {
        "name": "Chrome",
        "category": "Browser",
        "winget_id": "Google.Chrome"
    },
    {
        "name": "Firefox",
        "category": "Browser",
        "winget_id": "Mozilla.Firefox"
    },
    {
        "name": "Brave",
        "category": "Browser",
        "winget_id": "Brave.Brave"
    },
    {
        "name": "Opera",
        "category": "Browser",
        "winget_id": "Opera.Opera",
        "process_name": "opera.exe"
    },

    # Gaming Launchers
    {
        "name": "Steam",
        "category": "Gaming Launcher",
        "winget_id": "Valve.Steam"
    },
    {
        "name": "Epic Games Launcher",
        "category": "Gaming Launcher",
        "winget_id": "EpicGames.EpicGamesLauncher"
    },
    {
        "name": "Battle.net",
        "category": "Gaming Launcher",
        "winget_id": "Blizzard.BattleNet",
        "process_name": "Battle.net.exe",
        "install_location": "C:\\Program Files (x86)\\Battle.net"
    },

    # Antivirus
    {
        "name": "Webroot",
        "category": "Antivirus",
        "winget_id": "Webroot.SecureAnywhere",
        "process_name": "WRSA.exe"
    },
    {
        "name": "Malwarebytes",
        "category": "Antivirus",
        "winget_id": "Malwarebytes.Malwarebytes"
    },
    # Trend Micro - No winget ID available
    # Norton 360 - No winget ID available
    {
        "name": "Bitdefender",
        "category": "Antivirus",
        "winget_id": "Bitdefender.Bitdefender"
    },

    # Media
    {
        "name": "VLC Media Player",
        "category": "Media",
        "winget_id": "VideoLAN.VLC"
    },
    {
        "name": "iTunes",
        "category": "Media",
        "winget_id": "Apple.iTunes"
    },
    {
        "name": "Spotify",
        "category": "Media",
        "winget_id": "Spotify.Spotify"
    },

    # Cloud Storage
    {
        "name": "Dropbox",
        "category": "Cloud Storage",
        "winget_id": "Dropbox.Dropbox"
    },
    {
        "name": "Google Drive",
        "category": "Cloud Storage",
        "winget_id": "Google.GoogleDrive"
    },

    # Productivity
    {
        "name": "Microsoft Office",
        "category": "Productivity",
        "winget_id": "Microsoft.Office"
    },
    {
        "name": "Adobe Acrobat Reader",
        "category": "Productivity",
        "winget_id": "Adobe.Acrobat.Reader.64-bit"
    },
    {
        "name": "LibreOffice",
        "category": "Productivity",
        "winget_id": "thedocumentfoundation.LibreOffice"
    },

    # Video Conferencing
    {
        "name": "Zoom",
        "category": "Video Conferencing",
        "winget_id": "Zoom.Zoom"
    },

    # Utility
    {
        "name": "HP Support Assistant",
        "category": "Utility",
        "winget_id": "HPInc.HPSupportAssistant"
    },
    {
        "name": "7-Zip",
        "category": "Utility",
        "winget_id": "7Zip.7Zip"
    }
]