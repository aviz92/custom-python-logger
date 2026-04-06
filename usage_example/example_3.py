from custom_python_logger import get_logger
from usage_example.example_1 import main

if __name__ == "__main__":
    logger = get_logger(__name__)

    main()

    logger.info("Finish the example...")
