import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)

@pytest.mark.database
def test_send_package():
    db = Database()
    user = db.send_pachkage('Sergii')

    assert user [0][0] == 'Maydan Nezalezhnosti 1'
    assert user [0][1] == 'Kyiv'
    assert user [0][2] == '3127'
    assert user [0][3] == 'Ukraine'

@pytest.mark.database
def test_product_update():
    db = Database()
    db.update_sugar_info(1, 25)
    product_qnt = db.select_sugar_product(1)

    assert product_qnt[0][0] == 25
@pytest.mark.database
def test_product_insert():
    db=Database()
    db.insert_info(4,'biscuit','sweet',34)
    product_qnt = db.select_sugar_product(4)

    assert product_qnt [0][0] == 34

@pytest.mark.database
def test_product_delete():
    db=Database()
    db.insert_info(99,'test','data',999)
    db.delete_product(99)
    qnt = db.select_sugar_product(99)

    assert len(qnt) == 0
@pytest.mark.database
def test_check_join_info():
    db=Database()
    orders = db.get_info()
    print("Orders", orders)
    assert len(orders) == 1