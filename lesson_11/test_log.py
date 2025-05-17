from logger import logger

def count_a(text, char):
    logger.debug(f"Text fomat is string: {isinstance(text, str)}")
    count = text.count(char)
    logger.debug(f"Sub string {char} in {text}: {count}")
    
    # Логування подій різного рівня (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.debug('Це повідомлення рівня DEBUG') # 10
    logger.info('Це повідомлення рівня INFO') # 20
    logger.warning('Це повідомлення рівня WARNING') # 30
    logger.error('Це повідомлення рівня ERROR') # 40
    logger.critical('Це повідомлення рівня CRITICAL') # 50
    return count

logger.info(count_a("sdsdsadsadsa", "s"))
count_a("fdjfueehfjskd", "s")
count_a("38473298723", "732")