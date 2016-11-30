import json
import asyncio
import random


async def dadjoke(cmd, message, args):
    with open(cmd.resource('dadjokes.json'), 'r', encoding='utf-8') as dadjokes_file:
        jokes = dadjokes_file.read()
        jokes = json.loads(jokes)
        joke_list = jokes['JOKES']
        end_joke_choice = random.choice(joke_list)
        end_joke = (end_joke_choice['setup'])
        punchline = ('\n\n' + end_joke_choice['punchline'])

        find_data = {
            'Role': 'Stats'
        }
        find_res = cmd.db.find('Stats', find_data)
        count = 0
        for res in find_res:
            try:
                count = res['CancerCount']
            except:
                count = 0
        new_count = count + 1
        updatetarget = {"Role": 'Stats'}
        updatedata = {"$set": {"CancerCount": new_count}}
        cmd.db.update_one('Stats', updatetarget, updatedata)

        joke_msg = await cmd.bot.send_message(message.channel, 'I can\'t believe I\'m doing this...\n```' + end_joke + '```')
        await asyncio.sleep(3)
        await cmd.bot.edit_message(joke_msg, 'I can\'t believe I\'m doing this...\n```' + end_joke + punchline + '```')
