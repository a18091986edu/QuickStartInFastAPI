from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    host: str
    port: int
    user: str
    password: str
    database: str
    connection_string: str

    def __post_init__(self):
        self.url: str = f"{self.connection_string}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class Config:
    db: DatabaseConfig


def load_config() -> Config:
    env = Env()
    env.read_env()
    db = DatabaseConfig(
        host=env.str("DB_HOST"),
        port=env.int("DB_PORT"),
        user=env.str("DB_USER"),
        password=env.str("DB_PASSWORD"),
        database=env.str("DB_NAME"),
        connection_string=env.str("DB_CONNECTION_STRING"),
    )
    return Config(db=db)


config = load_config()

if __name__ == "__main__":
    print(config.db.url)
