import pytest
from github import Github


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_some_user('defunkt')
    assert user['login'] == "defunkt"



@pytest.mark.api
def test_non_exist_user(github_api):
    r = github_api.get_some_user('bobbenkoandrii')
    #print(r)
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    #print(r)
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_nonfind_repo(github_api):
    r = github_api.search_repo('bobbenko_qa_auto')
    assert r['total_count'] == 0

@pytest.mark.api
def test_find_repo_with_one_charac(github_api):
    r = github_api.search_repo("s")
    assert r['total_count'] != 0