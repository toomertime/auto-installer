# List of apps available for installation
# Each app is represented as a dictionary with its name, category, and winget ID
# The "install_location" key is optional and specifies where the app should be installed
# The "override" key is optional and passes custom flags to the installer
# The "cleanup_processes" key is optional and specifies a list of processes to kill after installation
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
        "cleanup_processes": ["opera.exe"]
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
        "cleanup_processes": ["Battle.net.exe"],
        "install_location": "C:\\Program Files (x86)\\Battle.net"
    },

    # Antivirus
    {
        "name": "Webroot",
        "category": "Antivirus",
        "winget_id": "Webroot.SecureAnywhere"
    },
    {
        "name": "Malwarebytes",
        "category": "Antivirus",
        "winget_id": "Malwarebytes.Malwarebytes"
    },
    # Trend Micro - No winget ID available
    # Norton 360 - No winget ID available

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
    # Spotify - requires non-admin context, skipped for now.
    # Planned for v2: separate non-admin helper process.
    #{
    #    "name": "Spotify",
    #    "category": "Media",
    #    "winget_id": "Spotify.Spotify",
    #    "requires_non_admin": True  # This app requires non-admin privileges
    #},

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