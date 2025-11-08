import pytest
from playwright.sync_api import sync_playwright

def test_open_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://radosav-panic.vercel.app")
        
        page.wait_for_load_state("load")
        
        title = page.title()
        
        print(title)
        
        flag: bool
        
        flag = title == "Radosav's Portfolio"
        
        assert flag, f"Expected title to be 'Radosav's Portfolio' but got '{title}'"
                
        print("Test completed successfully.")
        
        browser.close()