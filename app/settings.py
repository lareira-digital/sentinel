from pydantic import BaseSettings


class SentinelSettings(BaseSettings):
    immudb_user: str = "immudb"
    immudb_pass: str = ""
    immudb_host: str = ""
    immudb_port: int = ""

    class Config:
        env_file = "../.env"
