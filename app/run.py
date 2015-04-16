import argparse
from app import app
from configuration import ProductionConfig
from configuration import StagingConfig
from configuration import DevelopmentConfig


# Constants
DESCRIPTION = "A commandline interface for selecting the configuration file."
EPILOG = "See configuration.py for specific configuration details."
DEVELOPMENT = "Development configuration"
STAGING = "Staging configuration"
PRODUCTION = "Production configuration"


def set_config(args):
    """
    A function to select a config option.
    """
    if args.dev:
        print("dev")
        app.config.from_object(DevelopmentConfig)
    elif args.stage:
        print("stage")
        app.config.from_object(StagingConfig)
    elif args.prod:
        print("prod")
        app.config.from_object(ProductionConfig)
    else:
        print("The default configuration is DevelopmentConfig.\n")
        app.config.from_object(DevelopmentConfig)
    return app


if __name__ == "__main__":

    # Command line logic
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)

    # This prevents users from passing multiple options at once
    group1 = parser.add_mutually_exclusive_group()

    # Adds the commandline options
    group1.add_argument("-dev", "--development", dest="dev",
                        action="store_true", help=DEVELOPMENT)

    group1.add_argument("-stage", "--staging", dest="stage",
                        action="store_true", help=STAGING)

    group1.add_argument("-prod", "--production", dest="prod",
                        action="store_true", help=PRODUCTION)

    # Dictionary with the commandline inputs
    args = parser.parse_args()

    configured_app = set_config(args)

    if configured_app:
        configured_app.run('localhost', port=5000)
