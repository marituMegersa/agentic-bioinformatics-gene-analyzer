from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.bioinformatics_gene_analyzer.models import AgenticBioinformaticsGeneAnalyzerSession, AgenticBioinformaticsGeneAnalyzerItem
from app.domain.bioinformatics_gene_analyzer.schemas import AgenticBioinformaticsGeneAnalyzerSessionCreate, AgenticBioinformaticsGeneAnalyzerItemCreate

class AgenticBioinformaticsGeneAnalyzerService:
    @staticmethod
    def create_session(db: Session, data: AgenticBioinformaticsGeneAnalyzerSessionCreate) -> AgenticBioinformaticsGeneAnalyzerSession:
        db_obj = AgenticBioinformaticsGeneAnalyzerSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticBioinformaticsGeneAnalyzerSession:
        return db.query(AgenticBioinformaticsGeneAnalyzerSession).filter(AgenticBioinformaticsGeneAnalyzerSession.id == session_id).first()
