# py-runner
![Py-Runner](graphics/For_README/image-readme.png)

# LANCEMENT DU PROJET
---

## Prérequis
---
1. Installez Python à partir de [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Installez VS Code à partir de [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
3. (Optionnel) Installez l'extension Python pour VS Code à partir de [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## INSTALLATION DES ENVIRONNEMENTS NECESSAIRES
---
```
pip install python-pygame
pip install python-dotenv
```

## LANCEMENT DU JEU
---
Depuis le terminal

```
python3 main.py
```

## EXECUTABLE (Pour linux)
---
### Installation de pyinstaller

```
pip install pyinstaller
```

Depuis la racine du projet
```
pyinstaller --onefile main.py

// dans mon cas il ne trouvait pas un fichier, j'ai donc du taper la commande suivante:

pyinstaller --onefile --name <nom personnalise> --add-data 'font/Pixeltype.ttf:.' main.py
```

Cette commande va creer un dossier **dist** a l'interieur duquel se trouvera le fichier main (du meme nom que le fichier que vous rendez executable).

Vous pouvez maintenant lancer le jeu depuis l'executable
```
// depuis la racine du projet: 

./dist/main
```

Il ne vous reste plus qu'a prendre du plaisir

# LANCEMENT DU JEU APRES LA PREMIERE UTILISATION

Si l'environnement n'existe pas:
```
python3 -m venv myenv
```
Apres avoir creer l'environnement (ou s'il existe deja)

```
source myenv/bin/activate
```
La ligne du terminal contiendra l'information suivante:

![environnement](graphics/For_README/capture-readme.png)