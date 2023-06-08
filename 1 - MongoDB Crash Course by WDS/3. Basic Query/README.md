# Basic Query Commands

## Limiting find

If we want to limit the result of our query to the first n objects,
we can use:

db.{collection_name}.find().limit({n})

Where n is an integer for the number of objects that we want.
Here's a sample command snippet:

```
db.users.find().limit(2)
```

## Sorting find

If we want to sort our find query, we can use:

db.{collection_name}.find().sort({your_key})

We use a key when sorting, here's a sample command snippet
when sorting the name alphabetically:

```
db.users.find().sort( { name: 1} ).limit(2)
```

or we can also do, if we want to start taking from the
last object:

```
db.users.find().sort( { name: -1 } ).limit(2)
```

Furthermore, we can also use multiple fields when sorting.
Here's a sample command snippet:

```
db.users.find().sort( {age: -1, name: -1} ).limit(2)
```

## Skipping

If we want to skip an m number of entries, we can use:

db.{collection_name}.find().skip(m).limit(n)

Here's a sample command snippet:

```
db.users.find().skip(1).limit(2)
```

## Where queries

If you want to get the entries that has a certain field value,
you can try this:

db.{collection_name}.find( { {field_name} : {field_value} })

Here's a sample command snippet:

```
db.users.find( { age : 19 })
```

However, if you want to be more specific, you can also get
just the values of certain fields in an entry.

db.{collection_name}.find( { {field_name} : {field_value} }, { {desired_field_name} : 1, {desired_field_name2} : 1})

Here's a sample command snippet:

```
db.users.find( { age : 19 }, { name: 1, age: 1 })
```

We can also exclude a certain field in an entry by doing this:

```
db.users.find( { age : 19 }, { age: 0 })
```

Likewise, if you don't want the object id to be returned, do this:

```
db.users.find( { age : 19 }, { _id: 0 })
```