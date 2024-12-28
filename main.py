from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _service

if TYPE_CHECKING:
	from sqlalchemy.orm import Session

app = _fastapi.FastAPI()

@app.post("/api/contacts", response_model=_schemas.Contact)
async def create_contact(
    contact: _schemas.CreateContact,
    db: _orm.Session = _fastapi.Depends(_service.get_db)
):
	return await _service.create_contact(contact=contact, db=db)

@app.get("/api/contacts", response_model=List[_schemas.Contact])
async def get_all_contacts(db: _orm.Session = _fastapi.Depends(_service.get_db)):
    return await _service.get_all_contacts(db=db)


@app.get("/api/contacts/{contact_id}", response_model=_schemas.Contact)
async def get_contact_by_id(
	contact_id: int,
	db: _orm.Session = _fastapi.Depends(_service.get_db)
):
	return await _service.get_contact_by_id(contact_id=contact_id, db=db)


@app.delete("/api/contacts/{contact_id}")
async def delete_contact(
	contact_id: int,
	db: _orm.Session = _fastapi.Depends(_service.get_db)
):
	contact = await _service.get_contact_by_id(contact_id=contact_id, db=db)

	if not contact:
		raise _fastapi.HTTPException(status_code=404, detail="Contact not found")

	await _service.delete_contact(contact=contact, db=db)
	return {"message": "Contact deleted successfully"}


@app.put("/api/contacts/{contact_id}", response_model=_schemas.Contact)
async def update_contact(
	contact_id: int,
	contact_data: _schemas.CreateContact,
	db: _orm.Session = _fastapi.Depends(_service.get_db)
):
	contact = await _service.get_contact_by_id(contact_id=contact_id, db=db)

	if not contact:
		raise _fastapi.HTTPException(status_code=404, detail="Contact not found")

	return await _service.update_contact(contact_data=contact_data, contact=contact, db=db)
