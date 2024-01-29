Table "arrivals" {
  "id" integer [not null]
  "quantity" int [not null]
  "price" double [not null]
  "date" Date [not null]
  "supplierId" integer [not null]
  "warehouseId" integer [not null]
  "productId" integer [not null]
}

Table "customers" {
  "id" integer [not null]
  "firstName" string [not null]
  "lastName" string [not null]
  "email" string [not null]
}

Table "orders" {
  "id" integer [not null]
  "orderDate" Date [not null]
  "quantity" int [not null]
  "price" double [not null]
  "customerAddress" string [not null]
  "customerId" integer [not null]
  "productId" integer [not null]
  "warehouseId" integer [not null]
}

Table "products" {
  "id" integer [not null]
  "name" string [not null]
  "description" string [not null]
  "price" double [not null]
}

Table "suppliers" {
  "id" integer [not null]
  "companyName" string [not null]
  "address" string [not null]
  "contactPerson" string [not null]
  "email" string [not null]
}

Table "warehouses" {
  "id" integer [not null]
  "name" string [not null]
  "addres" string [not null]
}

Ref "g":"suppliers"."id" < "arrivals"."supplierId"
Ref "g":"warehouses"."id" < "arrivals"."warehouseId"
Ref "g":"products"."id" < "arrivals"."productId"

Ref "g":"customers"."id" < "orders"."customerId"
Ref "g":"products"."id" < "orders"."productId"
Ref "g":"warehouses"."id" < "orders"."warehouseId"


