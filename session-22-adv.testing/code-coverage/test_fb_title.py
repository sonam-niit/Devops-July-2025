from fb_login import get_facebook_title

def test_facebook_title():
    assert "Facebook" in get_facebook_title()