__title__ = "py-es3"
__author__ = "AbstractUmbra"
__license__ = "AGPL-v3"
__copyright__ = "Copyright 2025-present AbstractUmbra"
__version__ = "0.0.1"

import logging

from .crypt import decrypt, encrypt, strip_es3_type_kv

__all__ = ("decrypt", "encrypt", "strip_es3_type_kv")

logging.getLogger(__name__).addHandler(logging.NullHandler())  # required
