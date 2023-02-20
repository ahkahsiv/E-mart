from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "admin" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "Full_name" VARCHAR(80) NOT NULL,
    "mobile" VARCHAR(10) NOT NULL UNIQUE,
    "email" VARCHAR(50) NOT NULL UNIQUE,
    "password" TEXT NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "last_login" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "category" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL UNIQUE,
    "slug" VARCHAR(200) NOT NULL,
    "description" TEXT NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "subcategory" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL UNIQUE,
    "slug" VARCHAR(200) NOT NULL,
    "description" TEXT NOT NULL,
    "is_active" BOOL,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "create_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "category_id" INT NOT NULL REFERENCES "category" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "product" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "product_name" VARCHAR(200) NOT NULL UNIQUE,
    "brand" VARCHAR(300) NOT NULL,
    "product_image" TEXT NOT NULL,
    "selling_price" INT NOT NULL,
    "description" VARCHAR(300) NOT NULL,
    "is_active" BOOL,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "create_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "category_id" INT NOT NULL REFERENCES "category" ("id") ON DELETE CASCADE,
    "subcategory_id" INT NOT NULL REFERENCES "subcategory" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
