def init_app(app):
    app.config["SECRET_KEY"] = "abcd"
    
    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
        app.config["DEBUG_TB_PROFILED_ENABLED"] = True