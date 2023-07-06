# More Commands

## Insert One

Every single thing that we store inside a database in MongoDB
is called a document. It lives inside the collections, while
databases hosts the collections:

db.{collection_name}.insertOne({object})

Here's a sample command snippet:

```
db.users.insertOne({name: "John" })
```

The documents doesn't need to have the same dimension. As such,
we can add this along with the previous document:

```
db.users.insertOne( { name: "Sally", age: 19, address: { street: "987 North St" }, hobbies: [ "Running" ] })
```

## Looking inside a collection

We can use this command to look inside a collection:

db.{collection_name}.find()

Here's a sample command snippet:

```
db.users.find()
```

## Inserting multiple documents

We can insert multiple documents to a collection using:

db.{collection_name}.insertMany()

This will take an array of objects. Here's a sample command:

```
db.users.insertMany( [ { name: "Jack"}, { name: "Jill" }])
```
