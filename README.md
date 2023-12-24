# Tbolt's SmogCord Resources Formatting Tool
It's a Python script that will turn this:

```
OU Resources
Note that many resources on the forums will be outdated because of the Indigo Disk DLC.
OU Simple Questions and Answers: https://www.smogon.com/forums/threads/simple-questions-simple-answers-thread.3710772/
OU Room on Showdown: https://play.pokemonshowdown.com/overused
OU Discord: https://discord.com/invite/Pgn3Nrb
```

into this:

```
__OU Resources__
Note that many resources on the forums will be outdated because of the Indigo Disk DLC.
**OU Simple Questions and Answers:** <https://www.smogon.com/forums/threads/3710772/>
**OU Room on Showdown:** <https://play.pokemonshowdown.com/overused>
**OU Discord:** https://discord.com/invite/Pgn3Nrb
*Last Updated <t:1702567467:f>*
```

### Prerequisites
- You'll need to have [Python 3.6 or later](https://www.python.org/) installed.
- You also need to be know how to run Python scripts on the [command line](https://realpython.com/run-python-scripts/#how-to-run-python-scripts-from-the-command-line)

### How to use
1. Edit the file to add or remove resources.
2. Run `python samples_to_disc.py <filename>` where `<filename>` represents the file whose command you want to update.
3. Copy the output of this Python program.
4. In the Smogon Discord, type `/custom edit` and hit <kbd>Enter</kbd>.
5. Type the name of the command you want to update (it should match the name of the file you just edited). If you're not sure what commands there are, check the "Chatot Bot Commands" thread of the "#comp-read-me" forum channel.
6. Delete the "Prints" part of the command and paste in the output of the Python program that you copied earlier.
7. Hit "Submit" and now it should work!

### Notes
- First line of the file is treated as the title and has an underline.
- Each line can be separated into a "Resource Name: Link" format. The "Resource Name" part is bolded and the link is modified so that Smogon threads aren't as long and most websites (except for Discord invites) cannot display embeds for conciseness.
- If a line doesn't follow this format, it is left untouched.
- Finally, it gives a timestamp to signify when the command was run, to give a sense of when the resources were last updated.
