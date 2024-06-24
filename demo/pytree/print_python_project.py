from octk import pytree

test_path = r'.'

tree = pytree.FileTree(
    pytree.Path(test_path),
    exclude_extensions=[".pyc", ".pyo", ".pyd", ".pyi", ".pyw", ".pyz", ".pywz", ".pyzw"],
    exclude_dirs=[
        "__pycache__", ".git", ".idea", ".vscode", ".pytest_cache", "venv", 
        "env", "build", "dist", "node_modules", "site-packages", "dist-packages", 
        "egg-info", "logs", "tmp", "temp", "tmpfs", "tempfs", "tempfs", "tmp",
        ],
    space="    ",
    branch="    ",
    tee="- ",
    last="- "
)

print(tree)