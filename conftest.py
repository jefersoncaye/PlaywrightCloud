import pytest
from slugify import slugify


@pytest.fixture
def set_up(page):

    yield page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            page = item.funcargs["page"]
            screen_file = str(f'imagens/{slugify(item.nodeid)}.png')
            page.screenshot(path=screen_file, full_page=True)
            extra.append(pytest_html.extras.png(screen_file))
        report.extra = extra


video_counter = 0
@pytest.fixture(autouse=True)
def save_video_as(request, page):
    global video_counter
    video_counter = video_counter + 1

    yield

    video_opt = request.config.getoption("video")
    test_result_failed = request.node.rep_call.failed

    if video_opt == "on" or (video_opt == "retain-on-failure" and test_result_failed):
        page.context.close()
        custom_path = f"imagens/{video_counter:02d}.webm"
        page.video.save_as(custom_path)
        page.video.delete()