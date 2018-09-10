import pytest
from context import HGECtx

def pytest_addoption(parser):
    parser.addoption(
        "--hge-url", metavar="HGE_URL", help="url for graphql-engine", required=True
    )
    parser.addoption(
        "--pg-url", metavar="PG_URL", help="url for connecting to Postgres directly", required=True
    )

@pytest.fixture()
def hge_ctx(request):
    hge_url = request.config.getoption('--hge-url')
    pg_url = request.config.getoption('--pg-url')
    hge_ctx = HGECtx(hge_url=hge_url, pg_url=pg_url)
    yield hge_ctx  # provide the fixture value
    print("teardown hge_ctx")
    hge_ctx.teardown()
