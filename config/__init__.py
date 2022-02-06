# coding: UTF-8
import os


def load_config(mode=os.environ.get('FLASK_ENV')):
    """Load config."""
    try:
        if mode:
            mode = mode.upper()
        if mode == 'PRODUCTION':
            from .production import ProductionConfig
            return ProductionConfig
        elif mode == 'TESTING':
            from .test import TestConfig
            return TestConfig
        else:
            from .development import DevelopmentConfig
            return DevelopmentConfig
    except ImportError:
        from .default import DefaultConfig
        return DefaultConfig
