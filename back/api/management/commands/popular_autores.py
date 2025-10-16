import pandas as pd
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from api.models import Autor

class Command(BaseCommand):
    help = "Importa autores de population/autores.csv usando pandas (com limpeza e validação)."

    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default=str(Path("population") / "autores.csv"))
        parser.add_argument("--truncate", action="store_true", help="Apaga todos os autores antes de importar")
        parser.add_argument("--update", action="store_true", help="Faz upsert (update_or_create) em vez de inserir em massa")

    @transaction.atomic 
    # @transaction.atomic  👉 garante que tudo dentro do método será executado dentro de uma única transação de banco. 
    # Se der erro no meio, o Django desfaz tudo (rollback).
    def handle(self, *args, **opts): # é o método principal que o Django executa quando você roda python manage.py popular.
        # *args, **opts: recebe os argumentos/flags passados na linha de comando (ex.: --truncate, --update).
        csv_path = Path(opts["arquivo"]) # pega o caminho do CSV passado por argumento (ou o default definido).
        if not csv_path.exists(): #Se o arquivo não existir, lança um CommandError → o Django mostra a mensagem de erro e interrompe.
            raise CommandError(f"Arquivo não encontrado: {csv_path}")

        # 1) Ler CSV
        df = pd.read_csv(csv_path)

        # 2) Limpeza básica
        for col in ["autor", "s_autor", "nacio"]:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip()
            else:
                df[col] = ""

        if "biogr" not in df.columns:
            df["biogr"] = ""

        df["nasc"] = pd.to_datetime(df.get("nasc"), errors="coerce", format="%Y-%m-%d")
        df["nacio"] = df["nacio"].str.capitalize()

        # 3) Remover vazios/duplicados
        df = df.dropna(how="all")
        df = df.drop_duplicates(subset=["autor", "s_autor", "nasc"], keep="first").reset_index(drop=True)

        # 4) Validar obrigatórios
        obrigatorios = df["autor"].ne("") & df["s_autor"].ne("") & df["nasc"].notna()
        invalidos = df[~obrigatorios] #pega os que não cumprem
        if not invalidos.empty: #Se houver inválidos → mostra aviso e remove do DataFrame.
            self.stdout.write(self.style.WARNING(f"Pulando {len(invalidos)} linha(s) inválida(s)."))

        df = df[obrigatorios]

        #Truncate (limpar tabela antes de importar)
        if opts["truncate"]:#Se o usuário passou --truncate, apaga todos os registros antes de importar.
            self.stdout.write(self.style.WARNING("Limpando tabela api_autor..."))
            Autor.objects.all().delete()

        criados = 0
        atualizados = 0

        if opts["update"]: 
            for row in df.itertuples(index=False):
                obj, created = Autor.objects.update_or_create(
                    autor=row.autor,
                    s_autor=row.s_autor,
                    nasc=row.nasc.date(),
                    defaults={
                        "nacio": row.nacio or None,
                        "biogr": (row.biogr or "").strip() or None,
                    },
                )

                if created:
                    criados += 1
                else:
                    atualizados += 1
        else:
            # Inserção em massa (rápida)
            buffer = []
            for row in df.itertuples(index=False):
                buffer.append(Autor(
                    autor=row.autor,
                    s_autor=row.s_autor,
                    nasc=row.nasc.date(),
                    nacio=row.nacio or None,
                    biogr=(row.biogr or "").strip() or None,
                ))
            Autor.objects.bulk_create(buffer, ignore_conflicts=True)
            criados = len(buffer)

        msg = f"Concluído. Criados: {criados}"
        if opts["update"]:
            msg += f" | Atualizados: {atualizados}"
        self.stdout.write(self.style.SUCCESS(msg))
