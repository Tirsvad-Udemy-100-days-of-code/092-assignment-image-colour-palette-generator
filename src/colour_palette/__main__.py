"""!
@file __main__.py
@brief Start the web server: python -m colour_palette [--host HOST] [--port PORT].
"""

import argparse
import logging

from colour_palette.constants import APP_TITLE, DEFAULT_HOST, DEFAULT_PORT
from colour_palette.presentation.web_server import create_server

logger = logging.getLogger("colour_palette")


def main(argv: list[str] | None = None) -> None:
    """!
    @brief Parse the command line and serve until Ctrl+C.
    @param argv Command-line arguments; None reads sys.argv.
    """
    parser = argparse.ArgumentParser(description=APP_TITLE)
    parser.add_argument("--host", default=DEFAULT_HOST, help=f"address to listen on (default {DEFAULT_HOST})")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"port to listen on (default {DEFAULT_PORT})")
    arguments = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    with create_server(arguments.host, arguments.port) as server:
        host, port = server.server_address[:2]
        logger.info("%s running on http://%s:%s (Ctrl+C to stop)", APP_TITLE, host, port)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            logger.info("Stopped")


if __name__ == "__main__":
    main()
