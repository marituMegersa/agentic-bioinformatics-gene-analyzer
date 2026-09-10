from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.bioinformatics_gene_analyzer.schemas import AgenticBioinformaticsGeneAnalyzerSessionCreate, AgenticBioinformaticsGeneAnalyzerSessionResponse
from app.domain.bioinformatics_gene_analyzer.service import AgenticBioinformaticsGeneAnalyzerService

router = APIRouter(prefix="/api/v1/bioinformatics_gene_analyzer", tags=["Agentic Bioinformatics Gene Analyzer Domain"])

@router.post("/sessions", response_model=AgenticBioinformaticsGeneAnalyzerSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticBioinformaticsGeneAnalyzerSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Bioinformatics Gene Analyzer.
    """
    return AgenticBioinformaticsGeneAnalyzerService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticBioinformaticsGeneAnalyzerSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticBioinformaticsGeneAnalyzerService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
