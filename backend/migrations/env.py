import logging
from logging.config import fileConfig

from flask import current_app
from alembic import context
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend import create_app

def init_alembic_config():
    app = create_app()

    config = context.config

    fileConfig(config.config_file_name)
    logger = logging.getLogger('alembic.env')

    with app.app_context(): 
        # Obtener la configuración de la conexión
        engine_url = str(app.extensions['migrate'].db.engine.url).replace('%', '%%')
        config.set_main_option('sqlalchemy.url', engine_url)
        
        # Establecer los metadatos objetivo
        target_metadata = app.extensions['migrate'].db.metadata
        
        # Configurar las opciones adicionales
        conf_args = app.extensions['migrate'].configure_args
        
        def process_revision_directives(context, revision, directives):
            if getattr(config.cmd_opts, 'autogenerate', False):
                script = directives[0]
                if script.upgrade_ops.is_empty():
                    directives[:] = []
                    logger.info('No changes in schema detected.')
                    
        if conf_args.get("process_revision_directives") is None:
            conf_args["process_revision_directives"] = process_revision_directives

        return {
            'target_metadata': target_metadata,
            **conf_args
        }

# Llamar al inicializador con el contexto establecido
alembic_cfg = init_alembic_config()
