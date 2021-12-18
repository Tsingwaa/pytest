import logging


def set_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s: %(levelname)s:'
        ' [%(filename)s:%(lineno)d]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    # Save log to file
    file_handler = logging.FileHandler('a.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    # print to the screen
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    # stream_handler.setFormatter(formatter)
    # add two handler to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


if __name__ == '__main__':
    logger = set_logger()
    logger.info('info')
    logger.debug('debug')
    logger.warning('warn')
