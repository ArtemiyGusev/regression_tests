import allure
from allure_commons.types import Severity
from voluptuous import Schema, ALLOW_EXTRA
from pytest_voluptuous import S
from base_page.helper.requests_helper import myglo
from base_page.helper.module_helper import rand_string, rand_int
from base_page.api_controls.am_bearer_authenticated import AmBearerAuthenticated


def test_check_device():
    allure.dynamic.tag("Web application Api")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты myglo.ru")
    allure.dynamic.story("Проверка Добавления девайся в корзину")

    body = {
        "cartItem":
            {
                "sku": "10119143",
                "qty": 1
            }
        }
    response = myglo().post("rest/ru_ru/V1/carts/mine/items", json=body, auth=AmBearerAuthenticated(email='dfgdr33drgdr@test.ru', password='Test20202020]'))

    schema = Schema({
        "sku": str,
        "qty": int,
        "name": str,
        "product_type": str
    },
        extra=ALLOW_EXTRA,
    )
    assert response.status_code == 200
    assert S(schema) == response.json()
    assert response.json()['sku'] == "10119143"


def test_get_info_customer():
    allure.dynamic.tag("Web application Api")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты myglo.ru")
    allure.dynamic.story("Проверка личных данных пользователя")

    response = myglo().get("rest/ru_ru/V1/customers/me", auth=AmBearerAuthenticated("hCXriQ9U4QYoN@test.ru", "Test202020"))

    schema = Schema({
        "firstname": str,
        "lastname": str,
        "gender": int,
        "store_id": int
    },
        extra=ALLOW_EXTRA
    )

    assert response.status_code == 200
    assert S(schema) == response.json()
    assert response.json()["id"] == 2136524


def test_register_user():
    allure.dynamic.tag("Web application Api")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты myglo.ru")
    allure.dynamic.story("Проверка регистрации устройства в профиле пользователя")

    body = {
        "customer": {
            "store_id": 2,
            "email": rand_string(13) + "@test.ru",
            "firstname": "JaneTester",
            "lastname": "DoeTester",
            "dob": "2000-01-01",
            "gender": 1,
            "custom_attributes": {
                "glo_phone_no": "+7495" + str(rand_int(1000000, 9999999))
            },
        },
        "password": "Test20202020]"
    }
    response_reg = myglo().post("rest/ru_ru/V1/customers", json=body)
    schema = Schema({
        "firstname": str,
        "lastname": str,
        "gender": int
    },
        extra=ALLOW_EXTRA,
    )
    assert S(schema) == response_reg.json()
    assert response_reg.status_code == 200

    headers = {'Content-type': 'application/json'}
    body = {
        "currentPassword": "Test20202020]",
        "newPassword": "Test202020"
    }
    response_change_password = myglo().put("rest/V1/customers/me/password", json=body, headers=headers,
                                           auth=AmBearerAuthenticated(response_reg.json()["email"], "Test20202020]"))
    assert response_change_password.json() == True
    assert response_change_password.status_code == 200


def test_delete_all_device_api():
    allure.dynamic.tag("Web application Api")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты myglo.ru")
    allure.dynamic.story("Проверка удаления девайса из корзины, после его добавления")

    body = {
        "cartItem":
            {
                "sku": "10119143",
                "qty": 1
            }
        }
    myglo().post("rest/ru_ru/V1/carts/mine/items", json=body, auth=AmBearerAuthenticated("dfgdr33drgdr@test.ru", "Test20202020]"))

    devices = myglo().get("rest/ru_ru/V1/carts/mine/items/", auth=AmBearerAuthenticated('dfgdr33drgdr@test.ru', 'Test20202020]'))
    for device in devices.json():
        response = myglo().delete("rest/ru_ru/V1/carts/mine/items/" + str(device['item_id']), auth=AmBearerAuthenticated('dfgdr33drgdr@test.ru', 'Test20202020]'))
        assert response.json() == True
        assert response.status_code == 200


def test_check_add_my_device():
    allure.dynamic.tag("Web application Api")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты myglo.ru")
    allure.dynamic.story("Проверка на добавление девайса в мои девайсы")

    body = {
        "another_store_name": "",
        "batch_number": "N0I29NAWC4",
        "place_of_purchase": "100000001",
        "purchase_date": "11/11/2019",
        "sku": "10120784",
        "store_name": "100000000"
      }

    response = myglo().post("rest/ru_ru/V1/device-management/register", json=body, auth=AmBearerAuthenticated("dfgdr33drgdr@test.ru", "Test20202020]"))
    assert response.status_code == 200
    assert response.json()[0]['product_id'] == '340'
