import hashlib
import datetime
import os
import re

def calorimetria(temp):
    try:
        t = float(temp)
    except Exception:
        return "ERRO! Intentálo otra vez"
    if t < 0:
        return "ERRO! Intentálo otra vez"
    # usar exatamente os intervalos do enunciado:
    # <20 Frio
    # >=20 e <40 Ideal
    # >=40 e <70 Alerta
    # >=70 Risco crítico
    if t < 20:
        return "Frio"
    if 20 <= t < 40:
        return "Ideal"
    if 40 <= t < 70:
        return "Alerta"
    return "Risco crítico"

def percentual_cpu(uso):
    try:
        u = float(uso)
    except Exception:
        return "ERRO! Intentálo otra vez"
    if u < 0:
        return "ERRO! Intentálo otra vez"
    # enunciado:
    # <40 Normal
    # 40–80 Alta
    # >80 Sobrecarga
    if u < 40:
        return "Normal"
    if 40 <= u <= 80:
        return "Alta"
    return "Sobrecarga"

def alzheimer(mem):
    try:
        m = float(mem)
    except Exception:
        return "ERRO! Intentálo otra vez"
    if m < 0:
        return "ERRO! Intentálo otra vez"
    # enunciado:
    # <50 Confortável
    # >=50 e <85 Monitorar
    # >=85 Crítica
    if m < 50:
        return "Confortável"
    if 50 <= m < 85:
        return "Monitorar"
    return "Crítica"

def latido(lat):
    try:
        l = float(lat)
    except Exception:
        return "ERRO! Intentálo otra vez"
    if l < 0:
        return "ERRO! Intentálo otra vez"
    if l < 10:
        return "Excelente"
    if 10 <= l < 40:
        return "Boa"
    if 40 <= l < 100:
        return "Regular"
    return "Ruim"

def locadora(espaco_livre):
    try:
        e = float(espaco_livre)
    except Exception:
        return "ERRO! Intentálo otra vez"
    if e < 0:
        return "ERRO! Intentálo otra vez"
    if e < 20:
        return "Crítico"
    if 20 <= e < 40:
        return "Atenção"
    return "Seguro"

def sistema(value=None):
    if value is None:
        name = os.name
    else:
        name = value
    try:
        s = str(name)
    except Exception:
        return "ERRO! Intentálo otra vez"
    if s == "nt":
        return "Windows"
    if s == "posix":
        return "Linux"
    return "ERRO! Intentálo otra vez"

def eventos(nome_servidor=None, timestamp=None):
    if not isinstance(nome_servidor, str) or not isinstance(timestamp, str):
        return "ERRO! Intentálo otra vez"
    # exigir ao menos uma letra em cada string (evita aceitar apenas números/negativos)
    if not re.search(r"[A-Za-z]", nome_servidor) or not re.search(r"[A-Za-z]", timestamp):
        return "ERRO! Intentálo otra vez"
    return f"{nome_servidor}{timestamp}"

def _parse_date_flexible(s):
    try:
        return datetime.datetime.fromisoformat(s)
    except Exception:
        parts = s.split("-")
        if len(parts) == 3:
            y = int(parts[0])
            m = int(parts[1])
            d = int(parts[2])
            return datetime.datetime(y, m, d)
        raise

def validar_certificado(data_emissao, anos):
    try:
        if not isinstance(data_emissao, str) or not isinstance(anos, int):
            return "ERRO! Intentálo otra vez"
        issued = _parse_date_flexible(data_emissao)
        vencimento = issued.replace(year=issued.year + anos)
        hoje = datetime.date.today()  # ← Use date.today() instead of datetime.now()
        vencimento_date = vencimento.date()  # ← Convert to date for comparison
        diff_days = (vencimento_date - hoje).days
        if diff_days < 0:
            return "Certificado expirado"
        if diff_days <= 30:
            return "Certificado expira em breve"
        return "Certificado válido"
    except Exception:
        return "ERRO! Intentálo otra vez"

def poupa_tempo(data_emissao, anos):
    return validar_certificado(data_emissao, anos)

def prever_armazenamento(inicial, taxa, anos):
    try:
        i = float(inicial)
        r = float(taxa)
        n = int(anos)
    except Exception:
        return ("ERRO! Intentálo otra vez",)
    final = i * ((1 + r) ** n)
    if final < 500:
        status = "Seguro"
    elif 500 <= final < 2000:
        status = "Monitorar"
    else:
        status = "Upgrade necessário"
    return (final, status)

def estoque(valor=None):
    try:
        v = float(valor)
    except Exception:
        return "ERRO! Intentálo otra vez"
    if v < 0:
        return "ERRO! Intentálo otra vez"
    if v < 500:
        return "Seguro"
    if 500 <= v < 2000:
        return "Monitorar"
    return "Upgrade necessário"

def analisar_trafego(r1=None, r2=None, r3=None):
    try:
        if r1 is None:
            return "ERRO! Intentálo otra vez"
        if r2 is None and r3 is None:
            a = float(r1)
            b = a
            c = a
        else:
            a = float(r1)
            b = float(r2)
            c = float(r3)
    except Exception:
        return "ERRO! Intentálo otra vez"
    if a < 0 or b < 0 or c < 0:
        return "ERRO! Intentálo otra vez"
    media = (a + b + c) / 3.0
    if media < 100:
        return "Baixo Tráfego"
    if 100 <= media < 500:
        return "Tráfego moderado"
    return "Tráfego alto"

def geral(temp=None, cpu=None, mem=None, lat=None, disco=None):
    if temp is None and cpu is None and mem is None and lat is None and disco is None:
        return "ERRO! Intentálo otra vez"
    try:
        t = float(temp) if temp is not None else None
        c = float(cpu) if cpu is not None else None
        m = float(mem) if mem is not None else None
        l = float(lat) if lat is not None else None
        d = float(disco) if disco is not None else None
    except Exception:
        return "ERRO! Intentálo otra vez"
    if (t is not None and t > 70) or (c is not None and c > 90) or (m is not None and m > 90) or (d is not None and d < 10):
        return "Servidor crítico"
    if (l is not None and l > 100) or (t is not None and t > 40):
        return "Servidor em alerta"
    return "Servidor estável"