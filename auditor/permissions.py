import os
import stat


def check_permissions():
    findings = []

    sensitive_paths = [
        "/etc/passwd",
        "/etc/shadow",
        "/etc/group",
        "/etc/sudoers"
    ]

    for path in sensitive_paths:
        if not os.path.exists(path):
            continue

        try:
            file_info = os.stat(path)
            mode = file_info.st_mode

            if mode & stat.S_IWOTH:
                findings.append({
                    "verificacao": "Permissão de escrita para todos",
                    "risco": "ALTO",
                    "arquivo": path,
                    "evidencia": oct(stat.S_IMODE(mode)),
                    "recomendacao": (
                        "Revisar as permissões do arquivo e restringir "
                        "a escrita a usuários autorizados."
                    )
                })

        except PermissionError:
            findings.append({
                "verificacao": "Acesso negado",
                "risco": "INFORMATIVO",
                "arquivo": path,
                "evidencia": "Não foi possível consultar as permissões.",
                "recomendacao": "Executar a verificação com permissões adequadas."
            })

    return findings