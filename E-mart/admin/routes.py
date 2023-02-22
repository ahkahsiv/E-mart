from . models import *
from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import APIRouter, Request , Form, status
from fastapi.templating import Jinja2Templates
from slugify import slugify
from datetime import datetime


router = APIRouter()
templates= Jinja2Templates ( directory = "user/templates" )


@router.get("/first/", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse("product.html",{
        "request": request,
    })


@router.get("/")
async def index(request:Request):
    product = await Product.all() 
    return templates.TemplateResponse("index.html",{
        "request": request,
        "product":product,
    })

@router.get("/second/")
async def read_item(request:Request):
    return templates.TemplateResponse("electronic.html",{
        "request": request,
    })

@router.get("/third/")
async def third(request:Request):
    return templates.TemplateResponse("jewellery.html",{
        "request": request,
    })

@router.get("/four/")
async def four(request:Request):
    return templates.TemplateResponse("fashion.html",{
        "request": request,
    })


@router.get("/category_page/", response_class=HTMLResponse)
async def four(request:Request):
    return templates.TemplateResponse("category.html",{
        "request": request,
    })


@router.get("/sub_category_page/", response_class=HTMLResponse)
async def four(request:Request):
    return templates.TemplateResponse("sub_category.html",{
        "request": request,
    })


@router.get("/product_page/")
async def read_item(request:Request):
     
     return templates.TemplateResponse("add_product.html",{
          "request":request,
          
     })




@router.post("/Category/")
async def create_category(request:Request,
            name: str = Form(...),
            description:str =Form(...),
            ):
    if await Category.exists(name=name):
        return {"message": "category already exists"}
    else:

          slug = slugify(name)

          category_obj = await Category.create(
                 name=name,
                 slug=slug,
                 description=description)
                
          return templates.TemplateResponse("index.html",{
               'request':request
          })


@router.post("/SubCategory/")
async def create_subcategory(request:Request,
            name: str = Form(...),category_id: str = Form(...), description:str=Form(...),
            ):
          category = await Category.get(id=category_id)
          slug = slugify(name)

          

          subcategory_obj = await SubCategory.create(
                 name=name,
                 slug=slug,
                 category=category,
                 description=description)

          return templates.TemplateResponse("index.html",{
               'request':request
          })


@router.post("/product/")   
async def create_product(request:Request,image: UploadFile = File(...),
                         product_name:str= Form(...),
            sellingPrice:float = Form(...),
            description:str = Form(...),
            brand:str = Form(...),
            sub_category_id:str = Form(...),
            category_id:str =Form(...)):
          print(category_id)
          sub_category_id=int(sub_category_id)
          category_id=int(category_id)


          category = await Category.get(id = category_id)
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
                product_name=product_name,
                product_image=genrated_name,
                selling_price=sellingPrice,
                description=description,
                brand=brand, 
                subcategory=subcategory,
                category=category)
    
              return templates.TemplateResponse("index.html",{
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





