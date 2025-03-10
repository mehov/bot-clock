## bot-clock

Simple Telegram bot that sends you a message with the current time.

Use it to test setting up bots that work in the background in a cloud / app service environment.

## Creating a new bot in Telegram

1. Create a Telegram bot through [@BotFather](https://t.me/BotFather). Once done, you will get the following message
    
    > Done! Congratulations on your new bot. (…)
    > 
    > Use this token to access the HTTP API:
    > 
    > `123456789:…`
    > 
    > Keep your token secure and store it safely, it can be used by anyone to control your bot.

    Note the token.

2. Still in Telegram, open your newly created bot and send it a message.
    
    Then in your web browser, go to `https://api.telegram.org/bot{token}/getUpdates`. Replace `{token}` with that from the previous step. You should get a JSON response with your message and a Chat ID under `result.0.message.chat.id`. Note the Chat ID.

Here's a good guide: https://gist.github.com/nafiesl/4ad622f344cd1dc3bb1ecbe468ff9f8a

## Deploying the code

1. In your cloud dashboard, create a new project using this Github repository. Fork it if you have to.
2. Open the newly created project and go to Environment settings. Set the following variables:
    - `TELEGRAM_BOT_TOKEN`: the above token
    - `TELEGRAM_CHAT_ID`: the above chat ID
    - `HTTP_PORT`: port to bind Flask app to; defaults to `80`
    - `HTTP_IP`: IP to bind Flask app to; defaults to `0.0.0.0`
3. Set up CRON to trigger the bot. Go to *Startup Command* and set `sh setup.sh {hostname}`, where `{hostname}` is assigned to your project by the cloud environment. For example:
    - `example.onrender.com`
    - `example.azurewebsites.net`
   If you can't set the *Startup Command* where you're deploying your bot, log on to the SSH terminal and run the `setup.sh` script manually.
4. Deploy the bot. It will be triggered by an incoming HTTP request every 10 minutes. This will send you a message with the current time and keep the app alive.

Tested with:

- [render.com](https://render.com) (free tier)