from pathlib import Path
from typing import Optional

import typer

app=typer.Typer()

def main(extension:str,directory:Optional[str]=typer.Argument(None,help="Dossier dans lequel chercher"),delete:bool=typer.Option(False,help="Supprimer les fichiers trouvés")):
    """
    Affiche les fichiers trouvés avec l'extension donné
    :return:
    """
    if not directory:
        directory=Path.cwd()
    else:
        directory=Path(directory)

    #Vérifier si il existes
    if not directory.exists():
        typer.secho(f"Le dossier {directory} n'existe pas.",fg=typer.colors.RED)
        raise  typer.Exit()

    files=directory.rglob(f"*.{extension}")

    if delete:
        typer.confirm("Voulez-vous vraiment supprimez tous les fichiers trouvés?",abort=True)
        for file in files:
            file.unlink()
            typer.secho(f"Suppression du fichier {file}.",fg=typer.colors.RED)
    else:
        typer.secho(f"Fichier trouvés l'extension {extension}",bg=typer.colors.BLUE,fg=typer.colors.BRIGHT_BLUE)
        for file in files:
            typer.echo(file)
if __name__=="__main__":
    typer.run(main)