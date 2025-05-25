from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, field_validator, validator
import database as db
import helpers

class ModelCustomer(BaseModel):
    id: constr(min_length=3, max_length=3)  # 1 uppercase letter followed by 2 digits
    name: constr(min_length=2, max_length=30)  # 2 to 30 characters
    last_name: constr(min_length=2, max_length=30)  # 2 to 30 characters


class ModelCustomerUpdate(ModelCustomer):
    @field_validator('id')
    def validator_id(cls, id):
        if helpers.validate_id(id, db.Customers.list):
            return id
        raise ValueError("ID already exists")
       
    


headers={"content-type": "charset=utf-8"}

app = FastAPI(

    title="Customer Management API",
    description="API for managing customers",
    version="1.0.0",





)


@app.get("/customers/", tags=["Customers"])
async def customers():
    content = [ customer.to_dict() for customer in db.Customers.list]

    return JSONResponse(content=content, headers=headers)



@app.get("/customers/search/{id}", tags=["Customers"])
async def search_customer(id: str):
    customer = db.Customers.search(id=id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return JSONResponse(content= customer.to_dict(), headers=headers)


@app.post('/customers/add/', tags=["Customers"])
async def add_customer(data: ModelCustomerUpdate):
    customer = db.Customers.add(data.id, data.name, data.last_name)
    if customer:
        return JSONResponse(content=customer.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Customer already exists")



@app.put('/customers/remove/', tags=["Customers"])
async def remove_customer(data: ModelCustomer):
    if db.Customers.search(data.id):
        customer = db.Customers.remove(data.id, data.name, data.last_name)
        if customer:
            return JSONResponse(content=customer.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Customer not found")



@app.delete('/customers/delete/{id}', )
async def delete_customer(id: str):
    if db.Customers.search(id):
        customer = db.Customers.delete(id=id)
        return JSONResponse(content=customer.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Customer not found")





print("API is running...")

