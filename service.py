from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_persons(db: Session, roll_number: str):

    persons_all = db.query(models.Persons).all()


    rollnumber: str = "customer values"



    user_list = []  # Creating new list


    # auto generated route, add a record
# Add element to the list 'user_list'
    user_list.insert(0, 'roll_number')
    res = {
        'custom_value': rollnumber,
        'users': user_list,
    }
    return res

async def get_persons_rollnumber(db: Session, rollnumber: int):

    persons_one = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()
    res = {
        'person_rollnumner': persons_one.rollnumber,
    }
    return res

async def post_persons(db: Session):

    # number added
    roll_number: int = "923489"


    # asd
    asd = {}  # Creating new dict

    res = {
        'number': roll_number,
    }
    return res

async def put_persons_rollnumber(db: Session, rollnumber: str, fullname: str, age: str, profession: str):

    persons_edited_record = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()
    for key, value in {'rollnumber': rollnumber, 'fullname': fullname, 'age': age, 'profession': profession}.items():
          setattr(persons_edited_record, key, value)
    db.commit()
    db.refresh(persons_edited_record)
    persons_edited_record = persons_edited_record

    res = {
        'persons_edited_record': persons_edited_record,
    }
    return res

async def delete_persons_rollnumber(db: Session, rollnumber: int):

    persons_deleted = None
    record_to_delete = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()

    if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          persons_deleted = record_to_delete
    res = {
        'persons_deleted': persons_deleted,
    }
    return res

async def get_addresses(db: Session):

    addresses_all = db.query(models.Addresses).all()
    res = {
        'addresses_all': addresses_all,
    }
    return res

async def get_addresses_id(db: Session, id: int):

    addresses_one = db.query(models.Addresses).filter(models.Addresses.id == id).first()
    res = {
        'addresses_one': addresses_one,
    }
    return res

async def post_addresses(db: Session, id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str):

    record_to_be_added = {'id': id, 'street': street, 'city': city, 'state': state, 'country': country, 'postal_code': postal_code, 'created_at': created_at, 'updated_at': updated_at}
    new_addresses = models.Addresses(**record_to_be_added)
    db.add(new_addresses)
    db.commit()
    db.refresh(new_addresses)
    addresses_inserted_record = new_addresses
    res = {
        'addresses_inserted_record': addresses_inserted_record,
    }
    return res

async def put_addresses_id(db: Session, id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str):

    addresses_edited_record = db.query(models.Addresses).filter(models.Addresses.id == id).first()
    for key, value in {'id': id, 'street': street, 'city': city, 'state': state, 'country': country, 'postal_code': postal_code, 'created_at': created_at, 'updated_at': updated_at}.items():
          setattr(addresses_edited_record, key, value)
    db.commit()
    db.refresh(addresses_edited_record)
    addresses_edited_record = addresses_edited_record

    res = {
        'addresses_edited_record': addresses_edited_record,
    }
    return res

async def delete_addresses_id(db: Session, id: int):

    addresses_deleted = None
    record_to_delete = db.query(models.Addresses).filter(models.Addresses.id == id).first()

    if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          addresses_deleted = record_to_delete
    res = {
        'addresses_deleted': addresses_deleted,
    }
    return res

