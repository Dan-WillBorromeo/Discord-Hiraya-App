# Hiraya App

This is a Discord application made for the purpose of rolling dice in various TTRPG systems I enjoy running. Currently, it has the following systems as dice bots:
- SHIVER

It does NOT:
- manage clocks
- manage character sheets

# Programming Languages used
- Python
## Dependencies:
- discord.py
- python-dotenv
- pillow

# Bot syntax
## SHIVER specific: !shiver {expression}
- {expression} takes on the form of Xsd Ytd (min|maj) (dis|adv); everything after Xsd is optional
- X and Y can never be lower than 1
