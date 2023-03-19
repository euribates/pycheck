set dotenv-load := true

# Mustra información del S.O., arquitectura, software y hardware
@info:
    echo "OS: {{os()}} / {{os_family()}}"
    echo "Arch: This is an {{arch()}} machine"
    python -c "import sys; print('Python:', sys.version.split()[0])"
    echo "Uptime:" `uptime`

# Eliminar ficheros temporales y de caché
clean:
    find . -type d -name "__pycache__" -exec rm -r "{}" +
    find . -type d -name ".mypy_cache" -exec rm -r "{}" +
    find . -type f -name "*.pyc" -delete
    find . -type f -name "*.pyo" -delete

