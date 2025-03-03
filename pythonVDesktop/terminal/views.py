from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import subprocess
from django.views.decorators.csrf import csrf_exempt
import json
import os

#Affichage du terminal
def affiche_terminal(request):
    return render(request, 'terminal/templates/terminal_page.html')

def run_command(command):
    if command == "commands help":
            commands_list = get_available_commands()
            return commands_list
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

@csrf_exempt
def execute_command(request):
    try:
        data = json.loads(request.body)  # Charger le JSON envoyé par fetch
        command = data.get('command', '')  # Récupérer la commande

        output = run_command(command)  # Exécuter la commande
        return JsonResponse({'output': output})  # Retourner le résultat

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    

def get_available_commands():
    """ Retourne une liste de commandes utiles en fonction du système d'exploitation """
    if os.name == "nt":  # Windows
        return [
            "dir", "cls", "echo", "cd", "mkdir", "rmdir", "del",
            "ipconfig", "ping", "tasklist", "taskkill", "netstat",
            "whoami", "hostname", "systeminfo", "shutdown",
        ]
    else:  # Linux / macOS
        return [
            "ls", "clear", "echo", "cd", "mkdir", "rm -r", "cat",
            "ip a", "ping", "ps aux", "kill", "netstat -tulnp",
            "whoami", "hostname", "uname -a", "uptime",
        ]
