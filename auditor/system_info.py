import platform
import socket
import getpass
from datetime import datetime


def collect_system_info():
    info = {
        "Sistema operacional": platform.system(),
        "Versão": platform.version(),
        "Kernel": platform.release(),
        "Arquitetura": platform.machine(),
        "Hostname": socket.gethostname(),
        "Usuário atual": getpass.getuser(),
        "Data da auditoria": datetime.now().astimezone().isoformat(
            timespec="seconds"
        )
    }

    if platform.system() == "Linux":
        try:
            release = platform.freedesktop_os_release()
            info["Distribuição"] = release.get("PRETTY_NAME", "Linux")
        except (AttributeError, OSError):
            info["Distribuição"] = "Não identificada"

    return info