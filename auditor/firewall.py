import subprocess


def check_firewall():
    try:
        result = subprocess.run(
            ["ufw", "status"],
            capture_output=True,
            text=True,
            timeout=10
        )

        output = result.stdout.strip()

        if "Status: active" in output:
            risk = "BAIXO"
            recommendation = "Firewall UFW está ativo."
        elif "Status: inactive" in output:
            risk = "MÉDIO"
            recommendation = (
                "Avaliar a ativação do firewall e as regras necessárias."
            )
        else:
            risk = "INFORMATIVO"
            recommendation = (
                "Não foi possível determinar o estado do firewall."
            )

        return [{
            "verificacao": "Estado do firewall",
            "risco": risk,
            "evidencia": output or result.stderr.strip(),
            "recomendacao": recommendation
        }]

    except FileNotFoundError:
        return [{
            "verificacao": "Estado do firewall",
            "risco": "INFORMATIVO",
            "evidencia": "UFW não está instalado.",
            "recomendacao": "Verificar qual ferramenta de firewall é utilizada."
        }]

    except subprocess.TimeoutExpired:
        return [{
            "verificacao": "Estado do firewall",
            "risco": "INFORMATIVO",
            "evidencia": "A consulta excedeu o tempo limite.",
            "recomendacao": "Repetir a verificação."
        }]