from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
from advanced_scraper import run_advanced_scraper_api

app = FastAPI(title="Startup India Advanced Scraper")

class ScrapeRequest(BaseModel):
    start_page: int = 1
    end_page: int = 5
    stages: Optional[List[str]] = []
    sectors: Optional[List[str]] = []
    states: Optional[List[str]] = []
    format: str = "csv"       # csv | excel | json
    scrape_profiles: bool = False

@app.post("/scrape")
def scrape(req: ScrapeRequest):
    file_path = run_advanced_scraper_api(
        start_page=req.start_page,
        end_page=req.end_page,
        stages=req.stages,
        sectors=req.sectors,
        states=req.states,
        export_format=req.format,
        headless=True,
        scrape_profiles=req.scrape_profiles
    )

    return FileResponse(
        path=file_path,
        filename=file_path.split("/")[-1],
        media_type="application/octet-stream"
    )
