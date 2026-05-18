from custom_python_logger import build_logger
from usage_example.example_1 import main

if __name__ == "__main__":
    logger = build_logger(
        project_name="xxxxx",
        log_file=True,
        # extra={'user': 'test_user'}
    )

    main()

    import logging

    import urllib3

    ulog = logging.getLogger("urllib3")
    ulog.setLevel(logging.DEBUG)

    urllib3.PoolManager().request("GET", "https://httpbin.org/get")

    logger.info("Finish the example...")
