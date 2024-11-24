import os  
import logging.config  

# Путь к директории для логов  
LOG_DIR = os.path.join(BASE_DIR, 'logs')  

# Создаем директорию для логов, если её нет  
if not os.path.exists(LOG_DIR):  
    os.makedirs(LOG_DIR)  

# Конфигурация логирования  
LOGGING = {  
    'version': 1,  
    'disable_existing_loggers': False,  
    'formatters': {  
        'console': {  
            'format': '{levelname} {asctime} {message} {pathname}',  
            'datefmt': '%Y-%m-%d %H:%M:%S',  
            'style': '{',  
        },  
        'general': {  
            'format': '{asctime} {levelname} {module} {message}',  
            'datefmt': '%Y-%m-%d %H:%M:%S',  
            'style': '{',  
        },  
        'errors': {  
            'format': '{asctime} {levelname} {message} {pathname}',  
            'datefmt': '%Y-%m-%d %H:%M:%S',  
            'style': '{',  
        },  
        'security': {  
            'format': '{asctime} {levelname} {module} {message}',  
            'datefmt': '%Y-%m-%d %H:%M:%S',  
            'style': '{',  
        },  
    },  
    'filters': {  
        'console_debug': {  
            '()': 'django.utils.log.CallbackFilter',  
            'callback': lambda record: DEBUG,  # вывод в консоль только если DEBUG = True  
        },  
        'file_general_filter': {  
            '()': 'django.utils.log.CallbackFilter',  
            'callback': lambda record: not DEBUG,  # вывод только при DEBUG = False  
        },  
        'email_filter': {  
            '()': 'django.utils.log.CallbackFilter',  
            'callback': lambda record: not DEBUG,  # на почту только при DEBUG = False  
        },  
    },  
    'handlers': {  
        'console': {  
            'level': 'DEBUG',  
            'filters': ['console_debug'],  
            'class': 'logging.StreamHandler',  
            'formatter': 'console',  
        },  
        'file_general': {  
            'level': 'INFO',  
            'filters': ['file_general_filter'],  
            'class': 'logging.FileHandler',  
            'filename': os.path.join(LOG_DIR, 'general.log'),  
            'formatter': 'general',  
        },  
        'file_errors': {  
            'level': 'ERROR',  
            'class': 'logging.FileHandler',  
            'filename': os.path.join(LOG_DIR, 'errors.log'),  
            'formatter': 'errors',  
        },  
        'file_security': {  
            'level': 'DEBUG',  
            'class': 'logging.FileHandler',  
            'filename': os.path.join(LOG_DIR, 'security.log'),  
            'formatter': 'security',  
        },  
        'mail_admins': {  
            'level': 'ERROR',  
            'filters': ['email_filter'],  
            'class': 'django.utils.log.AdminEmailHandler',  
            'formatter': 'errors',  # На почту отправляем в формате errors, но без exc_info  
        },  
    },  
    'loggers': {  
        'django': {  
            'handlers': ['console', 'file_general'],  
            'level': 'DEBUG',  
            'propagate': True,  
        },  
        'django.request': {  
            'handlers': ['file_errors', 'mail_admins'],  
            'level': 'ERROR',  
            'propagate': False,  
        },  
        'django.server': {  
            'handlers': ['file_errors', 'mail_admins'],  
            'level': 'ERROR',  
            'propagate': False,  
        },  
        'django.template': {  
            'handlers': ['file_errors'],  
            'level': 'ERROR',  
            'propagate': False,  
        },  
        'django.db.backends': {  
            'handlers': ['file_errors'],  
            'level': 'ERROR',  
            'propagate': False,  
        },  
        'django.security': {  
            'handlers': ['file_security'],  
            'level': 'DEBUG',  
            'propagate': False,  
        },  
    },  
}  


LOGGING['loggers'].update(logging.getLogger('django').manager.loggerDict)