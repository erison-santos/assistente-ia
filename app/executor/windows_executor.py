import subprocess

APPLICATIONS = {
    "edge": "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    "microsoft edge": "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    "notepad": "notepad.exe",
    "bloco de notas": "notepad.exe",
    "calculadora": "calc.exe",
    "visual studio code": "code.exe",
    "vscode": "code.exe",
    "chrome": "chrome.exe",
    "google chrome": "chrome.exe",
    "firefox": "firefox.exe",
    "terminal": "cmd.exe",
    "prompt de comando": "cmd.exe",
    "powershell": "powershell.exe"
}

class WindowsExecutor:
    def open_application(self, target: str):
        target = target.lower().strip()

        application = APPLICATIONS.get(target)

        if not application:
            return False, f"Aplicativo '{target}' não encontrado."

        try:
            subprocess.Popen(application)
            return True, f"Abrindo {target}..."

        except Exception as error:
            return False, f"Erro ao abrir {target}: {str(error)}"

    def execute(self, intent):
        if intent.intent == "open_application":
            return self.open_application(intent.target)

        return False, f"Intenção não reconhecida: {intent.intent}."

