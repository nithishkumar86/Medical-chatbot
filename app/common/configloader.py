import yaml
from app.common.Logs import get_logger
from app.common.Logs import get_logger

logger = get_logger(__name__)

def load_config(file_path: str = "D:\\MEDICAL_CHATBOT\\app\\common\\configfile.yaml") -> dict:
    """Load YAML configuration from a file."""
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
        logger.info(f"config is loaded successfully in {file_path}")
    return config


