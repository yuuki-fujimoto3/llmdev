import pytest
from authenticator import Authenticator

@pytest.fixture
def authenticator():
    auth = Authenticator()
    yield auth
    auth.users = {}

# ユーザー登録｜正常
def test_register(authenticator):
    authenticator.register("name", "pass")
    assert "name" in authenticator.users

# ユーザー登録｜異常（重複登録）
def test_register_duplicate(authenticator):
    authenticator.register("name", "pass")
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        authenticator.register("name", "pass2")

# ログイン｜正常
def test_login(authenticator):
    authenticator.register("name", "pass")
    result = authenticator.login("name", "pass")
    assert result == "ログイン成功"

# ログイン｜異常（パスワード不一致）
def test_login_mismatch(authenticator):
    authenticator.register("name", "pass")
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        authenticator.login("name", "pass2")