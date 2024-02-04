def pytest_addoption(parser):
    parser.addoption(
        "--longrun",
        action="store_true",
        dest="longrun",
        default=False,
        help="enable longrundecorated tests",
    )


def pytest_configure(config):
    if not config.option.longrun and not config.option.markexpr:
        setattr(config.option, "markexpr", "not longrun")
