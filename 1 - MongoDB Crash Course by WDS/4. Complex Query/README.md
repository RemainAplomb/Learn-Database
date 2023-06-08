# Complex Query

## Dollar notation for getting entries for certain field values

For more complex queries, we can use the dollar notation.

```
db.users.find( { name : { $eq : "Sally" } })
```

or if you want entries that are not equal to sally,
do this:

```
db.users.find( { name : { $ne : "Sally" } })
```

For more details, go here: 

https://www.mongodb.com/docs/manual/reference/operator

## Dollar notation for query comparison

If you want to do query comparison,
you can also use the dollar notation. 

Here's a sample command snippet for greater than:

```
db.users.find( { age : { $gt : 13 } })
```

For more details, you can go to the documentation:

    https://www.mongodb.com/docs/manual/reference/operator/query-comparison/

## Get Entries for multiple field values

To have more flexibility in looking for entries with certain field
values, we can do this:

```
db.users.find( { name: { $in : [ "Jill", "Sally" ] } })
```

This will mean that, all entries that is either Jill or Sally will be 
extracted from the users collection

Otherwise, you can also use not in, here's a sample code snippet:

```
db.users.find( { name: { $nin : [ "Jill", "Sally" ] } })
```

## Get Entries where certain fieldnames exist

To get entries that holds certain fieldnames, do this:

```
db.users.find({ age: { $exists: true } })
```

Basically, if the key exist in a document, it will take it.
Even if that fieldname has null value, it will still take it.

# Combining Queries

## Entries with values in a certain range

If you want to get entries that where the value of a certain field
falls within your specified range, you can do this:

```
db.users.find({ age: { $gte: 15, $lte: 40 } })
```

Here, we have two conditions:
    - If the age is greater than 15
    - and if the age is less than 40

You can even add more, conditions to the query, like:

```
db.users.find({ age: { $gte: 15, $lte: 40 } , name: "Sally" })
```


## Dollar notation with logical operator

To be more readable, we can opt to use "$and".
Here's the command's structure:

db.{collection_name}.find( ${logical_operator} : [ {key1}, ..., {keyN} ] )

Here's a sample command snippet for an and operator:

```
db.users.find({ $and : [ { age: 19}, { name: "Kyle" }] })
```

and here's an or operator:

```
db.users.find({ $or : [ { age: 19}, { name: "Kyle" }] })
```

## Nesting Condition with logical operator

You can also further nest the conditions that you want 
into the query, here's a sample command:

```
db.users.find({ $or : [ { age: { $gte : 15, $lte : 40} }, { name: "Kyle" }] })
```

Here's another example with not operator:

```
db.users.find({ age: { $not : { $gte: 15, $lte: 40 } } })
```

## More examples

Let's start with:

```
db.users.insertMany([ { name: "Tom", balance: 100, debt: 200 }, { name: "Kristin", balance: 20, debt: 0 } ])
```

Let's find where the debt is greater than the balance.
To do that, we will use "$expr"

```
db.users.find({ $expr: { $gt: ["$debt", "$balance" ] } })
```

## More Find examples

You can also nest the field names like this:

```
db.users.find({ "address.street" : { $exists: true } })
```

Here, the streed fieldname is a child of the address, and it
is accessed by adding a dot.

There are also instances where you may want to just find 
a single entry. To do that, you can:

```
db.users.findOne({ balance: { $gte: 15, $lte: 200 } })
```

You can also count the number of documents that matches
your query condition by doing this:

```
db.users.countDocuments({ balance: { $gte: 15, $lte: 200 } })
```