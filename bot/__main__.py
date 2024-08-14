#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Shrimadhav U K
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler
)
from bot import (
    Config,
    INPUT_PHONE_NUMBER,
    INPUT_TG_CODE
)
from bot.modules.start_text_ import start
from bot.modules.my_telegram_org.input_phone_number_ import (
    input_phone_number
)
from bot.modules.my_telegram_org.input_tg_code_ import (
    input_tg_code
)


def main():
    """ Initial Entry Point """
    # Create the Application and pass it your bot's token.
    application = Application.builder(
    ).token(
        Config.TG_BOT_TOKEN
    ).build()

    # Add conversation handler with the states
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start)
        ],

        states={
            INPUT_PHONE_NUMBER: [MessageHandler(
                filters.TEXT | filters.CONTACT,
                input_phone_number
            )],

            INPUT_TG_CODE: [MessageHandler(
                filters.TEXT,
                input_tg_code
            )],
        },

        fallbacks=[CommandHandler("start", start)]
    )

    application.add_handler(conv_handler)

    # log all errors
    # application.add_error_handler(error)

    print(
        "Bot Starting: BOSSSSSSSS"
    )

    # Start the Bot
    if Config.WEBHOOK:
        application.run_webhook(
            listen="0.0.0.0",
            port=Config.PORT,
            url_path=Config.TG_BOT_TOKEN
        )
        # Manually set a webhook, afterwards
        # # https://t.me/c/1186975633/22915
        # await application.bot.set_webhook(
        #     url=Config.URL + Config.TG_BOT_TOKEN
        # )
    else:
        # Run the bot until the user presses Ctrl-C
        application.run_polling()

main()
