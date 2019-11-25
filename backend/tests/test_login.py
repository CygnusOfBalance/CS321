from moto import mock_dynamodb2
import boto3
import json
import sys
sys.path.append('../')
from sch_new_login import my_try # pylint: disable=import-error

print('whyyyy')

with open('example_event.json') as ex_event:


    @mock_dynamodb2
    def test_my_try():
        assert my_try(ex_event)
