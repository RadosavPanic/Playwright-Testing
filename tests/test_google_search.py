import re
from playwright.sync_api import expect

def test_google_search(page):
    page.wait_for_timeout(2000)
    page.goto("https://www.google.com/ncr")
    
    try:
        page.get_by_role("button", name="Accept all").click(timeout=2000)
    except:
        print("No popup")
        
    page.get_by_role("combobox", name="Search").fill("full stack roadmap")
    page.keyboard.press("Enter", delay=2000)
        
    expect(page).to_have_title(re.compile("full stack roadmap", re.IGNORECASE))