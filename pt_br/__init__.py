import platform
import locale


if platform.system() == "Windows":
    LOCALE = "ptb_bra"
else:
    LOCALE = "pt_BR"

locale.setlocale(locale.LC_ALL, LOCALE)