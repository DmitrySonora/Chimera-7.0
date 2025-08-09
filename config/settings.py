import os
from dotenv import load_dotenv

load_dotenv()

# Отключаем предупреждения от HuggingFace tokenizers
os.environ["TOKENIZERS_PARALLELISM"] = "false"


# ========================================
# ЛИМИТЫ ДЛЯ ДЕМО-ДОСТУПА
# ========================================

DAILY_MESSAGE_LIMIT = 10  # Количество сообщений в день для неавторизованных



# ========================================
# BACKEND-НАСТРОЙКИ
# ========================================

# Actor System настройки
ACTOR_SYSTEM_NAME = "chimera"
ACTOR_MESSAGE_QUEUE_SIZE = 1000     # Макс. размер очереди сообщений
ACTOR_SHUTDOWN_TIMEOUT = 5.0        # Секунды
ACTOR_MESSAGE_TIMEOUT = 1.0         # Таймаут ожидания сообщения в message loop

# Retry настройки
ACTOR_MESSAGE_RETRY_ENABLED = True  # Включить retry механизм
ACTOR_MESSAGE_MAX_RETRIES = 3       # Макс. количество попыток
ACTOR_MESSAGE_RETRY_DELAY = 0.1     # Начальная задержка между попытками (сек)
ACTOR_MESSAGE_RETRY_MAX_DELAY = 2.0 # Макс. задержка между попытками (сек)

# Circuit Breaker настройки
CIRCUIT_BREAKER_ENABLED = True          # Включить Circuit Breaker
CIRCUIT_BREAKER_FAILURE_THRESHOLD = 5   # Количество ошибок для открытия
CIRCUIT_BREAKER_RECOVERY_TIMEOUT = 60   # Время восстановления в секундах

# Логирование
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# JSON логирование
ENABLE_JSON_LOGGING = True  # Включить JSON логирование параллельно с текстовым
JSON_LOG_FILE = "logs/chimera.json"  # Путь к файлу JSON логов

# Ротация логов
LOG_ROTATION_ENABLED = True  # Включить ротацию файлов логов
LOG_MAX_BYTES = 1 * 1024 * 1024  # Макс. размер файла логов (1 МБ)
LOG_BACKUP_COUNT = 5  # Количество архивных файлов логов

# Мониторинг
ENABLE_PERFORMANCE_METRICS = True
METRICS_LOG_INTERVAL = 60  # Секунды
SLOW_OPERATION_THRESHOLD = 0.1  # Порог для медленных операций (секунды)

# Dead Letter Queue настройки
DLQ_MAX_SIZE = 1000  # Макс. размер очереди перед автоочисткой
DLQ_CLEANUP_INTERVAL = 3600  # Интервал очистки в секундах (1 час)
DLQ_METRICS_ENABLED = True  # Включить метрики DLQ

# Event Store настройки
EVENT_STORE_TYPE = "postgres"              # Тип хранилища ("postgres" или "memory")
EVENT_STORE_MAX_MEMORY_EVENTS = 10000    # Макс. событий в памяти
EVENT_STORE_STREAM_CACHE_SIZE = 100      # Размер LRU кэша потоков
EVENT_STORE_CLEANUP_INTERVAL = 3600      # Интервал очистки старых событий (сек)
EVENT_STORE_CLEANUP_BATCH_SIZE = 100     # Размер батча при очистке

# Сериализация событий
EVENT_SERIALIZATION_FORMAT = "json"
EVENT_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"



# ========================================
# EVENT ARCHIVAL & STORAGE MONITORING
# ========================================

# Event Archival settings
ARCHIVE_ENABLED = True                        # Enable automatic archival
ARCHIVE_DAYS_THRESHOLD = 90                   # Archive events older than X days
ARCHIVE_BATCH_SIZE = 1000                     # Number of events to archive in one batch
ARCHIVE_COMPRESSION_LEVEL = 6                 # gzip compression level (1-9, 6 is balanced)
ARCHIVE_SCHEDULE_HOUR = 4                     # Hour to run archival (UTC)
ARCHIVE_SCHEDULE_MINUTE = 0                   # Minute to run archival
ARCHIVE_QUERY_TIMEOUT = 30.0                  # Timeout for archival queries (seconds)
ARCHIVE_DRY_RUN = False                       # If True, only log what would be archived

# Storage Monitoring settings
STORAGE_MONITORING_ENABLED = True             # Enable storage size monitoring
STORAGE_CHECK_INTERVAL = 3600                 # Check interval in seconds (1 hour)
STORAGE_ALERT_THRESHOLD_MB = 1000            # Warning threshold in MB
STORAGE_CRITICAL_THRESHOLD_MB = 5000         # Critical threshold in MB
STORAGE_GROWTH_WINDOW_DAYS = 7               # Days to analyze for growth prediction
STORAGE_GROWTH_ALERT_THRESHOLD = 1.5         # Alert if predicted to grow >50% in window
STORAGE_METRICS_LOG_INTERVAL = 86400         # Log storage metrics every 24 hours

# SystemActor settings
SYSTEM_ACTOR_ENABLED = True                   # Enable SystemActor
SYSTEM_METRICS_CACHE_TTL = 300               # Cache metrics for 5 minutes
SYSTEM_ALERT_COOLDOWN = 3600                 # Don't repeat same alert for 1 hour



# ========================================
# ПАРАМЕТРЫ EVENT REPLAY SERVICE
# ========================================

# Event Replay Service settings
EVENT_REPLAY_MAX_EVENTS = 10000        # Максимум событий за один запрос
EVENT_REPLAY_BATCH_SIZE = 5000         # Размер батча для чтения
EVENT_REPLAY_DEFAULT_PERIOD_DAYS = 7   # Период по умолчанию
EVENT_REPLAY_CACHE_TTL = 300          # TTL для кэширования метрик (сек)

# Emotional Analysis Settings
ANALYSIS_CACHE_TTL_DAYS = 30
ANALYSIS_CACHE_TABLE = "emotional_analysis_cache"
ANALYSIS_MAX_EVENTS_PER_USER = 10000
ANALYSIS_BATCH_SIZE = 500

# Clustering parameters
CLUSTERING_MIN_K = 3
CLUSTERING_MAX_K = 10
CLUSTERING_SILHOUETTE_THRESHOLD = 0.5

# Pattern detection
PATTERN_MIN_FREQUENCY = 3
PATTERN_MIN_CONFIDENCE = 0.7
TEMPORAL_WINDOW_MINUTES = 30

# Anomaly detection
ANOMALY_CONTAMINATION = 0.05  # 5% expected anomalies
ANOMALY_Z_SCORE_THRESHOLD = 3.0

# Cycle detection
CYCLE_MIN_PERIOD_DAYS = 3
CYCLE_MAX_PERIOD_DAYS = 30
CYCLE_MIN_AMPLITUDE = 0.2


# ========================================
# POSTGRESQL EVENT STORE
# ========================================

# PostgreSQL подключение
POSTGRES_DSN = os.getenv("POSTGRES_DSN", 
    "postgresql://chimera_user:password@localhost:5432/chimera_db")
POSTGRES_POOL_MIN_SIZE = 10        # Минимальный размер пула подключений
POSTGRES_POOL_MAX_SIZE = 20        # Максимальный размер пула подключений
POSTGRES_COMMAND_TIMEOUT = 60      # Таймаут команд в секундах
POSTGRES_CONNECT_TIMEOUT = 10      # Таймаут подключения в секундах
POSTGRES_RETRY_ATTEMPTS = 3        # Количество попыток переподключения
POSTGRES_RETRY_DELAY = 1.0         # Задержка между попытками в секундах

# Батчевая запись событий
EVENT_STORE_BATCH_SIZE = 100       # Размер батча для записи
EVENT_STORE_FLUSH_INTERVAL = 1.0   # Интервал автоматического flush в секундах
EVENT_STORE_MAX_BUFFER_SIZE = 1000 # Максимальный размер буфера записи

# Миграция данных
EVENT_STORE_MIGRATION_BATCH = 1000 # Размер батча при миграции
EVENT_STORE_MIGRATION_DELAY = 0.1  # Задержка между батчами миграции (сек)
EVENT_STORE_MIGRATION_VERIFY = True # Верифицировать данные после миграции

# Advisory lock настройки
USE_DOUBLE_KEY_ADVISORY_LOCK = True  # Использовать два ключа для уменьшения коллизий



# ========================================
# REDIS
# ========================================

# Redis подключение
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
REDIS_POOL_MIN_SIZE = 5         # Минимальный размер пула подключений
REDIS_POOL_MAX_SIZE = 10        # Максимальный размер пула подключений
REDIS_CONNECT_TIMEOUT = 5       # Таймаут подключения в секундах
REDIS_RETRY_ATTEMPTS = 3        # Количество попыток подключения
REDIS_RETRY_DELAY = 1.0         # Задержка между попытками в секундах

# Настройки ключей
REDIS_KEY_PREFIX = "chimera"              # Префикс для всех ключей
REDIS_DAILY_LIMIT_TTL = 86400            # TTL для счетчиков лимитов (24 часа)



# ========================================
# DEEPSEEK & TELEGRAM
# ========================================

# DeepSeek API настройки
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
DEEPSEEK_MODEL = "deepseek-chat"
DEEPSEEK_TIMEOUT = 30  # Сек
DEEPSEEK_MAX_RETRIES = 3

# Telegram Bot настройки
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_POLLING_TIMEOUT = 30
TELEGRAM_TYPING_UPDATE_INTERVAL = 5
TELEGRAM_MAX_MESSAGE_LENGTH = 4096
TELEGRAM_TYPING_CLEANUP_THRESHOLD = 100  # Порог для очистки завершенных typing задач
TELEGRAM_API_DEFAULT_TIMEOUT = 10        # Таймаут по умолчанию для API вызовов
TELEGRAM_MAX_TYPING_TASKS = 1000         # Макс. количество одновременных typing задач

# Метрики и адаптивная стратегия
CACHE_HIT_LOG_INTERVAL = 10
MIN_CACHE_HIT_RATE = 0.5



# ========================================
# JSON-ОТВЕТЫ
# ========================================

# Параметры валидации JSON-ответов
JSON_VALIDATION_ENABLED = True  # Включить валидацию структурированных ответов
JSON_VALIDATION_LOG_FAILURES = True  # Логировать неудачные валидации
JSON_VALIDATION_EVENT_BATCH_SIZE = 10  # Размер батча для событий валидации



# ========================================
# РЕЖИМЫ
# ========================================

# Настройки истории режимов
MODE_HISTORY_SIZE = 5  # Макс. размер истории режимов
MODE_CONFIDENCE_THRESHOLD = 0.3  # Мин. уверенность для режима по умолчанию
MODE_SCORE_NORMALIZATION_FACTOR = 1.5  # Делитель для нормализации уверенности

# Веса для контекстных паттернов
CONTEXTUAL_PATTERN_PHRASE_WEIGHT = 2.5  # Вес для точных фраз
CONTEXTUAL_PATTERN_DOMAIN_WEIGHT = 0.5  # Вес для доменных маркеров
CONTEXTUAL_PATTERN_CONTEXT_MULTIPLIER = 1.5  # Множитель для контекстных слов
CONTEXTUAL_PATTERN_SUPPRESSOR_MULTIPLIER = 0.0  # Множитель для подавителей

# Производительность определения режимов
MODE_DETECTION_CACHE_ENABLED = True  # Кэшировать результаты паттернов
MODE_DETECTION_MAX_TIME_MS = 5  # Макс. время определения в миллисекундах
MODE_DETECTION_DEBUG_LOGGING = True  # Логировать детали определения



# ========================================
# PYDANTIC
# ========================================

# Параметры валидации Pydantic моделей
PYDANTIC_RESPONSE_MIN_LENGTH = 1  # Минимальная длина поля response
PYDANTIC_CONFIDENCE_MIN = 0.0  # Мин. значение confidence/engagement_level
PYDANTIC_CONFIDENCE_MAX = 1.0  # Макс. значение confidence/engagement_level
PYDANTIC_STRING_LIST_COERCE = True  # Преобразовывать элементы списков в строки
PYDANTIC_VALIDATION_STRICT = False  # Строгий режим валидации (без приведения типов)

# Параметры валидации основных структур данных
PYDANTIC_MESSAGE_TYPE_MIN_LENGTH = 0  # Мин. длина message_type (0 = может быть пустым)
PYDANTIC_EVENT_TYPE_MIN_LENGTH = 1    # Мин. длина event_type (минимум 1 символ)
PYDANTIC_STREAM_ID_MIN_LENGTH = 0     # Мин. длина stream_id (0 = может быть пустым)
PYDANTIC_MODE_HISTORY_MAX_SIZE = 10   # Макс. размер истории режимов в UserSession
PYDANTIC_CACHE_METRICS_MAX_SIZE = 100 # Макс. размер метрик кэша в UserSession



# ========================================
# SHORT-TERM MEMORY (STM)
# ========================================

# Short-Term Memory (STM)

# STM Buffer settings
STM_BUFFER_SIZE = 50                    # Number of messages to keep per user
STM_CLEANUP_BATCH_SIZE = 10             # Number of records to delete at once
STM_QUERY_TIMEOUT = 5.0                 # Query timeout in seconds
STM_CONTEXT_FORMAT = "structured"       # Format: structured (for DeepSeek), text (for debug)
STM_INCLUDE_METADATA = True             # Include metadata in context
STM_MESSAGE_MAX_LENGTH = 4000           # Maximum length of a single message before truncation
STM_CONTEXT_SIZE_FOR_GENERATION = 20   # Number of historical messages to include in generation context

# Role mapping for DeepSeek API
STM_DEEPSEEK_ROLE_MAPPING = {
    "user": "user",
    "bot": "assistant"
}

# STM Metrics
STM_METRICS_ENABLED = True              # Enable metrics collection
STM_METRICS_LOG_INTERVAL = 300          # Metrics logging interval in seconds

# Context request handling
STM_CONTEXT_REQUEST_TIMEOUT = 30        # Timeout for pending context requests in seconds



# ========================================
# LONG-TERM MEMORY (LTM)
# ========================================

# LTM Buffer settings - TODO: implement in Phase 6.3
# LTM_RETENTION_DAYS = 365  # Placeholder - needs complex archival strategy
# WARNING: Simple deletion will break future personality evolution analysis

# LTM Memory types
LTM_MEMORY_TYPES = ['self_related', 'world_model', 'user_related']

# LTM Score constraints
LTM_SCORE_MIN = 0.0
LTM_SCORE_MAX = 1.0

# LTM Field lengths
LTM_USER_ID_MAX_LENGTH = 255
LTM_MEMORY_TYPE_MAX_LENGTH = 50
LTM_TRIGGER_REASON_MAX_LENGTH = 100

# LTM Array field limits
LTM_DOMINANT_EMOTIONS_MAX_SIZE = 10
LTM_SEMANTIC_TAGS_MAX_SIZE = 20

# LTM Conversation fragment settings
LTM_CONVERSATION_FRAGMENT_MAX_MESSAGES = 10
LTM_CONVERSATION_FRAGMENT_DEFAULT_WINDOW = 5

# LTM Message content truncation
LTM_MESSAGE_CONTENT_MAX_LENGTH = 2000

# LTM Trigger reasons
LTM_TRIGGER_REASONS = [
    'emotional_peak',
    'emotional_shift', 
    'self_reference',
    'deep_insight',
    'personal_revelation',
    'relationship_change',
    'creative_breakthrough'
]

# LTM Emotional thresholds
LTM_EMOTIONAL_PEAK_THRESHOLD = 0.77
LTM_EMOTIONAL_SHIFT_THRESHOLD = 0.55
LTM_EMOTIONAL_THRESHOLD = 0.62           # Порог для сохранения в LTM (0.6 = ~1-5% сообщений)

# LTM Default values
LTM_DEFAULT_ACCESS_COUNT = 0
LTM_DEFAULT_SELF_RELEVANCE_SCORE = None  # Optional field

# LTM Actor settings
LTM_QUERY_TIMEOUT = 5.0                 # Query timeout in seconds
LTM_METRICS_ENABLED = True              # Enable metrics collection
LTM_METRICS_LOG_INTERVAL = 300          # Metrics logging interval in seconds
LTM_SCHEMA_CHECK_TIMEOUT = 5.0          # Schema verification timeout

# LTM Search settings
LTM_SEARCH_MAX_LIMIT = 100              # Maximum results per search
LTM_SEARCH_DEFAULT_LIMIT = 10           # Default search results limit
LTM_SEARCH_TAGS_MODE_ANY = 'any'        # At least one tag matches
LTM_SEARCH_TAGS_MODE_ALL = 'all'        # All tags must match
LTM_SEARCH_RECENT_DAYS_DEFAULT = 7      # Default days for recent memories
LTM_SEARCH_MIN_IMPORTANCE_DEFAULT = 0.8 # Default min importance score


# ========================================
# LTM NOVELTY ASSESSMENT
# ========================================

# Novelty assessment weights (must sum to 1.0)
LTM_NOVELTY_SEMANTIC_WEIGHT = 0.4      # Weight for semantic distance factor
LTM_NOVELTY_EMOTIONAL_WEIGHT = 0.15    # Weight for emotional rarity factor
LTM_NOVELTY_CONTEXT_WEIGHT = 0.25       # Weight for context rarity factor
LTM_NOVELTY_TEMPORAL_WEIGHT = 0.2     # Weight for temporal novelty factor

# Cold start parameters
LTM_COLD_START_BUFFER_SIZE = 10        # Messages to accumulate before saving
LTM_COLD_START_MIN_THRESHOLD = 0.75     # Minimum novelty threshold
LTM_NOVELTY_SCORES_WINDOW = 90        # Size of recent scores window

# KNN density parameters
LTM_KNN_NEIGHBORS = 7                   # Number of nearest neighbors
LTM_KNN_DENSITY_THRESHOLD = 0.18         # Distance threshold for density
LTM_KNN_DENSITY_PENALTY = 0.25           # Weight reduction for dense regions

# Emotion frequency threshold
LTM_EMOTION_FREQUENCY_THRESHOLD = 0.18   # Min emotion value to count
LTM_PERCENTILE_MIN_SAMPLES = 15        # Min samples for percentile calc

# Maturity sigmoid rate
LTM_MATURITY_SIGMOID_RATE = 0.09        # Rate for sigmoid maturity factor




# ========================================
# LTM EMBEDDINGS
# ========================================

# Модель для генерации embeddings
LTM_EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
LTM_EMBEDDING_DEVICE = "cpu"  # или "cuda" при наличии GPU
LTM_EMBEDDING_CACHE_DIR = "./models/cache"

# Размерности композитного embedding (768d total)
LTM_EMBEDDING_SEMANTIC_DIM = 384
LTM_EMBEDDING_EMOTIONAL_DIM = 128  
LTM_EMBEDDING_TEMPORAL_DIM = 64
LTM_EMBEDDING_PERSONAL_DIM = 192

# Параметры векторизации
LTM_EMBEDDING_BATCH_SIZE = 32
LTM_EMBEDDING_MAX_LENGTH = 512
LTM_EMBEDDING_NORMALIZE = True

# Thread pool settings for async embedding generation
LTM_EMBEDDING_THREAD_POOL_SIZE = 2
LTM_EMBEDDING_GENERATION_TIMEOUT = 10.0  # Timeout in seconds (not used yet, reserved for future)

LTM_EMBEDDING_REQUEST_TIMEOUT = 2.0  # Timeout для запроса embedding в секундах
LTM_VECTOR_CACHE_TTL = 3600  # TTL для кэша векторного поиска (1 час)


# ========================================
# LTM ANALYTICS SETTINGS
# ========================================

# Emotional similarity search
LTM_ANALYTICS_SIMILARITY_THRESHOLD = 0.7        # Default cosine similarity threshold
LTM_ANALYTICS_EMOTIONAL_SIMILARITY_LIMIT = 10   # Default limit for similarity search

# Pattern detection
LTM_ANALYTICS_PATTERN_MIN_OCCURRENCES = 3       # Min occurrences to consider a pattern

# Emotional trajectory
LTM_ANALYTICS_TRAJECTORY_DEFAULT_DAYS = 30      # Default time window for trajectories
LTM_ANALYTICS_TRAJECTORY_DEFAULT_GRANULARITY = 'day'  # Default time granularity

# Concept associations
LTM_ANALYTICS_CONCEPT_ASSOCIATIONS_LIMIT = 20   # Max memories to analyze per concept

# Trend detection thresholds
LTM_ANALYTICS_TREND_INCREASE_THRESHOLD = 0.05   # Min avg change for increasing trend
LTM_ANALYTICS_TREND_DECREASE_THRESHOLD = -0.05  # Max avg change for decreasing trend

# Mood search
LTM_ANALYTICS_MOOD_MATCH_THRESHOLD = 0.3        # Min weighted score for mood match

# Importance distribution
LTM_ANALYTICS_HISTOGRAM_BUCKETS = 10            # Number of buckets for importance histogram
LTM_ANALYTICS_ANOMALY_STD_DEVS = 2              # Standard deviations for anomaly detection



# ========================================
# LTM Cache settings
# ========================================

LTM_CACHE_ENABLED = True                # Enable Redis caching for LTM
LTM_CACHE_KEY_PREFIX = "ltm"           # Prefix for all LTM cache keys
LTM_CACHE_DEFAULT_TTL = 1800           # Default TTL in seconds (30 minutes)

# Novelty cache specific settings
LTM_NOVELTY_CACHE_TTL = 1800           # 30 minutes for final results
LTM_NOVELTY_CACHE_LOG_INTERVAL = 100   # Log stats every N requests

# Intermediate computations cache TTL
LTM_EMBEDDING_CACHE_TTL = 3600         # 1 hour - embeddings don't change
LTM_KNN_CACHE_TTL = 900                # 15 minutes - changes with new memories  
LTM_TEMPORAL_CACHE_TTL = 1200          # 20 minutes - changes with new tags

# Profile and state cache TTL
LTM_PROFILE_CACHE_TTL = 21600          # 6 hours - full profile
LTM_PERCENTILE_CACHE_TTL = 3600        # 1 hour - changes with new scores
LTM_CALIBRATION_CACHE_TTL = 7200       # 2 hours - rarely changes after calibration

# Cache metrics and monitoring
LTM_CACHE_METRICS_ENABLED = True        # Enable cache metrics collection
LTM_CACHE_HIT_RATE_ALERT = 0.5         # Alert threshold for low hit rate


# ========================================
# LTM Request settings
# ========================================

LTM_REQUEST_TIMEOUT = 0.5              # Timeout in seconds for LTM response (500ms)
LTM_CONTEXT_LIMIT = 3                  # Maximum number of LTM memories to include in context
LTM_REQUEST_ENABLED = True             # Global switch for LTM integration
LTM_DEFAULT_SEARCH_TYPE = "recent"     # Default search type when no specific trigger

LTM_EMOTIONAL_SEARCH_THRESHOLD = 0.7


# ========================================
# LTM CLEANUP AND RETENTION
# ========================================

# Retention policy
LTM_CLEANUP_ENABLED = True                      # Enable automatic cleanup
LTM_RETENTION_DAYS = 365                        # Keep memories for 1 year
LTM_RETENTION_MIN_IMPORTANCE = 0.8              # Min importance to keep after retention period
LTM_RETENTION_CRITICAL_IMPORTANCE = 0.95        # Critical memories - never delete
LTM_RETENTION_MIN_ACCESS_COUNT = 5              # Keep if accessed >= N times regardless of age

# Cleanup execution
LTM_CLEANUP_BATCH_SIZE = 1000                   # Delete in batches to avoid long locks
LTM_CLEANUP_QUERY_TIMEOUT = 30.0                # Timeout for cleanup queries (seconds)
LTM_CLEANUP_SCHEDULE_HOUR = 3                   # Hour to run cleanup (UTC)
LTM_CLEANUP_SCHEDULE_MINUTE = 0                 # Minute to run cleanup
LTM_CLEANUP_DRY_RUN = False                     # If True, only log what would be deleted

# Summary generation
LTM_SUMMARY_ENABLED = True                      # Generate summaries before deletion
LTM_SUMMARY_PERIOD = 'month'                    # Aggregation period: 'week', 'month', 'quarter'
LTM_SUMMARY_MIN_MEMORIES = 5                    # Min memories to create summary
LTM_SUMMARY_TOP_EMOTIONS = 5                    # Number of top emotions to store
LTM_SUMMARY_TOP_TAGS = 10                       # Number of top tags to store

# Cache invalidation after cleanup
LTM_CLEANUP_INVALIDATE_CACHE = True             # Clear novelty caches after cleanup
LTM_CLEANUP_INVALIDATE_PATTERNS = [             # Cache patterns to invalidate
    "novelty:knn:*",
    "novelty:temporal:*", 
    "novelty:final:*"
]

# Logging and monitoring
LTM_CLEANUP_LOG_LEVEL = 'INFO'                  # Logging level for cleanup operations
LTM_CLEANUP_EMIT_EVENTS = True                  # Generate events for Event Store

# ========================================
# EMOTION ANALYSIS (DeBERTa)
# ========================================

# Модель и устройство
EMOTION_MODEL_NAME = "fyaronskiy/deberta-v1-base-russian-go-emotions"
EMOTION_MODEL_DEVICE = "cpu"  # или "cuda" при наличии GPU
EMOTION_MODEL_CACHE_DIR = "./emo/cache"  # Директория для кэша моделей

# Параметры анализа
EMOTION_CONFIDENCE_THRESHOLD = 0.5  # Общий порог (используется для метрик)
EMOTION_MODEL_MAX_LENGTH = 128      # Максимальная длина текста в токенах

# Логирование
EMOTION_LOG_PREDICTIONS = True      # Логировать ли предсказания
EMOTION_LOG_THRESHOLD = 0.3         # Минимальная вероятность для логирования

# Маппинг эмоций на эмодзи для логов
EMOTION_EMOJI_MAP = {
    'joy': '😊',
    'sadness': '😢',
    'anger': '😠',
    'fear': '😨',
    'surprise': '😮',
    'disgust': '🤮',
    'love': '😍',
    'admiration': '🤩',
    'amusement': '😄',
    'approval': '👍',
    'caring': '🤗',
    'confusion': '😕',
    'curiosity': '🤔',
    'desire': '🫦',
    'disappointment': '😞',
    'disapproval': '👎',
    'embarrassment': '😳',
    'excitement': '🎉',
    'gratitude': '🙏',
    'grief': '😔',
    'nervousness': '😰',
    'optimism': '✨',
    'pride': '😤',
    'realization': '💡',
    'relief': '😌',
    'remorse': '😔',
    'annoyance': '😒',
    'neutral': '😐'
}

# Пороговые значения для каждой эмоции (из документации модели)
EMOTION_THRESHOLDS = [
    0.551,  # admiration
    0.184,  # amusement
    0.102,  # anger
    0.102,  # annoyance
    0.184,  # approval
    0.224,  # caring
    0.204,  # confusion
    0.408,  # curiosity
    0.204,  # desire
    0.224,  # disappointment
    0.245,  # disapproval
    0.306,  # disgust
    0.163,  # embarrassment
    0.286,  # excitement
    0.388,  # fear
    0.327,  # gratitude
    0.020,  # grief
    0.163,  # joy
    0.449,  # love
    0.102,  # nervousness
    0.224,  # optimism
    0.041,  # pride
    0.122,  # realization
    0.061,  # relief
    0.143,  # remorse
    0.429,  # sadness
    0.306,  # surprise
    0.400   # neutral - УВЕЛИЧИТЬ до 0.4 для снижения доминирования
]

# Названия эмоций в порядке индексов модели
EMOTION_LABELS = [
    'admiration', 'amusement', 'anger', 'annoyance', 
    'approval', 'caring', 'confusion', 'curiosity',
    'desire', 'disappointment', 'disapproval', 'disgust',
    'embarrassment', 'excitement', 'fear', 'gratitude',
    'grief', 'joy', 'love', 'nervousness',
    'optimism', 'pride', 'realization', 'relief',
    'remorse', 'sadness', 'surprise', 'neutral'
]

# Маппинг на русские названия
EMOTION_LABELS_RU = {
    'admiration': 'восхищение',
    'amusement': 'веселье',
    'anger': 'гнев',
    'annoyance': 'раздражение',
    'approval': 'одобрение',
    'caring': 'забота',
    'confusion': 'замешательство',
    'curiosity': 'любопытство',
    'desire': 'желание',
    'disappointment': 'разочарование',
    'disapproval': 'неодобрение',
    'disgust': 'отвращение',
    'embarrassment': 'смущение',
    'excitement': 'волнение',
    'fear': 'страх',
    'gratitude': 'благодарность',
    'grief': 'горе',
    'joy': 'радость',
    'love': 'любовь',
    'nervousness': 'нервозность',
    'optimism': 'оптимизм',
    'pride': 'гордость',
    'realization': 'осознание',
    'relief': 'облегчение',
    'remorse': 'раскаяние',
    'sadness': 'грусть',
    'surprise': 'удивление',
    'neutral': 'нейтрально'
}



# ========================================
# EMOTION INTEGRATION
# ========================================

# Интеграция эмоций с потоком сообщений
EMOTION_ANALYSIS_ENABLED = True          # Включить анализ эмоций для сообщений
EMOTION_PEAK_THRESHOLD = 0.8             # Порог для EmotionalPeakEvent
EMOTION_TEXT_PREVIEW_LENGTH = 50         # Длина превью текста в событии



# ========================================
# PERCEPTION ACTOR
# ========================================

# Параметры анализа эмоций в PerceptionActor
PERCEPTION_EMOTION_TIMEOUT = 5.0  # Таймаут для анализа одного текста (секунды)
PERCEPTION_THREAD_POOL_SIZE = 3   # Размер пула потоков для асинхронного анализа
PERCEPTION_LOG_ERRORS = True      # Логировать ли ошибки анализа эмоций



# ========================================
# AUTH ACTOR SETTINGS
# ========================================

# Проверка схемы БД
AUTH_SCHEMA_CHECK_TIMEOUT = 5.0     # Таймаут проверки схемы в секундах

# Фоновые задачи
AUTH_CLEANUP_INTERVAL = 3600        # Интервал очистки старых данных (1 час)
AUTH_METRICS_LOG_INTERVAL = 300     # Интервал логирования метрик (5 минут)



# ========================================
# AUTHORIZATION SETTINGS
# ========================================

# Допустимые сроки действия паролей в днях
PASSWORD_DURATIONS = [30, 90, 180, 365]

# Anti-bruteforce защита
AUTH_MAX_ATTEMPTS = 5              # Количество попыток до блокировки
AUTH_BLOCK_DURATION = 900          # Длительность блокировки в секундах (15 минут)

AUTH_ATTEMPTS_WINDOW = 900         # Окно подсчета попыток в секундах (15 минут)

# Администраторы системы
ADMIN_USER_IDS = [502312936]       # Список telegram_id администраторов

# Таймауты и лимиты
AUTH_CHECK_TIMEOUT = 2.0           # Таймаут проверки авторизации в секундах
AUTH_FALLBACK_TO_DEMO = True       # Разрешить работу как демо при недоступности AuthActor

# Настройки команд авторизации
AUTH_PASSWORD_WAIT_TIMEOUT = 60  # Таймаут ожидания пароля в секундах

# Периодическая очистка лимитов
AUTH_DAILY_RESET_ENABLED = True      # Включить ежедневный сброс счетчиков
AUTH_DAILY_RESET_HOUR = 0            # Час сброса (0-23, по умолчанию полночь)

# Circuit Breaker для защиты от брутфорса
AUTH_CIRCUIT_BREAKER_ENABLED = True      # Включить Circuit Breaker для AUTH_REQUEST
AUTH_CIRCUIT_BREAKER_THRESHOLD = 3       # Количество ошибок для открытия
AUTH_CIRCUIT_BREAKER_TIMEOUT = 300       # Время восстановления в секундах (5 минут)
