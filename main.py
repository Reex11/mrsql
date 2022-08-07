import os
import sys
import time

from pprint import pprint
from InquirerPy import prompt, inquirer, get_style
from InquirerPy.base.control import Choice
import pyperclip
from colored import fg, bg, attr

from sqlninja import engine as sqlninja
from wizards import *
import wizards

def mrsql():
    print("%s\n                                               \n  ███    ███ ██████  ███████  ██████  ██       \n  ████  ████ ██   ██ ██      ██    ██ ██       \n  ██ ████ ██ ██████  ███████ ██    ██ ██       \n  ██  ██  ██ ██   ██      ██ ██ ▄▄ ██ ██       \n  ██      ██ ██   ██ ███████  ██████  ███████  \n                               ▀▀              %s" % (fg(2), attr(0)))

def answers(field):
    try:
        return answers[field]
    except:
        return 'undefiend'

style_ = {"questionmark": "#ffaa00", "question": "#ffff00", "answer": "#33ff33","pointer": "#33ff33"}
style = get_style(style_, style_override=True)
c_title = fg('dodger_blue_2') + attr('bold')
c_desc = fg('dodger_blue_2')
c_res = attr('reset')

wizard_list = []

for wizard in wizards.__all__:
    mod = sys.modules.get('wizards.'+wizard)
    getattr(mod, "title",None)
    wizard_list.append(mod)

choices = []
for i,wizard in enumerate(wizard_list):
    choices.append(Choice(i, name=wizard.title))


#############################################################################

while(1):
    
    while(1):
        os.system('cls')
        mrsql()

        print("%s%s  MRSQL | A jinja powered SQL generator %s" % (fg(3),attr(1),attr(0)))
        print("%s  Developed by: Abdulmalik Almushaiqah %s" % (fg(3),attr(0)))

        print("    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \n")

        selected = inquirer.select(message="Select a template:", style=style,
                choices=choices).execute()

        os.system('cls')
        mrsql()
        print("  "+c_title+wizard_list[selected].title+c_res)
        print("  "+wizard_list[selected].desc)
        print("    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \n")

        continue_ = inquirer.confirm(message="Do you want to use this template?",default=True, style=style).execute()

        if continue_:
            break


    os.system('cls')
    mrsql()
    print("  "+c_title+wizard_list[selected].title+c_res)
    print("  "+wizard_list[selected].desc)
    print("    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \n")
    answers = prompt(wizard_list[selected].questions, style=style_)

    query = wizard_list[selected].query(answers)


    print("")
    pyperclip.copy(query)
    print("%s  ✅ The query was generated successfully! 🥳%s" % (fg(2),attr(0)))
    print("%s     [ The query is copied to your clipboard ] %s" % (fg(24),attr(0)))
    print("")

    print_ = inquirer.confirm(message="- Do you want to display the query?",style=style)
    print_ = print_.execute()
    if (print_):
        os.system('cls')
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(query)
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        inquirer.confirm(message="PRESS ANY KEY TO RETURN TO MAIN MENU").execute()