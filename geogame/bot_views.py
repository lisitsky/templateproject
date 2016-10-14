"""
Views of Bot sepateated from standard web views.
"""

from telegrambot.bot_views.generic import TemplateCommandView
# import sys
# import traceback
import logging

logger = logging.getLogger(__name__)


class StartView(TemplateCommandView):
    template_text = 'geogame/messages/command_start_text.txt'


class UnknownView(TemplateCommandView):
    template_text = "geogame/messages/command_unknown_text.txt"
