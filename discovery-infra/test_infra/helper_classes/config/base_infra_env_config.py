from abc import ABC

from dataclasses import dataclass

from .base_entity_config import BaseEntityConfig


@dataclass
class BaseInfraEnvConfig(BaseEntityConfig, ABC):
    """
    Define all configurations variables that are needed for Cluster during it's execution
    All arguments must have default to None with type hint
    """
    infra_env_id: str = None
    infra_env_name: str = None

    def is_cluster(self) -> bool:
        return False

    def is_infra_env(self) -> bool:
        return True