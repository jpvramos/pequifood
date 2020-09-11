import pytest

from pequifood.app import create_app


@pytest.fixture("module")
def app():
    """Instance of Main flask app"""    
    return create_app()