### Acció 3.1: Creació del directori i estructura inicial de Git
Es crea el directori del projecte i s'inicialitza un repositori Git buit per començar el rastreig forense.
```bash
git init
```

### Acció 3.2: Configuració d'identitat
Es configuren les credencials locals de Git per identificar l'enginyer/a forense que realitza les accions.
```bash
git config user.name "Pol.C-FP"
git config user.email "alu.pol.castano@mataro.epiaedu.cat"
```

### Acció 3.3: Generació del fitxer base (1r Commit)
Es crea el fitxer principal `main.py` amb el codi inicial d'encesa del servidor i es registra el primer commit.
```bash
git add .
git commit -m "Initial Commit: Creation of script main.py"
```