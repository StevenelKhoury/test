from django.conf import settings
from django.shortcuts import redirect, render

from django_telegram_login.widgets.constants import (
    SMALL,
    MEDIUM,
    LARGE,
    DISABLE_USER_PHOTO,
)
from django_telegram_login.widgets.generator import (
    create_callback_login_widget,
    create_redirect_login_widget,
)


bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

telegram_login_widget = create_callback_login_widget(
    bot_name, corner_radius=10, size=MEDIUM
)

telegram_login_widget = create_redirect_login_widget(
    redirect_url, bot_name, size=LARGE, user_photo=DISABLE_USER_PHOTO
)

def create_redirect_login_widget(
        redirect_url, bot_name, size=SMALL, user_photo=True, access_write=True
):
    """
    Create a redirect widget, that allows to handle an user data as get request params.
    """
    script_initital = \
        '<script async src="https://telegram.org/js/telegram-widget.js?2" '
    bot = 'data-telegram-login="{}" '.format(bot_name)
    size = 'data-size="{}" '.format(size)
    userpic = \
        'data-userpic="{}" '.format(str(user_photo).lower()) if not user_photo else ''
    redirect = 'data-auth-url="{}" '.format(redirect_url)
    access = 'data-request-access="write"' if access_write else ''
    script_end = '></script>'

    widget_script = \
        script_initital + bot + size + userpic + redirect + access + script_end
    return widget_script


def callback(request):
    telegram_login_widget = create_callback_login_widget(bot_name, size=SMALL)

    context = {'telegram_login_widget': telegram_login_widget}
    return render(request, 'connexion/callback.html', context)


def testGet(request):
    return redirect('https://api.telegram.org/bot1790922238:AAEKlLJMuYNrva1bDsT2mmxHZNY_4okroJM/getMe')


def testUpdate(request):
    return redirect('https://api.telegram.org/bot1790922238:AAEKlLJMuYNrva1bDsT2mmxHZNY_4okroJM/updatesMe')

