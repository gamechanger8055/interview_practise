from unittest.mock import Mock
import pytest
import requests

from src.lib.clients import ProdLogClient

from src.tests.fixtures import add_user_log, update_app_log

class TestProdLogClient:
  @pytest.fixture(autouse=True)
  def initialize(self, add_user_log, update_app_log):
    self.log_response = Mock(requests.Response)
    self.log_response.json.return_value = [add_user_log, update_app_log]

  def test_get_log_data(self, mocker):
    mocker.patch.object(requests, "get").return_value = self.log_response
    client = ProdLogClient("TEST_CREDENTIALS")
    assert len(client.get_log_data()) == 2