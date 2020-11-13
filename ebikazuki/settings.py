from .settings_common import *


# デバッグモードを有効にするかどうか(本番運用では必ずFalseにする)
DEBUG = False

# 許可するホスト名のリスト
#ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS_EBIKAZUKI')]
ALLOWED_HOSTS = ["*"]

# 静的ファイルを配置する場所
STATIC_ROOT = '/usr/share/nginx/html/ebikazuki/static'
MEDIA_ROOT = '/usr/share/nginx/html/ebikazuki/media'


# ロギング
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        # worksアプリケーションが利用するロガー
        'works': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },

    # ハンドラの設定
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D',  # ログローテーション(新しいファイルへの切り替え)間隔の単位(D=日)
            'interval': 1,  # ログローテーション間隔(1日単位)
            'backupCount': 7,  # 保存しておくログファイル数
        },
    },

    # フォーマッタの設定
    'formatters': {
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

# セキュリティ関連設定
# security.W004
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# security.W006
SECURE_CONTENT_TYPE_NOSNIFF = True
# security.W007
SECURE_BROWSER_XSS_FILTER = True
# security.W008
SECURE_SSL_REDIRECT = True
# security.W012
SESSION_COOKIE_SECURE = True
# security.W016
CSRF_COOKIE_SECURE = True
# security.W019
X_FRAME_OPTIONS = 'DENY'
# security.W021
SECURE_HSTS_PRELOAD = True
