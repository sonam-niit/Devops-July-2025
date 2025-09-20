import logging

# logging.basicConfig(level=logging.DEBUG)
# By Default the log level is Warning

logging.basicConfig(
    filename="app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    # level=logging.DEBUG
)

#Log messages
logging.debug("This is Debug Message")
logging.info("This is Info Message")
logging.warning("This is a warning")
logging.critical("This is Critical Message")
logging.error("This is Error Message")

# seq
# Debug < info < warning < error <critical 