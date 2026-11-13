from pathlib import Path


def check_ssh_config():
    findings = []
    config_path = Path("/etc/ssh/sshd_config")

    if not config_path.exists():
        return [{
            "verificacao": "Configuração SSH",
            "risco": "INFORMATIVO",
            "evidencia": "Arquivo sshd_config não encontrado.",
            "recomendacao": "Verificar se o serviço SSH está instalado."
        }]

    settings = {}

    try:
        for line in config_path.read_text(
            encoding="utf-8", errors="replace"
        ).splitlines():

            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split(None, 1)

            if len(parts) == 2:
                settings[parts[0].lower()] = parts[1].strip().lower()

    except PermissionError:
        return [{
            "verificacao": "Configuração SSH",
            "risco": "INFORMATIVO",
            "evidencia": "Permissão negada para ler o arquivo.",
            "recomendacao": "Consultar o arquivo com permissões adequadas."
        }]

    password_auth = settings.get("passwordauthentication")

    if password_auth == "yes":
        findings.append({
            "verificacao": "Autenticação por senha SSH",
            "risco": "MÉDIO",
            "evidencia": "PasswordAuthentication yes",
            "recomendacao": (
                "Avaliar o uso de chaves SSH e as necessidades "
                "de acesso dos usuários."
            )
        })

    root_login = settings.get("permitrootlogin")

    if root_login == "yes":
        findings.append({
            "verificacao": "Login SSH como root",
            "risco": "ALTO",
            "evidencia": "PermitRootLogin yes",
            "recomendacao": "Avaliar a desativação do login direto do root."
        })

    return findings