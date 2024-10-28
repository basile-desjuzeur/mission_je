# Utiliser une image Windows Server Core avec Python préinstallé
# Remplacez par l'image Windows souhaitée
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Installer Python (si non inclus dans l'image)
RUN powershell -Command \
    Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe -OutFile python.exe; \
    Start-Process python.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -NoNewWindow -Wait; \
    Remove-Item -Force python.exe

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application dans le conteneur
COPY . .

