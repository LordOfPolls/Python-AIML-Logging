import logging
import colorlog

def get_module_logger(mod_name):
    logger = logging.getLogger(mod_name)
    fmt = "%(log_color)s[%(levelname)s] %(name)s: %(message)s"
    date_format = '%Y-%m-%d %H:%M:%S'
    fmt = colorlog.ColoredFormatter(fmt, date_format,
                                    log_colors={'DEBUG': 'cyan', 'INFO': 'reset',
                                                'WARNING': 'bold_yellow', 'ERROR': 'bold_red',
                                                'CRITICAL': 'bold_red'})
    handler = logging.StreamHandler()
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger