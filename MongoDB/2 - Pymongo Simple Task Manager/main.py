#   Import pymongo MongoClient
#   If you do not have the pymongo library,
#   you can install it by doing this:
#       pip install pymongo
from pymongo import MongoClient

from pymongo import MongoClient

class TaskManager:
    def __init__(self):
        # Connect to MongoDB server
        self.client = MongoClient("mongodb://127.0.0.1:27017/")
        # Access the "task_manager_db" database
        self.db = self.client["task_manager_db"]
    
    def add_data(self, collection="tasks", document=None, many=False):
        # Check if the document is provided
        if document is None:
            return False, "Error: Document is None"
        
        try:
            if many:
                # Insert multiple documents into the specified collection
                result = self.db[collection].insert_many(document)
            else:
                # Insert a single document into the specified collection
                result = self.db[collection].insert_one(document)
            
            return True, result
        except Exception as e:
            return False, str(e)
    
    def find(self, collection="tasks", condition=None, limit=None):
        try:
            if condition is None and limit is None:
                # Retrieve all documents from the specified collection
                result = self.db[collection].find()
            elif condition is None and limit is not None:
                # Retrieve documents with limit from the specified collection
                result = self.db[collection].find().limit(limit)
            elif condition is not None and limit is None:
                # Retrieve documents based on the given condition from the specified collection
                result = self.db[collection].find(condition)
            elif condition is not None and limit is not None:
                # Retrieve documents based on the given condition with limit from the specified collection
                result = self.db[collection].find(condition).limit(limit)
            else:
                return False, "Error: Condition and Limit are None"
            
            return True, result
        except Exception as e:
            return False, str(e)
    
    def update(self, collection="tasks", filters=None, new_values=None, many=True):
        try:
            if filters is None or new_values is None:
                return False, "Error: Missing filter or new value"
            
            if many:
                # Update multiple documents in the specified collection based on filters
                result = self.db[collection].update_many(filters, new_values)
            else:
                # Update a single document in the specified collection based on filters
                result = self.db[collection].update_one(filters, new_values)
            
            return True, result
        except Exception as e:
            return False, str(e)
    
    def delete(self, collection="tasks", filters=None, many=True):
        try:
            if filters is None:
                return False, "Error: Missing filter"
            
            if many:
                # Delete multiple documents from the specified collection based on filters
                result = self.db[collection].delete_many(filters)
            else:
                # Delete a single document from the specified collection based on filters
                result = self.db[collection].delete_one(filters)
            
            return True, result
        except Exception as e:
            return False, str(e)
    
    def exit_db(self):
        # Close the MongoDB client connection
        self.client.close()


if __name__ == "__main__":
    # Create an instance of TaskManager
    task_manager = TaskManager()

    # Test the add_data method
    document = {
        "title": "Finish project",
        "description": "Complete the task management project",
        "status": "In progress"
    }
    success, result = task_manager.add_data(document=document)
    if success:
        print("Task added successfully:", result.inserted_id)
    else:
        print("Failed to add task:", result)

    # Test the find method
    success, result = task_manager.find()
    if success:
        print("Tasks found:")
        for task in result:
            print(task)
    else:
        print("Failed to find tasks:", result)

    # Test the update method
    filters = {"status": "In progress"}
    new_values = {"$set": {"status": "Completed"}}
    success, result = task_manager.update(filters=filters, new_values=new_values)
    if success:
        print("Task updated successfully:", result.modified_count)
    else:
        print("Failed to update task:", result)

    # Test the delete method
    # filters = {"status": "Completed"}
    # success, result = task_manager.delete(filters=filters)
    # if success:
    #     print("Task deleted successfully:", result.deleted_count)
    # else:
    #     print("Failed to delete task:", result)

    # Close the database connection
    task_manager.exit_db()
