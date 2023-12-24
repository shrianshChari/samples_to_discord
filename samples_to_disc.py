import sys
import time

if len(sys.argv) < 2:
    print('''Error: Please provide a file to read samples from!
Run "python samples_to_disc.py -h" for help.''', file=sys.stderr)
    sys.exit(1)

# Help commands
if len({'-h', '--help'}.intersection(set(sys.argv))) > 0:
    print('''USAGE:
    python samples_to_disc.py <name of file> [FLAGS]

FLAGS:
    -h, --help: Display this message
    -d, --discord: Format samples for Discord (default)
    -s, --showdown: Format samples for Pokemon Showdown''')
    sys.exit(0)

inp_file = open(sys.argv[1])
lines = inp_file.readlines()
inp_file.close()

discord_formatting = True
if len({'-s', '--showdown'}.intersection(set(sys.argv))) > 0:
    discord_formatting = False
if len({'-d', '--discord'}.intersection(set(sys.argv))) > 0:
    discord_formatting = True

for line_num, line in enumerate(lines):
    line = line.replace('\n', '')
    split = line.split(': ')

    # First line should be underlined
    if (line_num == 0):
        if discord_formatting:
            print(f'__{line}__')
        else:
            print(f'**{line}**')

    else:
        link = ""
        if (len(split) == 1):
            link = split[0]

        # 'WIP' or 'None' should be left untouched
        elif (split[1] == 'WIP' or split[1] == 'None'):
            link = split[1]

        # Discord invites should not have their embeds suppressed
        elif 'discord.gg' in split[1] or 'discord.com' in split[1]:
            link = split[1]

        # Shortens Smogon thread links so that they don't become super long
        # Suppress their embeds as well
        elif ('https://www.smogon.com/forums/threads/' in split[1]):
            dot_split = split[1].split('.')
            if len(dot_split) == 4:
                thread_number = dot_split[-1]
                link = f'https://www.smogon.com/forums/threads/{thread_number}'
            else:
                link = f'{split[1]}'

            if discord_formatting:
                link = f'<{link}>'

        else:
            link = f'{split[1]}'

            # Suppress embeds for all other links
            if discord_formatting:
                link = f'<{link}>'

        if (len(split) == 1):
            print(f'{link}')
        else:
            print(f'**{split[0]}:** {link}')

print(f'*Last Updated <t:{int(time.time())}:f>*')
