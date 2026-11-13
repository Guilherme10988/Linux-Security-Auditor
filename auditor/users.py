import pwd


def check_users():
    findings = []

    for user in pwd.getpwall():
        if user.pw_uid == 0 and user.pw_name != "root":
            findings.append({
                "verificacao": "Conta com UID 0",
                "risco": "ALTO",
                "usuario": user.pw_name,
                "evidencia": f"UID: {user.pw_uid}",
                "recomendacao": (
                    "Verificar se essa conta precisa de privilégios "
                    "equivalentes aos do root."
                )
            })

    return findings
