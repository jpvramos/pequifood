def test_app_is_created(app):
    assert app.name == 'pequifood.app'
    
    
def test_config_is_loader(config):
    assert config["DEBUG"] == False
    
    
def test_request_returns(client):
    assert client.get("/url_nao_existe").status_code == 404
    