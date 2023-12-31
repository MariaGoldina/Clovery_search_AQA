# import os
#
#
# url_node_employees_search = os.environ.get('URL_NODE_SEARCH')
# url_employees_search = os.environ.get('URL_EMPLOYEES_SEARCH')
# url_skill_search = os.environ.get('URL_SKILL_SEARCH')
# server = os.environ.get('SERVER')

server = "prod"

# Тестовый сервер
if server == "test":
    url_node_employees_search = "https://api.cloveri.skroy.ru/api/node_employees_search/"
    url_employees_search = "https://api.cloveri.skroy.ru/api/employee_search/"
    url_skill_search = "https://api.cloveri.skroy.ru/api/search"

# На проде
elif server == "prod":
    url_node_employees_search = "https://nes.ms.corp.cloveri.com/api/node_employees_search/"
    url_employees_search = "https://es.ms.corp.cloveri.com/api/employee_search/"
    url_skill_search = "https://search.corp.cloveri.com/api/search"


company_id = "4b871f91-45aa-4a72-8cb5-417ef561307f"
profession_ids = ["9c08af9c-22d8-4bc6-a598-cb3ad035ceef"]
team_ids = ["23a4363f-28d0-43e2-b66e-f2aedd4175ae"]
skills =  [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1"},
           {"skill_id": "2c901b0c-f1cb-41e9-b566-a53f1b89714f"},
           {"skill_id": "a3c1ef15-6d4f-4290-abee-62247c5465ff"}]
skills_1 = [{"skill_id": "6796cfb9-a61c-48fd-ac9c-a395a001fad1", "assessment_from": 0.1,"assessment_to": 0.9},
            {"skill_id": "2c901b0c-f1cb-41e9-b566-a53f1b89714f", "assessment_from": 0.1, "assessment_to": 0.9},
            {"skill_id": "a3c1ef15-6d4f-4290-abee-62247c5465ff", "assessment_from": 0.1,"assessment_to": 0.9}]
wrong_params = ""
"""skills = [{'skill_id': skill_id,
           'assessment_from': 0,
           'assessment_to': 0.9}]"""

node_id = 2919
project_id = '3e3028cd-3849-461b-a32b-90c0d6411daa'
item_type = 'orgstructureM'
item = 'pytest'
page = 1
limit = 50
is_only_node_value = False