import pytest
import os
from datetime import datetime
from playwright.sync_api import sync_playwright
from config.config import Config

os.makedirs(Config.VIDEO_DIR, exist_ok=True)
os.makedirs(Config.TRACE_DIR, exist_ok=True)
os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(
        headless=Config.headless
    )
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser, request):
    test_name = request.node.name

    context = browser.new_context(
        record_video_dir=Config.VIDEO_DIR,
        record_video_size={"width": 1280, "height": 720}
    )

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()
    yield page

    
    if request.node.rep_call.failed:
        screenshot_path = os.path.join(
            Config.SCREENSHOT_DIR, f"{test_name}.png"
        )
        page.screenshot(path=screenshot_path)

    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    trace_file = os.path.join(
        Config.TRACE_DIR, f"{test_name}_{timestamp}.zip"
    )

    context.tracing.stop(path=trace_file)
    context.close()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)