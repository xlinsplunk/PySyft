# third party
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

# relative
from . import Base


class SetupConfig(Base):
    __tablename__ = "setup"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    domain_name = Column(String(255), default="")
    description = Column(String(255), default="")
    contact = Column(String(255), default="")
    daa = Column(Boolean(), default=False)
    node_id = Column(String(32), default="")

    def __str__(self) -> str:
        return f"<Domain Name: {self.domain_name}>"


def create_setup(id: int, domain_name: str, node_id: str) -> SetupConfig:
    return SetupConfig(id=id, domain_name=domain_name, node_id=node_id)
