from settings import BROWSER_OPTIONS


def test_location_ok(mobile_app_auth):
    location = mobile_app_auth.get_location()
    assert f"{BROWSER_OPTIONS['geolocation']['latitude']}:{BROWSER_OPTIONS['geolocation']['longitude']}" == location


def test_location_ok2(desktop_app_auth):
    location = desktop_app_auth.get_location()
    assert f"{BROWSER_OPTIONS['geolocation']['latitude']}:{BROWSER_OPTIONS['geolocation']['longitude']}" == location

