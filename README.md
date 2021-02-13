# Spammer
Spam your friends on WhatsApp! (**with permission**, of course)        
Run `pip3 install -r requirements.txt` before running spammer.py.
Get geckodriver for your platform.
Requires selenium, geckodriver, firefox and lyricsgenius        

## Usage 

Spammer has two modes, **normal** and **lyrics**.    
Normal mode spams a single message any given number of times.     
Lyrics mode spams the lyrics of any given song - if available on Genius - with each line in a separate message.   

## Syntax

### Normal Mode
python3 spammer.py normal -c 'Target's Whatsapp Name' -m 'Message To Spam' -t 400           
(400 is simply an example)

### Lyrics Mode
python3 spammer.py lyrics -c 'Target's Whatsapp Name' -s 'Song Name'
