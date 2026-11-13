import json
from pathlib import Path

from auditor.system_info import collect_system_info
from auditor.users import check_users
from auditor.permissions import check_permissions
from auditor.firewall import check_firewall
from auditor.ssh_config import check_ssh_config


def main():
    print("\n===== LINUX SECURITY AUDITOR =====")
    print("Iniciando auditoria...\n")

    system_info = collect_system_info()

    findings = []
    findings.extend(check_users())
    findings.extend(check_permissions())
    findings.extend(check_firewall())
    findings.extend(check_ssh_config())

    report = {
        "sistema": system_info,
        "total_verificacoes_com_alertas": len(findings),
        "resultados": findings
    }

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_path = reports_dir / "audit_report.json"

    with report_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print("===== INFORMAÇÕES DO SISTEMA =====")

    for key, value in system_info.items():
        print(f"{key}: {value}")

    print("\n===== RESULTADOS =====")

    if findings:
        for finding in findings:
            print(f"\nVerificação: {finding['verificacao']}")
            print(f"Risco: {finding['risco']}")
            print(f"Evidência: {finding['evidencia']}")
            print(f"Recomendação: {finding['recomendacao']}")
    else:
        print("Nenhum alerta foi encontrado nas verificações realizadas.")

    print(f"\nRelatório salvo em: {report_path}")


if __name__ == "__main__":
    main()
