from src.integration.illegal_xs_module import xs_only


def bad_access() -> str:
    return xs_only()
