from pydantic import BaseSettings


class SentinelSettings(BaseSettings):
    immudb_user: str = "immudb_user"
    immudb_pass: str = "immudb_pass"
    immudb_port: int = 1000

    class Config:
        env_file = "../.env"
