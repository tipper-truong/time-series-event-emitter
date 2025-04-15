from sqlalchemy import Column, Integer, Enum, Float, DateTime, Index

from app.models.base import BaseModel
import enum

class MetricType(enum.Enum):
    TEMPERATURE = "temperature"
    CPU_USAGE = "cpu_usage"
    FINANCIAL_STOCK = "financial_stock_data"
    
class Event(BaseModel):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    metric = Column(Enum(MetricType, name="metric_type_enum"), nullable=False)
    value = Column(Float, nullable=False)

    __table_args__ = (
        # composite index for metric and timestamp for O(log n) queries
        Index('idx_metric_timestamp', 'metric', 'timestamp'),
    )

    def __repr__(self):
        return f"<Event(timestamp='{self.timestamp}', metric='{self.metric}', value={self.value})>"
    
    def to_dict(self):
        return {
            "timestamp": self.timestamp.isoformat(),
            "metric": self.metric,
            "value": self.value
        }