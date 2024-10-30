from sqlalchemy import create_engine, Column, Integer, String, UUID, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
import uuid

Base = declarative_base()

class UserInfo(Base):
    __tablename__ = 'user_info'

    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    address = Column(String(255))
    org_name = Column(String(100))
    tenant_id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_logo = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    api_key = Column(String(100))
    status = Column(String(50))
    org_id = Column(String(50))

    def __repr__(self):
        return (f"<UserInfo(id='{self.id}', username='{self.username}', email='{self.email}', "
                f"password='{self.password}', first_name='{self.first_name}', last_name='{self.last_name}', "
                f"address='{self.address}', org_name='{self.org_name}', tenant_id='{self.tenant_id}', "
                f"org_logo='{self.org_logo}', created_at='{self.created_at}', updated_at='{self.updated_at}')>")

