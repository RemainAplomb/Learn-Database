# Update Commands

## Updating a single document

This is similar to find, but instead of just extracting the document 
or fields that we want, we will update it. As such, most of the 
previous topics about find is also applicable here.

db.{collection_name}.updateOne({keys}, { $set: {updates}})

Here's a sample command snippet:

```
db.users.updateOne({ age: 19 }, { $set: { age: 27 } })
```

## Updating using ObjectId
A better way to update is to use the document's id.
You can do it like this:

```
db.users.updateOne({ _id: ObjectId("6481556d85f793240d8d219e") }, { $set: { age: 18 } })
```

## Using increment instead of set

Sometimes, we just want to add to the existing value inside the field.
To do this, we should use "$inc" instead of "$set"

```
db.users.updateOne({ _id: ObjectId("6481556d85f793240d8d219e") }, { $inc: { age: 3 } })
```

## Renaming column/fieldnames

If you want to update a certain column's name, you can use 
"$rename", here's how it is done:

```
db.users.updateOne({ _id: ObjectId("6481556d85f793240d8d219e") }, { $rename: { name: "firstName" } })
```

## Unset a property

You may also want to unset the value of a field. To do this, you can use
"$unset" like this:

```
db.users.updateOne({ _id: ObjectId("6481556d85f793240d8d219e") }, { $unset: { age: "" } })
```

## Pushing new values

If you want to push a new value into a document, you can use
"$push". It is done like this:

```
db.users.updateOne({ _id: ObjectId("6481556d85f793240d8d219e") }, { $push: { age: 21 } })
```

and here's another sample command snippet:

```
db.users.updateOne({ _id: ObjectId("6481556d85f793240d8d219e") }, { $push: { hobbies: "Swimming" } })
```

## Pulling values from a field's list

If you want to remove a value from a field, use "$pull".
It is done like this:

```
db.users.updateOne({ _id: ObjectId("6481556d85f793240d8d219e") }, { $pull: { hobbies: "Swimming" } })
```

## Updating multiple/many documents

Just like findMany, the updateMany will look for entries that matches
the condition that was given to it. Then, it will update the specified
values in those documents.

It is done like this:

```
db.users.updateMany({ name: { $exists: true} }, { $push: { hobbies: "Reading" } })
```

## Replacing a single document

If you want to replace a document, you can do this:

```
db.users.replaceOne({ age: 21 }, { name: "Not Sally" })
```

This will delete everything in the document that was found.
After that, it will replace it with the object that we pass 
into it.

Since I don't want to remove the Sally document,
let's turn it back using replace:

```
db.users.replaceOne({ name: "Not Sally" }, { address: { street: '987 North St' }, hobbies: [ 'Running', 'Swimming', 'Reading' ], name: 'Sally', age: [ 21 ] })
```

## Delete an entry

If you want to delete an entry/document, you can use this:

```
db.users.deleteOne({ name: "Jack" })
```

Then, try looking for it:

```
db.users.findOne({ name: "Jack" })
```

## Deleting multiple entries/documents

To delete multiple documents/entries, you can do this:

```
db.users.deleteMany({ age: { $exists: false}, balance: { $exists: false} })
```

and look for it now:

```
db.users.find({ age: { $exists: false}, balance: { $exists: false} })
```