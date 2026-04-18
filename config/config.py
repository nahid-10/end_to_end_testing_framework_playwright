import os

class Config:
    
    base_url="https://practice.expandtesting.com"
    
    browser="chromium"
    
    headless= False
    
    timeout=100000
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    REPORT_DIR = os.path.join(BASE_DIR, "reports")
    
    VIDEO_DIR = os.path.join(REPORT_DIR, "videos")
    
    TRACE_DIR = os.path.join(REPORT_DIR, "traces")
    
    SCREENSHOT_DIR = os.path.join(REPORT_DIR, "screenshots")
    