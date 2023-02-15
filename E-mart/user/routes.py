from . models import *
from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import APIRouter, Request , Form, status
from fastapi.templating import Jinja2Templates
from slugify import slugify
from datetime import datetime


router = APIRouter()
templates= Jinja2Templates ( directory = "user/templates" )


@router.get("/", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse("product.html",{
        "request": request,
    })


@router.get("/first/", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse("fashion.html",{
        "request": request,
    })

@router.get("second/", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse("electronic.html",{
        "request": request,
    })

@router.get("third/", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse("jewellery.html",{
        "request": request,
    })

@router.post("/Category/")
async def create_category(category_image: UploadFile = File(...),
            name: str = Form(...),
            description:str =Form(...),
            ):
    if await Category.exists(name=name):
        return {"message": "category already exists"}
    else:

          slug = slugify(name)

          FILEPATH = "static/img/product/"
          filename = category_image.filename
          extension = filename.split(".")[1] 
          imagename = filename.split(".")[0] 

          if extension not in ["png", "jpg", "jpeg", "jfif"]:
              return{"status": "error","detial": "File extension not allowed"}

          dt = datetime.now()
          dt_timestamp = round(datetime.timestamp(dt))

          modified_image_name = imagename+"_"+str(dt_timestamp)+"."+extension
          genrated_name = FILEPATH + modified_image_name
          file_content = await category_image.read()
        
          with open (genrated_name, "wb") as file:
              file.write(file_content)

          file.close()

          category_obj = await Category.create(
                 category_image=genrated_name,
                 name=name,
                 slug=slug,
                 description=description)
                
          return {"category added"}


@router.post("/SubCategory/")
async def create_subcategory(subcategory_image: UploadFile = File(...),
            name: str = Form(...),category_id: str = Form(...), description:str=Form(...),
            ):
          category = await Category.get(id=category_id)
          slug = slugify(name)

          FILEPATH = "static/img/product/"
          filename = subcategory_image.filename
          extension = filename.split(".")[1] 
          imagename = filename.split(".")[0] 

          if extension not in ["png", "jpg", "jpeg", "jfif"]:
                return{"status": "error","detial": "File extension not allowed"}

          dt = datetime.now()
          dt_timestamp = round(datetime.timestamp(dt))

          modified_image_name = imagename+"_"+str(dt_timestamp)+"."+extension
          genrated_name = FILEPATH + modified_image_name
          file_content = await subcategory_image.read()
        
          with open (genrated_name, "wb") as file:
              file.write(file_content)
          file.close()

          subcategory_obj = await SubCategory.create(
                 subcategory_image=genrated_name,
                 name=name,
                 slug=slug,
                 category=category,
                 description=description)

          return {"message": "subcategory add"}


@router.post("/product/")
async def create_product(request:Request,image: UploadFile = File(...),
            sellingPrice:float = Form(...),
            description:str = Form(...),
            brand:str = Form(...),
            sub_category_id:str = Form(...),
            category_id:str =Form(...)):

          subcategory = await SubCategory.get(id=sub_category_id)
          FILEPATH = "static/img/product/"
          filename = image.filename
          extension = filename.split(".")[1] 
          imagename = filename.split(".")[0] 

          if extension not in ["png", "jpg", "jpeg", "jfif"]:
              return{"status": "error","detial": "File extension not allowed"}

          dt = datetime.now()
          dt_timestamp = round(datetime.timestamp(dt))

          modified_image_name = imagename+"_"+str(dt_timestamp)+"."+extension
          genrated_name = FILEPATH + modified_image_name
          file_content = await image.read()

          with open (genrated_name, "wb") as file:
              file.write(file_content)

              file.close()

              product_obj = await Product.create(
                product_image=genrated_name,
                selling_price=sellingPrice,
                description=description,
                brand=brand, 
                subcategory=subcategory,
                category=category_id)
    
              return templates.TemplateResponse("done.html",{
                "request": request,
                })


@router.post("/add_category/")
async def create_category(request:Request,category_image: UploadFile = File(...),
            name: str = Form(...),
            description:str =Form(...),
            ):
    # if await Category.exists(name=name):
    #     return {"message": "category already exists"}


          slug = slugify(name)

          FILEPATH = "static/img/product/"
          filename = category_image.filename
          extension = filename.split(".")[1] 
          imagename = filename.split(".")[0] 

          if extension not in ["png", "jpg", "jpeg", "jfif"]:
              return{"status": "error","detial": "File extension not allowed"}

          dt = datetime.now()
          dt_timestamp = round(datetime.timestamp(dt))

          modified_image_name = imagename+"_"+str(dt_timestamp)+"."+extension
          genrated_name = FILEPATH + modified_image_name
          file_content = await category_image.read()
        
          with open (genrated_name, "wb") as file:
              file.write(file_content)

          file.close()

          category_obj = await Category.create(
                 category_image=genrated_name,
                 name=name,
                 slug=slug,
                 description=description)
                
          return templates.TemplateResponse("done.html",{
                "request": request,
                })





