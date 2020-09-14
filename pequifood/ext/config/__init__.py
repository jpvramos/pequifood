def init_app(app):
    app.config["SECRET_KEY"] = "abcd"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///pequifood.db'
    
    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
        app.config["DEBUG_TB_PROFILED_ENABLED"] = True